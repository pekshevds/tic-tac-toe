import os


def cls() -> None:
    """
    Очищает экран"""
    os.system("cls" if os.name == "nt" else "clear")
