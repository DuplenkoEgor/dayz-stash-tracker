import click
import storage as st
import core
from cli import format_stash


@click.group()
def app():
    """Stash tracker"""


@app.command("add")
@click.argument("number", type=int)
@click.argument("city")
@click.argument("x", type=float)
@click.argument("y", type=float)
@click.argument("hint", nargs=-1, required=True)
def add(number, city, x, y, hint):
    """Add a new stash: add NUMBER CITY X Y HINT..."""
    stashes = st.load_stashes()
    try:
        core.add_stash(stashes, number, city, x, y, " ".join(hint), False)
        click.echo("Added")
    except ValueError as error:
        click.echo(f"error: {error}")


@app.command("show")
def show():
    """Show all stashes"""
    stashes = st.load_stashes()
    if not stashes:
        click.echo("Nothing found")
    for stash in stashes:
        click.echo(format_stash(stash))


@app.command("search")
@click.argument("city")
def search(city):
    """Search stashes by city"""
    stashes = st.load_stashes()
    result = core.search_by_city(stashes, city)
    if not result:
        click.echo("Nothing found")
    for stash in result:
        click.echo(format_stash(stash))


@app.command("edit")
@click.argument("number", type=int)
@click.argument("city")
@click.argument("x", type=float)
@click.argument("y", type=float)
@click.argument("hint", nargs=-1, required=True)
@click.option("--found", is_flag=True, help="Mark stash as found")
def edit(number, city, x, y, hint, found):
    """Edit stash: edit NUMBER CITY X Y HINT... [--found]"""
    stashes = st.load_stashes()
    try:
        core.edit_stash(stashes, number, city, x, y, " ".join(hint), found)
        click.echo("Edit done!")
    except ValueError as error:
        click.echo(f"error: {error}")


@app.command("delete")
@click.argument("number", type=int)
def delete(number):
    """Delete stash by number"""
    stashes = st.load_stashes()
    try:
        core.del_stash(stashes, number)
        click.echo("Deleted!")
    except ValueError as error:
        click.echo(f"error: {error}")


if __name__ == "__main__":
    app()