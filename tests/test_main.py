import subprocess
import sys

def test_main_computes_double():
    p = subprocess.run([sys.executable, "main.py", "3"], capture_output=True, text=True)
    assert "result: 6" in p.stdout