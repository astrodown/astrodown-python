import os
from pathlib import Path
import shutil
from astrodown.quarto import (
    move_quarto_resources_to_public,
    adjust_resource_links,
    add_html_dep,
)


analysis_dir = "analysis"
data_dir = "data"
content_dir = "src/content"

output_dir = (
    content_dir
    if os.getenv("QUARTO_PROJECT_OUTPUT_DIR") is None
    else os.getenv("QUARTO_PROJECT_OUTPUT_DIR")
)

move_quarto_resources_to_public(Path(output_dir, analysis_dir))
move_quarto_resources_to_public(Path(output_dir, data_dir))
# move reamining html depenedencies generated by usage of htmlwidgets
move_quarto_resources_to_public(Path(data_dir))
move_quarto_resources_to_public(Path(analysis_dir))

if os.getenv("QUARTO_PROJECT_OUTPUT_FILES") is not None:
    output_files = os.getenv("QUARTO_PROJECT_OUTPUT_FILES").split("\n")
    for file in output_files:
        adjust_resource_links(file)
        if file == f"{content_dir}/index.md":
            move_quarto_resources_to_public(content_dir)
            dst = "src/pages/index.md"
            if os.path.exists(dst):
                os.remove(dst)
            shutil.move(file, "src/pages")
            html_dir = Path("index_files")
            if html_dir.exists():
                add_html_dep(html_dir / "libs")
                shutil.rmtree(html_dir)