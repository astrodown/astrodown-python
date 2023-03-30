import os
from typing import Optional
import typer
from typer import Typer
from astrodown.cli.check import (
    print_health_table,
    command_path,
    required_programs,
)
from astrodown.cli.utils import colored_text, get_package_manager, run_shell
from astrodown.cli.install import PackageManager
from rich import print
from astrodown.cli.new import ComponentType


app = Typer(
    rich_markup_mode="rich",
    no_args_is_help=True,
    epilog="""
    Report [bold red]bugs[/bold red] on [link=https://github.com/astrodown/astrodown-web/]Github[/link]
    """,
)


@app.command()
def init(
    path: str = typer.Option(
        os.getcwd(),
        "--path",
        "-p",
        prompt="Project Directory",
        help="path to create the project, default to the current working directory",
        writable=True,
    ),
    name: str = typer.Option(
        None,
        "--name",
        "-n",
        help="name of the project",
        show_default=False,
        prompt="Project Name",
    ),
    package_manager: PackageManager = typer.Option(
        PackageManager.npm,
        "--package-manager",
        "-pm",
        prompt="Node.js Package Manager",
        help="package manager to use, default to npm",
    ),
):
    """
    [bold blue]Scaffold[/bold blue] an astrodown project at given path.

    Must have Node.js installed and avaiable in PATH variables, see https://nodejs.org for installation instructions.
    """
    if path is None:
        path = os.getcwd()

    all_required_programs = [*required_programs, package_manager]
    program_availabilities = {
        program: command_path(program) for program in all_required_programs
    }

    for program in program_availabilities:
        if program_availabilities[program] is None:
            print(
                colored_text(
                    "Some of the required programs are not installed, see the table below for details",
                    color="red",
                )
            )
            print_health_table(program_availabilities)
            raise typer.Exit()

    print(
        f"Creating project {colored_text(name)} at {colored_text(path)} with package manager {package_manager}"
    )


@app.command()
def install(
    package_manager: PackageManager = typer.Option(
        get_package_manager(), help="package manager to use"
    )
):

    return run_shell(f"{package_manager} install")


@app.command()
def dev(
    package_manager: PackageManager = typer.Option(
        get_package_manager(), help="package manager to use"
    ),
    port: Optional[int] = typer.Option(3000, help="port to run the website"),
):
    """
    [bold blue]Preivew[/bold blue] the website
    """
    run_shell(f"{package_manager} run dev")


@app.command(rich_help_panel="Utils")
def new(
    component_type: ComponentType = typer.Argument(
        ..., help="the type of the component to be created"
    )
):
    """
    [bold blue]Create[/bold blue] the folder structure for a new analysis, dataset, model, api, etc.
    """
    pass


@app.command(rich_help_panel="Utils")
def docs():
    """
    [bold blue]Open[/bold blue] documentation websites for relevant tools, e.g. Quarto, Python, etc.
    """
    pass


@app.command(rich_help_panel="Utils")
def check():
    """
    Check for availabilities of programs required by astrodown
    """
    missing_programs = print_health_table()
    if len(missing_programs) == 0:
        print("All things installed," + colored_text(" you are good to go!"))
    else:
        print(
            "The following tools are missing "
            f"{colored_text(missing_programs, color='red')}\n"
            "please make sure they are installed and available in PATH variables"
        )


@app.callback(context_settings={"ignore_unknown_options": True})
def callback(ctx: typer.Context):
    """
    [bold blue]Astrodown[/bold blue] is a toolkit to build interactive websites for data science projects.

    See a live example at https://astrodown-playground.qiushiyan.dev :sparkles:
    """


if __name__ == "__main__":
    app()
