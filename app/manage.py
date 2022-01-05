import typer
import uvicorn

from commands.migrate_cli import migrate_cli
from commands.user_cli import user_cli
from main import app

typer_app = typer.Typer()


@typer_app.command()
def run(reload: str = typer.Option("", help="Run development server.")):
    uvicorn.run(app, host="localhost", port=8080, reload=reload)


typer_app.add_typer(user_cli, name="user")
typer_app.add_typer(migrate_cli, name="alembic")

if __name__ == "__main__":
    typer_app()
