import typer

cli = typer.Typer()

@cli.command()
def greet(command, me):
    print(f"Hello {me}")

if __name__ == "__main__":
    cli()