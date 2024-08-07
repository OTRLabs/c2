# src/commander/superficial/strings/languages/EN_US.py

from __future__ import annotations
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from datetime import datetime

class EN_US_Strings:
    class WebUIStrings:
        EXAMPLE: str = "Example"
        WELCOME: str = "Welcome to Commander"
        LOGIN: str = "Log In"
        LOGOUT: str = "Log Out"
        DASHBOARD: str = "Dashboard"
    
    class CliStrings:
        INITIALIZATION_MESSAGE: str = "Initializing Commander..."
        COMMAND_NOT_FOUND: str = "Command not found. Type 'help' for a list of commands."
        HELP_MESSAGE: str = "Available commands:"

    class ErrorMessages:
        GENERAL_ERROR: str = "An error occurred. Please try again."
        AUTHENTICATION_FAILED: str = "Authentication failed. Please check your credentials."
        PERMISSION_DENIED: str = "Permission denied. You don't have access to this resource."

    @staticmethod
    def get_welcome_message(console: Console) -> None:
        welcome_panel = Panel(
            Text("Welcome to Commander", style="bold green"),
            subtitle=f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        )
        console.print(welcome_panel)

    @staticmethod
    def print_help_menu(console: Console, commands: dict[str, str]) -> None:
        table = Table(title="Commander Help Menu")
        table.add_column("Command", style="cyan", no_wrap=True)
        table.add_column("Description", style="magenta")

        for command, description in commands.items():
            table.add_row(command, description)

        console.print(table)