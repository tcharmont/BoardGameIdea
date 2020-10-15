from cx_Freeze import setup, Executable

setup(
    name="BoardGameIdea",
    version="1.0",
    description="Generate idea for board game creation",
    executables=[Executable("view.py")],
)
