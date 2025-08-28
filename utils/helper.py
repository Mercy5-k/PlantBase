# helper.py
import textwrap
from tabulate import tabulate

def wrap_text(text, width=15):
    """Wrap long text for nicer table display."""
    return textwrap.fill(str(text), width=width)

def print_table(data, headers, title=None, width=15):
    """
    Utility function to display tabular data nicely using tabulate.
    - data: list of lists (rows)
    - headers: list of column names
    - title: optional title string
    """
    # Wrap all text in the data for consistent formatting
    wrapped_data = [
        [wrap_text(cell, width=width) for cell in row]
        for row in data
    ]

    if title:
        print(f"\n📋 {title}")

    print(tabulate(
        wrapped_data,
        headers=headers,
        tablefmt="fancy_grid"
    ))

def get_int_input(prompt, default=None):
    """
    Safely get integer input from the user.
    Returns default if input is empty.
    Keeps asking until a valid integer is entered.
    """
    while True:
        val = input(prompt).strip()
        if val == "" and default is not None:
            return default
        if val.isdigit():
            return int(val)
        print("❌ Please enter a valid number.")


def confirm_action(prompt="Are you sure? (y/n): "):
    """
    Ask user to confirm an action.
    Returns True if 'y' or 'yes', False otherwise.
    """
    return input(prompt).strip().lower() in ["y", "yes"]
