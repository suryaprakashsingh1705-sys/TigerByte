# src/debug.py
"""
Handles debug output formatting for the TigerByte interpreter.
"""

# Optional: Using simple print for now, can add 'chalk' later for colors
# If adding chalk: run `pip install chalk` and uncomment lines

# import chalk

class Debugger:
    def __init__(self, enabled=False):
        """Initializes the Debugger.

        Args:
            enabled (bool): Whether debug output should be printed.
        """
        self.enabled = enabled
        if self.enabled:
            # print(chalk.yellow("🐯 TigerByte Debug Mode Activated!"))
            print("🐯 TigerByte Debug Mode Activated!")

    def log(self, message: str):
        """Prints a general debug message if enabled."""
        if not self.enabled:
            return
        # print(chalk.blue(f"[DEBUG] {message}"))
        print(f"[DEBUG] {message}")

    def show_tokens(self, tokens):
        """Prints the list of tokens if debug mode is enabled.
           (Placeholder for when tokenizer exists)
        """
        if not self.enabled:
            return

        # print(chalk.cyan("\n[DEBUG] Tokens:"))
        print("\n[DEBUG] Tokens:")
        if tokens:
            formatted_tokens = "\n".join([f"  {tok}" for tok in tokens])
            print(formatted_tokens)
        else:
            print("  (No tokenizer implemented yet)")


    def show_ast(self, ast_node):
        """Prints the AST if debug mode is enabled.
           (Placeholder for when parser exists)
        """
        if not self.enabled:
            return

        # print(chalk.magenta("\n[DEBUG] AST / Structure:"))
        print("\n[DEBUG] AST / Structure:")
        if ast_node:
             print(f"  {ast_node}")
        else:
            print("  (No parser/AST implemented yet)")

    def show_line_execution(self, line_number: int, line: str):
        """Prints the line being executed."""
        if not self.enabled:
            return
        # print(chalk.green(f"[EXECUTE:{line_number}]> {line}"))
        print(f"[EXECUTE:{line_number}]> {line}")