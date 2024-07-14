import subprocess

scripts = ['CCAR.py', 'CCAR2.py']

for script in scripts:
    result = subprocess.run(['python', script])
    if result.returncode != 0:
        print(f"Script {script} failed with return code {result.returncode}")
        break
