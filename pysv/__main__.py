from pysv.functions.general import p_print, make_config
from pysv.tui.session import Session


def main() -> None:
    make_config()

    # Create session
    session = Session()

    # main loop
    try:
        while True:
            # run the session until the user quits
            session.run()
    except KeyboardInterrupt:
        p_print("<grey>Bye!!!</grey>")


if __name__ == "__main__":
    main()
