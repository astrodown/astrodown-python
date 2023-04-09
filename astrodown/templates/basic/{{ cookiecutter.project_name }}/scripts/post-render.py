import os
from pathlib import Path
import shutil
from astrodown.cli.utils import get_astrodown_config
from astrodown.quarto import move_assets, move_html_assets, adjust_resource_links

config = get_astrodown_config()

analysis_dir = config["analysis_dir"]
data_dir = config["data_dir"]
public_dir = Path(os.getcwd(), "public")
content_dir = Path(os.getcwd(), "src/content")
output_dir = (
    content_dir
    if os.getenv("QUARTO_PROJECT_OUTPUT_DIR") is None
    else os.getenv("QUARTO_PROJECT_OUTPUT_DIR")
)

# create /public if it doesn't exist
if not public_dir.exists():
    public_dir.mkdir()

move_assets(Path(output_dir, analysis_dir), public_dir)
move_assets(Path(output_dir, data_dir), public_dir)
# move reamining html depenedencies generated by usage of htmlwidgets
move_html_assets(data_dir, public_dir)
move_html_assets(analysis_dir, public_dir)

if os.getenv("QUARTO_PROJECT_OUTPUT_FILES") is not None:
    output_files = os.getenv("QUARTO_PROJECT_OUTPUT_FILES").split("\n")
    index_md = f"{output_dir}/index.md"
    for file in output_files:
        adjust_resource_links(file)
        if file in index_md:
            move_assets(output_dir, public_dir)
            dst = Path(os.getcwd(), "src/pages/_index.md")
            if os.path.exists(dst):
                os.remove(dst)
            shutil.copy(index_md, dst)
            html_dir = Path("index_files")
            if html_dir.exists():
                move_html_assets(html_dir, public_dir)
                shutil.rmtree(html_dir)
