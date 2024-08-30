# A Comprehensive Guide to Capture the Flag Challenges

## Guide Links
[The CTF Primer](https://primer.picoctf.org/)

## Tools:
### Operating System
- Kali WSL
- Win KeX
### How To Install WSL
- [Install WSL Tutorial](https://learn.microsoft.com/en-us/windows/wsl/install)
### How To Install Kali WSL
- [Install Kali WSL](https://www.kali.org/docs/wsl/wsl-preparations/)
## Basic Kali Linux Command-line Tips:
### Navigating the File System
- `pwd`: Print the current working directory.
- `cd [directory]`: Change the current directory.
  - Example: `cd /usr/bin`
- `ls`: List files and directories in the current directory.
  - Use `ls -la` to list all files, including hidden ones, with detailed information.

### Managing Files and Directories
- `cp [source] [destination]`: Copy files or directories.
  - Example: `cp file.txt /home/user/`
- `mv [source] [destination]`: Move or rename files or directories.
  - Example: `mv oldname.txt newname.txt`
- `rm [file]`: Remove a file.
  - Use `rm -r [directory]` to remove a directory and its contents recursively.
- `touch [filename]`: Create a new, empty file.
- `mkdir [directory]`: Create a new directory.

### User Management
- `whoami`: Display the current logged-in user.
- `sudo [command]`: Execute a command as the superuser.
  - Example: `sudo apt update`
- `passwd [username]`: Change the password for a user.
  - Example: `passwd root`

### Networking Commands
- `ifconfig`: Display or configure network interfaces.
- `ping [hostname or IP]`: Test connectivity to a host.
  - Example: `ping google.com`
- `netstat -tuln`: Display listening network connections and services.
- `nmap [target]`: Network exploration and security auditing tool.
  - Example: `nmap -sP 192.168.1.0/24`

### System Information
- `uname -a`: Display detailed information about the system.
- `df -h`: Show disk space usage in human-readable format.
- `top`: Display tasks and system resource usage in real-time.
- `ps aux`: List all running processes with detailed information.

### Package Management
- `apt update`: Update the package list.
- `apt upgrade`: Upgrade all installed packages to their latest versions.
- `apt install [package]`: Install a new package.
  - Example: `apt install nmap`
- `apt remove [package]`: Remove an installed package.
  - Example: `apt remove nmap`

## Kex Command-line Tips
### Run Win-KeX
- Inside of Kali WSL: kex --win -s
### Seamless Mode
- Inside of Kali WSL: kex --sl -s
### Shutdown WSL
- Inside of CMD: wsl --shutdown

## Top 3 Websites to Practice CTF

1. **[Hack The Box](https://www.hackthebox.com/)**
   - A platform that offers a wide range of challenges, from beginner to advanced, focusing on various aspects of cybersecurity. Users can solve challenges, hack machines, and improve their skills in a competitive environment.

2. **[TryHackMe](https://tryhackme.com/)**
   - An interactive learning platform that provides guided lessons on cybersecurity topics through hands-on challenges. It’s beginner-friendly and covers everything from basic networking to advanced penetration testing.

3. **[PicoCTF](https://picoctf.org/)**
   - A beginner-friendly CTF platform designed by Carnegie Mellon University. It offers a series of challenges in various categories like cryptography, forensics, and web exploitation, aimed at helping students and newcomers learn about cybersecurity.

## Best Websites to Decode Things in CTF

1. **[CyberChef](https://gchq.github.io/CyberChef/)**
   - A web-based tool that provides a wide range of functionalities for decoding, encoding, and analyzing data. It's great for quickly solving challenges involving different encodings, cryptographic algorithms, and data manipulation tasks.

2. **[Online Decoder](https://www.dcode.fr/)**
   - A website that offers numerous tools for decoding and solving various types of puzzles, including cryptographic, steganographic, and format-specific challenges. It’s handy for working with different ciphers and encodings.

3. **[Base64 Decode](https://www.base64decode.net/)**
   - A simple and effective tool for decoding Base64 encoded strings. It's useful for challenges that involve encoding or decoding data in Base64 format.

## Go-To Commands When CTFing:
+ **`wget <URL>`**: Download files from the web.
    - Example:
      ```bash
      wget http://example.com/file.txt
      ```
    - This command will download the file `file.txt` from the specified URL and save it in the current directory.

+ **`chmod +x <filename>`**: Change file permissions to make it executable.
   - Example:
     ```bash
     chmod +x exploit.sh
     ```

+ **`./<filename>`**: Run the file.
   - Example:
     ```bash
     ./exploit.sh
     ```

+ **`file ./<filename>`**: View file contents or determine file type.
   - Example:
     ```bash
     file ./mystery_file
     ```
   - Output might be:
     ```
     mystery_file: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked
     ```

+ **`strings <filename>`**: Perform static analysis to extract readable strings from the file.
   - Example:
     ```bash
     strings mystery_file
     ```
   - Output might include:
     ```
     /bin/sh
     GLIBC_2.0
     ```

+ **`ltrace <filename>`**: Trace library calls made by a program.
   - Example:
     ```bash
     ltrace ./mystery_file
     ```
   - Output might show:
     ```
     __libc_start_main(0x4005ed, 1, 0x7ffdf1f37e18, 0x4006f0, 0x400770 <unfinished ...>
     ```

+ **`strace <filename>`**: Trace system calls and signals made by a program.
   - Example:
     ```bash
     strace ./mystery_file
     ```
   - Output might show:
     ```
     execve("./mystery_file", ["./mystery_file"], 0x7ffd41c0) = 0
     ```

+ **`xxd <filename>`**: Create a hexdump of a file, useful for analyzing binary data.
   - Example:
     ```bash
     xxd mystery_file
     ```
   - Output might include:
     ```
     00000000: 7f45 4c46 0201 0100 0000 0000 0000 0000  .ELF............
     ```

+ **`nc <hostname> <port>`**: Use Netcat to connect to a remote server, often for interacting with remote CTF challenges.
   - Example:
     ```bash
     nc example.com 12345
     ```

+ **`tar -xvf <filename>`**: Extract files from a tar archive.
    - Example:
      ```bash
      tar -xvf archive.tar
      ```

+ **`unzip <filename>`**: Extract files from a zip archive.
    - Example:
      ```bash
      unzip archive.zip
      ```

+ **`md5sum <filename>`** / **`sha256sum <filename>`**: Calculate and verify the hash of a file.
    - Example:
      ```bash
      md5sum mystery_file
      ```
    - Output might include:
      ```
      d41d8cd98f00b204e9800998ecf8427e  mystery_file
      ```

+ **`gdb <filename>`**: Start the GNU Debugger to analyze and debug binary files.
    - Example:
      ```bash
      gdb ./mystery_file
      ```
    - Within `gdb`, you can use commands like:
      ```gdb
      run
      break main
      ```
+ **`grep <pattern> <file>`**: Search for a specific pattern within a file.
    - Example:
      ```bash
      grep "password" secrets.txt
      ```
    - This command searches for the word "password" within the file `secrets.txt` and displays all matching lines.

+ **`feh <file>`**: Open an image file using the feh image viewer.
    - Example:
      ```bash
      feh image.png
      ```
    - This command will open the image `image.png` using the `feh` image viewer, which is often used in CTFs for viewing images quickly.

+ **`zbarimg <file>`**: Scan and decode barcodes or QR codes from an image file.
    - Example:
      ```bash
      zbarimg qr_code.png
      ```
    - This command scans the image `qr_code.png` for barcodes or QR codes and prints the decoded content to the terminal.


# Guide to Loops in the Linux Command Line

Loops in the Linux command line are powerful tools that allow you to automate repetitive tasks. This guide will cover the basics of `for` loops, including syntax and examples.

## Basic Syntax of a `for` Loop

The basic syntax for a `for` loop in the Linux shell is as follows:

```bash
for VARIABLE in LIST
do
    COMMANDS
done
``` 

-   **VARIABLE**: This is a placeholder that takes the value of each element in the list, one at a time.
-   **LIST**: A sequence of values that the loop will iterate over.
-   **COMMANDS**: One or more commands that are executed for each value in the list.

## Loop with `seq` Command

One common use case is iterating over a sequence of numbers. The `seq` command generates a sequence of numbers. Here’s an example:

```bash
`for i in $(seq -w 001 999)
do
    echo "Hello World $i"
done` 
```
-   `$(seq -w 001 999)`: Generates a sequence of numbers from 001 to 999.
-   `for i in $(seq -w 001 999)`: The loop assigns each number in the sequence to the variable `i` and iterates through them.
-   `echo "Hello World $i"`: Prints "Hello World" followed by the current number.

**Output**:

When you run this script, it will output:

```output
Hello World 001
Hello World 002
Hello World 003
...
Hello World 999 
```

## Loop with `seq` Command without `-w`:
The `-w` option in the `seq` command in Linux ensures that all output numbers have the same width by padding them with leading zeros, if necessary. This is particularly useful when generating sequences with numbers that need to be aligned or have a consistent format.

```bash
`seq 1 10` 
```
**Output:**

```output
1
2
3
4
5
6
7
8
9
10
```
## Loop with `seq` Command with `-w`:

```bash
`seq -w 1 10` 
```
**Output:**
```output
01
02
03
04
05
06
07
08
09
10
```
In the second example, `-w` ensures that all numbers have two digits by padding with zeros. If the sequence was longer (e.g., up to 100), it would pad the numbers with two zeros for single-digit numbers and one zero for two-digit numbers, ensuring that all numbers are three characters long.

## Looping Over a List of Files

```bash
`for file in *.txt
do
    echo "Processing $file"
done` 
```
## Looping with a Step Value

```bash
`for i in $(seq 0 2 10)
do
    echo "Number: $i"
done` 
```
This loop will output:

```output
Number: 0
Number: 2
Number: 4
Number: 6
Number: 8
Number: 10
```
