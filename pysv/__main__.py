from pysv.functions.general import p_print, make_config
from pysv.tui.session import Session
import click


@click.command()
@click.option("--file", "-f", is_flag=False, help="CSV file that should be pre-loaded.")
def main(file: str) -> None:
    make_config()

    # Create session
    session = Session()

    if file:
        session.load_file(file)
    # main loop
    try:
        while True:
            # run the session until the user quits
            session.run()
    except KeyboardInterrupt:
        p_print("<grey>Bye!!!</grey>")


if __name__ == "__main__":
    main()
