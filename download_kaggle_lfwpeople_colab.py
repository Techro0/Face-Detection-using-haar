
import os, sys, subprocess

def run(cmd):
    print("+", cmd)
    r = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print(r.stdout)

# Ensure Kaggle is available
run("pip -q install kaggle")
os.makedirs(os.path.expanduser("~/.kaggle"), exist_ok=True)

# Expect kaggle.json in the current directory (upload it in Colab first)
if not os.path.exists("kaggle.json"):
    raise SystemExit("Please upload kaggle.json in this working directory before running this script.")

run("cp kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json")
os.makedirs("data", exist_ok=True)
run("kaggle datasets download -d atulanandjha/lfwpeople -p data --unzip")
print("Downloaded to data/")
