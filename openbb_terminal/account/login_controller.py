from openbb_terminal.rich_config import console
from openbb_terminal.account.login_model import (
    get_saved_token_if_valid,
    request_token,
    launch_terminal,
)


def display_welcome_message():
    console.print(
        "You need to be connected to use the installer version of OpenBB."
        "\nTo register please go on: https://my.openbb.co/register"
    )


def login_prompt():
    display_welcome_message()
    while True:
        console.print("\nPlease enter your credentials:")
        email = console.input("> Email: ", style="yellow")
        password = console.getpass("> Password: ", style="yellow")
        save_str = console.input("> Keep me logged in? [y/n]: ").lower()

        if save_str == "y":
            save = True
        elif save_str == "n":
            save = False

        login_info = request_token(email, password, save)
        if login_info:
            break

    return launch_terminal(login_info)


def main():
    """Main function"""
    login_info = get_saved_token_if_valid()
    if login_info:
        return launch_terminal(login_info)
    return login_prompt()


if __name__ == "__main__":
    main()
