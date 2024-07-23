import subprocess



# res = subprocess.run(['git', 'clone', 'https://github.com/Atul-Torane/test.git' ,'D://Codes//gith'], check=True)
# res = subprocess.run(['cd', 'D://Codes//gith//newfile'], check=True)
res = subprocess.run(['git', 'add', '.'], check=True)
print(res)
res = subprocess.run(['git', 'commit', '-m', 'first commit'], check=True)
print(res)