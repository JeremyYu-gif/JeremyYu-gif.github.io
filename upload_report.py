#!/usr/bin/env python3
import base64
import json
import subprocess
import sys

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.returncode

def upload_to_github(file_path, repo, message):
    with open(file_path, 'rb') as f:
        content = base64.b64encode(f.read()).decode()
    
    # Get current file SHA if exists
    filename = file_path.split('\\')[-1] if '\\' in file_path else file_path.split('/')[-1]
    cmd = f'gh api repos/{repo}/contents/{filename} --jq ".sha"'
    sha, _ = run_cmd(cmd)
    
    # Prepare API call
    if sha:
        cmd = f'gh api repos/{repo}/contents/{filename} --method PUT --field message="{message}" --field content="{content}" --field sha="{sha}"'
    else:
        cmd = f'gh api repos/{repo}/contents/{filename} --method PUT --field message="{message}" --field content="{content}"'
    
    result, code = run_cmd(cmd)
    return result, code

if __name__ == '__main__':
    file_path = r'c:\Users\yujia\repos\JeremyYu-gif.github.io\TOP-stock-daily-20260416.html'
    repo = 'JeremyYu-gif/JeremyYu-gif.github.io'
    message = 'Add TOP stock daily report 20260416'
    
    result, code = upload_to_github(file_path, repo, message)
    print(result)
    sys.exit(code)
