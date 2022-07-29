import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call(['git', 'checkout', 'main'])
subprocess.check_call(['git', 'pull'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install','-r','requirements.txt'])
subprocess.check_call(['pytest', 'tests/'])
subprocess.check_call(['python3', 'script.py'])
