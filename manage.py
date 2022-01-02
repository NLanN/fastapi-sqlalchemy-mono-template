import typer
import uvicorn

from src.commands.user_cli import user_cli
from src.main import app

typer_app = typer.Typer()


@typer_app.command()
def run(reload: str = typer.Option("", help="Run development server.")):
    uvicorn.run(app, host="localhost", port=8080, reload=reload)


typer_app.add_typer(user_cli, name="users")

if __name__ == "__main__":
    typer_app()
