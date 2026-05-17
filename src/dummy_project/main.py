"""Simple dummy project entry points."""


def hello(name: str = "world") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def main() -> None:
    """Run the module as a script."""
    print(hello())


if __name__ == "__main__":
    main()
