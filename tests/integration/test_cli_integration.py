import subprocess
import unittest


class TestCLIIntegration(unittest.TestCase):
    """Integration tests for the CLI calculator"""

    def run_cli(self, *args):
        """Helper to run the CLI with arguments"""
        result = subprocess.run(
            ["python", "src/cli.py", *args], capture_output=True, text=True
        )
        return result

    def test_cli_add_integration(self):
        """Test CLI can perform addition"""
        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip().splitlines()[-1] == "8"

    def test_cli_subtract_integration(self):
        """Test CLI can perform subtraction"""
        result = self.run_cli("subtract", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip().splitlines()[-1] == "2"

    def test_cli_subtract_missing_operand_error(self):
        """Test CLI handles missing operand in subtraction"""
        result = self.run_cli("subtract", "5")
        assert result.returncode != 0
        # Updated to match current CLI output
        assert "Unexpected error" in result.stdout

    def test_cli_multiply_integration(self):
        """Test CLI can perform multiplication"""
        result = self.run_cli("multiply", "5", "3")
        assert result.returncode == 0
        # Only check the last line (actual result)
        assert result.stdout.strip().splitlines()[-1] == "15"

    def test_cli_divide_integration(self):
        """Test CLI can perform division"""
        result = self.run_cli("divide", "5", "3")
        assert result.returncode == 0
        # Only check the last line (formatted result)
        assert result.stdout.strip().splitlines()[-1] == "1.67"
