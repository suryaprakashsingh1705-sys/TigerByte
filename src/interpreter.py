#!/usr/bin/env python3
"""
🐯 TigerByte Interpreter v0.1
A minimal starter interpreter for TigerByte source files (.tb)
-------------------------------------------------------------
This script reads TigerByte source files, validates them,
and executes simple TigerByte commands.

Author: Your Name
Date: October 2025
License: MIT
"""

import sys
import os


def run_tigerbyte_file(filepath: str):
    """
    Reads and executes a TigerByte (.tb) source file.

    Steps:
    1. Validate file extension
    2. Ensure file exists
    3. Read contents
    4. Execute line-by-line (currently only print commands)
    """

    # ✅ Step 1: Validate file type
    if not filepath.endswith(".tb"):
        print("❌ Error: Only .tb (TigerByte) files are supported.")
        return

    # ✅ Step 2: Check file existence
    if not os.path.exists(filepath):
        print(f"❌ Error: File '{filepath}' not found.")
        return

    # ✅ Step 3: Read the file contents
    with open(filepath, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]

    if not lines:
        print("⚠️ Warning: The TigerByte file is empty.")
        return

    print("🐯 Executing TigerByte source...\n")

    # ✅ Step 4: Execute each line
    for line in lines:
        execute_command(line)


def execute_command(command: str):
    """
    Basic command executor.
    Supports: print "<message>"
    Future: feed, chase, roar, etc.
    """

    if command.startswith("print "):
        # Extract message text
        message = command[len("print "):].strip().strip('"').strip("'")
        print(message)

    else:
        # Placeholder for unrecognized commands
        print(f"⚠️ Unknown command: {command}")


def main():
    """CLI entry point"""
    if len(sys.argv) < 2:
        print("Usage: python src/interpreter.py <filename.tb>")
        sys.exit(1)

    filepath = sys.argv[1]
    run_tigerbyte_file(filepath)


if __name__ == "__main__":
    main()
