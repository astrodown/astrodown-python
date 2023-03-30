import subprocess
from rich import print
import typer
import yaml

from astrodown.cli.install import PackageManager
import os


def run_shell(cmd: str, verbose: bool = True, **kwargs):
    if verbose:
        print(colored_text("\[astrodown]: ") + cmd)
    try:
        completed_process = subprocess.run(cmd, shell=True, check=True, **kwargs)
    except Exception as e:
        print(
            colored_text("\[astrodown]: ", "red")
            + f"Error: command `{cmd}` failed, reason: {e}"
        )
        raise typer.Exit(1)


def colored_text(
    text: str, color: str = "green", bold: bool = True, with_prefix: bool = True
):
    begin_tag = f"[bold {color}]" if bold else f"[{color}]"
    end_tag = f"[/bold {color}]" if bold else f"[/{color}]"
    return f"{begin_tag}{text}{end_tag}"


def config_exists(config_file: str = "_astrodown.yml") -> bool:
    return os.path.exists(config_file)


def get_astrodown_config(config_file: str = "_astrodown.yml"):
    if not config_exists(config_file):
        print(
            colored_text("\[astrodown]: ", "red") + f"config file {config_file} not found"
        )
        return None

    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
    return config


def get_package_manager(config_file: str = "_astrodown.yml") -> PackageManager:
    config = get_astrodown_config(config_file)
    if config is not None:
        return config["node"]["package_manager"]
    else:
        print(
            colored_text("\[astrodown]: ") + "using default package manager",
            colored_text("npm", "green"),
        )
        return PackageManager.npm
