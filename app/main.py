import sys
import os


command_keys = ["echo", "exit", "type"]


def resolve_echo(rest: str) -> bool:
    print(rest)
    return True


def resolve_exit(rest: str) -> bool:
    if rest == "0":
        return False

    print("Error: missing exit number")
    return True


def resolve_type(rest: str) -> bool:
    if rest in command_keys:
        print(rest, "is a shell builtin")
        return True
    

    for folder in os.environ.get('PATH').split(":"):
        if os.path.isfile(f"{folder}/{rest}"):
            print(f"{rest} is {folder}/{rest}")
            return True

    print(f"{rest}: not found")
    return True


command_solvers = [resolve_echo, resolve_exit, resolve_type]

commands = {key: solver for key, solver in zip(command_keys, command_solvers)}

def main() -> None:
    continue_ = True
    while continue_:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input()
        args = user_input.split(" ", 1)

        command = args[0]

        rest = ""
        if len(args) > 1:
            rest = args[1]

        if command in commands.keys():
            continue_ = commands[command](rest)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()