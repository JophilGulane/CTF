## Important Links
+ [CTF Write-Ups](https://ctftime.org/writeups)
+ [p0isonp4wn - Hack4Gov 2019 CTF Writeups](https://james-mercado-work.medium.com/p0isonp4wn-hack4gov-2019-ctf-writeups-9c405f4d9e16)
+ [p0isonp4wn - Haxxor4.0 CTF Writeups](https://james-mercado-work.medium.com/p0isonp4wn-haxxor4-0-ctf-writeups-31ca7ce6570d)

## CATEGORIES

### Cryptography
Challenges involving the use of encryption and decryption techniques. Participants must break ciphers, decode messages, or otherwise manipulate cryptographic algorithms to retrieve hidden information or flags.

### Exploit
Challenges that require finding and exploiting vulnerabilities in systems, binaries, or applications. These could involve buffer overflows, shellcode execution, or other forms of software exploitation.

### Forensics
Tasks that involve analyzing digital evidence to uncover clues and retrieve flags. This might include examining file metadata, recovering deleted files, or analyzing memory dumps and network traffic.

### Investigation
Challenges focused on information gathering and analysis. Participants may need to investigate specific scenarios, follow digital trails, or gather intelligence to solve the puzzle.

### Miscellaneous
A catch-all category for challenges that don't fit neatly into other categories. These can include logic puzzles, steganography, or any other unique or unconventional problems.

### Programming
Tasks that require writing code to solve a specific problem. These challenges may involve algorithm development, automating tasks, or performing computations to find the flag.

### Reverse Engineering
Challenges that require understanding and deconstructing compiled code to find vulnerabilities or hidden information. This often involves analyzing binaries, assembly code, or disassembling software to retrieve the flag.

### Web
Challenges focused on web technologies and security. Participants might exploit vulnerabilities in websites or web applications, such as SQL injection, cross-site scripting (XSS), or authentication bypass techniques.

## How to Tackle Each CTF Category

### 1. Cryptography
Challenges involving encryption and decryption.

#### Steps:
1. **Identify the Cipher**: Look for common encryption types like Caesar, RSA, AES, or Base64. Patterns or known ciphertext structures can provide clues.
2. **Analyze the Data**: Look for repeating patterns, frequencies, and anomalies. Tools like frequency analysis can help.
3. **Use Cryptographic Tools**: Use tools like CyberChef, Hashcat, John the Ripper, or online decryptors to test common algorithms.
4. **Brute Force**: If the encryption type is known but not the key, try brute-forcing possible keys or using dictionary attacks.
5. **Understand Public Key Cryptography**: If RSA or other public-key cryptography is involved, check for common vulnerabilities like small exponent attacks or incorrect padding.
6. **Look for Weaknesses**: Check if there are known weaknesses or exploits for the cryptographic method used.

### 2. Exploit
Challenges focusing on finding and exploiting vulnerabilities.

#### Steps:
1. **Understand the Environment**: Identify the platform (e.g., Linux, Windows) and application type (e.g., web server, custom application).
2. **Examine Input Points**: Look for places where user input is accepted, such as forms, URL parameters, or files.
3. **Identify the Vulnerability**: Common vulnerabilities include buffer overflows, SQL injection, and command injection. Use automated scanners like `Nmap`, `Burp Suite`, or manual testing to identify them.
4. **Develop or Use an Exploit**: Write your exploit code, or find existing ones tailored to the vulnerability. Tools like `Metasploit` can automate this process.
5. **Test Exploit**: Run your exploit against the target, ensuring it is safe and will not cause unintended damage.
6. **Gain Access and Retrieve the Flag**: Once exploited, look for flags in common directories like `/root`, `/home`, or the webroot.

### 3. Forensics
Challenges based on analyzing digital evidence.

#### Steps:
1. **Identify File Types**: Start by determining the file type (using tools like `file` command in Linux). Even if the extension is misleading, this step helps identify the actual format.
2. **Analyze Metadata**: Extract metadata using tools like `ExifTool` to gather information about the file's origin, creation time, and editing history.
3. **Look for Hidden Data**: Use tools like `binwalk` and `foremost` to extract hidden files and data from the main file. Check for steganography using tools like `Stegsolve` or `zsteg`.
4. **Examine Strings**: Use the `strings` command to find readable text within binary files, which might contain clues or even the flag.
5. **Memory Analysis**: For memory dump files, use tools like `Volatility` to extract useful information, like running processes, network connections, or cached data.
6. **Network Forensics**: If provided with packet capture (PCAP) files, use tools like `Wireshark` to analyze network traffic, looking for suspicious communication or sensitive data transmission.

### 4. Investigation
Challenges that require gathering information from various sources.

#### Steps:
1. **Read the Challenge Description Carefully**: Understand what is being asked. Identify keywords or names that might be clues.
2. **Gather Information**: Use search engines, social media platforms, and other online tools to gather information. Google dorking can help find specific information.
3. **Correlate Data**: Piece together information from various sources. Look for connections between different pieces of data.
4. **Use OSINT Tools**: Tools like `Maltego`, `Recon-ng`, or `theHarvester` can automate information gathering from various sources.
5. **Validate Information**: Double-check the information you find to avoid red herrings. Make sure your conclusions are based on accurate data.

### 5. Miscellaneous
Unique challenges that don’t fit into other categories.

#### Steps:
1. **Understand the Problem**: Miscellaneous challenges could involve logic puzzles, trivia, or novel problems. Start by fully understanding what is being asked.
2. **Think Creatively**: These challenges often require out-of-the-box thinking. Don't limit yourself to conventional methods.
3. **Use Available Tools**: Depending on the challenge, use tools that might help solve the problem. It could range from text editors to specific scripts.
4. **Look for Patterns**: Often, miscellaneous challenges involve recognizing patterns or solving sequences.
5. **Collaborate**: Sometimes, discussing with team members can provide new perspectives and ideas.

### 6. Programming
Challenges that require coding to solve a problem.

#### Steps:
1. **Understand the Problem Statement**: Carefully read the problem description to understand the requirements and constraints.
2. **Plan Your Approach**: Think through the logic needed to solve the problem before coding. Break the problem into smaller, manageable parts.
3. **Choose the Right Language**: Select a programming language you are comfortable with and that suits the task (e.g., Python for scripting, C/C++ for performance).
4. **Write the Code**: Implement your logic in code. Use functions and modules to keep your code organized and reusable.
5. **Test Your Code**: Run tests with different inputs to ensure your solution works as expected. Debug any issues that arise.
6. **Optimize If Necessary**: If the solution is slow or resource-intensive, look for ways to optimize it, like improving algorithm efficiency.

### 7. Reverse Engineering
Challenges involving analyzing and understanding compiled code.

#### Steps:
1. **Identify the File Type**: Determine whether it's an executable, a library, or another binary type. Use the `file` command or similar tools.
2. **Disassemble the Code**: Use disassemblers like `Ghidra`, `IDA Pro`, or `Radare2` to convert the binary into assembly code.
3. **Analyze the Code Flow**: Identify the program’s entry points and understand the main flow of execution. Look for functions, loops, and conditional statements.
4. **Find Interesting Code Sections**: Look for functions or code sections related to user input, encryption, or data manipulation. These areas might contain vulnerabilities or clues.
5. **Debug the Program**: Use debuggers like `GDB` to run the program step-by-step, monitoring changes in memory and registers.
6. **Patch the Binary**: If necessary, modify the binary to change its behavior. This can help bypass security checks or uncover hidden functionality.

### 8. Web
Challenges related to web applications and their security.

#### Steps:
1. **Inspect the Web Application**: Start by manually browsing the application. Look at URLs, form fields, and error messages.
2. **Examine the Source Code**: Use the browser’s developer tools to inspect HTML, CSS, and JavaScript. Look for comments, hidden fields, or script files that may contain useful information.
3. **Test for Common Vulnerabilities**: Use tools like `Burp Suite`, `OWASP ZAP`, or `sqlmap` to test for vulnerabilities such as SQL injection, XSS, CSRF, and file inclusion.
4. **Look for Authentication and Session Issues**: Test login functionalities for weak passwords, session fixation, or cookie manipulation.
5. **Analyze HTTP Requests and Responses**: Use tools like `Burp Suite` to capture and modify HTTP traffic. Look for sensitive data or vulnerabilities in the way requests are handled.
6. **Exploit Vulnerabilities to Access the Flag**: Once a vulnerability is found, exploit it to gain unauthorized access or retrieve sensitive data that contains the flag.


# Important Commands

## Exploit

### 1. Nmap
- **Description**: Nmap (Network Mapper) is a powerful network scanning tool used to discover hosts and services on a computer network by sending packets and analyzing the responses.
- **Example/Use Case**: Nmap can be used to identify open ports, running services, and the operating systems of network devices. This information is crucial for vulnerability assessment and penetration testing.
- **Command**:
```bash
nmap -sV -O 192.168.1.1 
```

-   **Example Output**:

```plaintext
Starting Nmap 7.80 ( https://nmap.org ) at 2024-08-31 14:47
Nmap scan report for 192.168.1.1
Host is up (0.00050s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 7.6 (protocol 2.0)
80/tcp  open  http     Apache httpd 2.4.29 ((Ubuntu))
443/tcp open  ssl/http Apache httpd 2.4.29 ((Ubuntu))
MAC Address: 00:0C:29:5E:8B:4F (VMware, Inc.)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.9
```


### 2. Burp Suite

-   **Description**: Burp Suite is a comprehensive web vulnerability scanner and security testing tool used to find and exploit vulnerabilities in web applications.
-   **Example/Use Case**: Burp Suite is used to intercept and analyze web traffic, perform security scans, and identify vulnerabilities in web applications.
-   **Command**: Burp Suite is typically run through its graphical user interface (GUI), so commands are not usually issued via the command line. Instead, you start it with:

```bash   
`burpsuite` 
```

-   **Example Output**: The output is graphical and consists of various tabs such as Proxy, Target, Scanner, and Repeater for analyzing web traffic and vulnerabilities.

### 3. Metasploit

-   **Description**: Metasploit is a penetration testing framework that allows security professionals to find and exploit vulnerabilities in systems.
-   **Example/Use Case**: Metasploit can be used to exploit vulnerabilities in network services or applications. For instance, it can be used to exploit a known vulnerability in a service to gain access to a system.
-   **Command**:
```bash
`msfconsole` 
```




-   **Example Output**:

```plaintext
msf > use exploit/windows/smb/ms17_010_eternalblue
msf exploit(ms17_010_eternalblue) > set RHOSTS 192.168.1.100
msf exploit(ms17_010_eternalblue) > run
[*] Started reverse TCP handler on 192.168.1.1:4444
[*] 192.168.1.100:445 - Connecting to target...
[*] 192.168.1.100:445 - Exploit succeeded
```

## Forensics

### 1. file

-   **Description**: The `file` command is used to determine the type of a file by analyzing its contents rather than relying solely on the file extension.
-   **Example/Use Case**: To check the type of a file and identify its format, which can be useful for forensic analysis.
-   **Command**:

```bash
`file suspicious_image.png` 
```
-   **Example Output**:
``` plaintext
'suspicious_image.png: PNG image data, 800 x 600, 8-bit/color RGBA, non-interlaced'
```

### 2. ExifTool

-   **Description**: ExifTool is a command-line application for reading, writing, and editing meta-information in files, including image metadata.
-   **Example/Use Case**: Extracting metadata from images to find hidden information or track modifications.
-   **Command**:

```bash
`exiftool suspicious_image.png` 
```
-   **Example Output**:

```plaintext
`ExifTool Version Number         : 12.36
File Name                       : suspicious_image.png
File Size                       : 123456 bytes
Image Width                     : 800
Image Height                    : 600
Date/Time Original              : 2024:08:31 12:34:56` 
```

### 3. binwalk

-   **Description**: Binwalk is a tool for analyzing and extracting data from binary files. It is often used for firmware analysis.
-   **Example/Use Case**: To search for and extract embedded files or data from binary files.
-   **Command**:

```bash
`binwalk -e firmware.bin` 
```
-   **Example Output**:

```plaintext
`DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Embedded file: initramfs
123456        0x1E240         Embedded file: rootfs.img` 
```

### 4. foremost

-   **Description**: Foremost is a console program to recover files based on their headers, footers, and internal data structures.
-   **Example/Use Case**: To recover files from disk images or other data sources where file headers might be damaged or missing.
-   **Command**:

```bash

`foremost -i disk_image.img -o recovered_files` 
```
-   **Example Output**:

```plaintext
`Foremost v1.5.7 by Sumuri
Recovering files from disk_image.img
Processing: image/jpeg - found 15 files
Processing: image/png - found 10 files` 
```

### 5. Stegsolve

-   **Description**: Stegsolve is a graphical tool for analyzing and extracting hidden data from images.
-   **Example/Use Case**: To analyze an image for hidden messages or data through various steganographic techniques.
-   **Command**: Stegsolve is run as a Java application:

```bash
`java -jar stegsolve.jar` 
```
-   **Example Output**: The output is graphical, showing various analysis filters and options to reveal hidden information in images.

### 6. zsteg

-   **Description**: zsteg is a tool for detecting and extracting data from PNG and BMP images that use steganographic techniques.
-   **Example/Use Case**: To analyze images for hidden data using different color channels and bit layers.
-   **Command**:

```bash
`zsteg -a suspicious_image.png` 
```
-   **Example Output**:

```plaintext
`Detected LSB (Least Significant Bit) data in PNG image
Secret message: flag{hidden_in_image}` 
```

### 7. strings

-   **Description**: The `strings` command extracts and displays printable strings from binary files or data.
-   **Example/Use Case**: To find hidden text or other useful information within binary files or memory dumps.
-   **Command**:

```bash
`strings binary_file.bin` 
```
-   **Example Output**:

```plaintext
`This is a secret message.
Another useful string` 
```

### 8. Volatility

-   **Description**: Volatility is a framework for analyzing and extracting information from memory dumps, used in digital forensics.
-   **Example/Use Case**: To analyze a memory dump to extract information such as running processes, network connections, and malware.
-   **Command**:

```bash
`volatility -f memory_dump.raw --profile=Win7SP1x64 pslist` 
```
-   **Example Output**:

```plaintext
`Volatility Foundation Volatility Framework 2.6
Offset(V)          Name                    PID   PPID  Thds  Hnds  Sess  Wow64
------------------ ------------------------ ----- ----- ----- ----- ----- -----
0x81000            System                      4     0     70   340     0     0
0x9c00             smss.exe                  320     4      2     12     0     0` 
```

## Investigation

### 1. Maltego

-   **Description**: Maltego is an OSINT (Open Source Intelligence) and forensics application used to gather and analyze information about people, groups, websites, and other entities.
-   **Example/Use Case**: To map out relationships and gather data on a specific target by analyzing links between various entities.
-   **Command**: Maltego is run through its GUI, so commands are typically issued via its interface. Start it with:

```bash
`maltego` 
```
-   **Example Output**: The output is graphical, showing relationships and connections between different entities.

### 2. Recon-ng

-   **Description**: Recon-ng is a web reconnaissance framework with a powerful interface and modular design for gathering intelligence from various sources.
-   **Example/Use Case**: To perform reconnaissance on a target, such as gathering domain information, email addresses, and more.
-   **Command**:

```bash
`recon-ng` 
```
-   **Example Output**:

```plaintext
`[recon-ng][default] > use recon/hosts-domains/get_host
[recon-ng][default] > set SOURCE example.com
[recon-ng][default] > run
+-------------------------+---------------------------+
| Domain Name             | IP Address                |
+-------------------------+---------------------------+
| example.com             | 93.184.216.34             |
+-------------------------+---------------------------+` 
```

### 3. theHarvester

-   **Description**: theHarvester is a tool used to gather email addresses, subdomains, hosts, and other information from public sources for use in penetration testing and reconnaissance.
-   **Example/Use Case**: To collect information about email addresses and subdomains related to a specific domain.
-   **Command**:

```bash
`theHarvester -d example.com -b google` 
```
-   **Example Output**:

```plaintext
`Google search found 15 email addresses:
- contact@example.com
- support@example.com` 
```

## Reverse Engineering

### 1. file

-   **Description**: The `file` command determines the type of a file by analyzing its contents rather than relying on file extensions.
-   **Example/Use Case**: To identify the format of a binary file for reverse engineering.
-   **Command**:

```bash
`file binary_file.bin` 
```
-   **Example Output**:

```plaintext
`binary_file.bin: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=...` 
```

### 2. Ghidra

-   **Description**: Ghidra is a software reverse engineering (SRE) framework developed by the NSA that helps in analyzing binaries and decompiling code.
-   **Example/Use Case**: To disassemble and analyze executable files for vulnerabilities or understand their functionality.
-   **Command**: Ghidra is used through its GUI. Start it with:

```bash
`ghidraRun` 
```
-   **Example Output**: The output is graphical, showing the disassembled code and analysis tools.

### 3. IDA Pro

-   **Description**: IDA Pro (Interactive DisAssembler) is a disassembler and debugger used for reverse engineering binary files.
-   **Example/Use Case**: To decompile and analyze binaries to understand their functionality and discover vulnerabilities.
-   **Command**: IDA Pro is used through its GUI. Start it with:

```bash
`idaq` 
```
-   **Example Output**: The output is graphical, showing the disassembled code and analysis tools.

### 4. Radare2

-   **Description**: Radare2 is an open-source framework for reverse engineering and analyzing binaries.
-   **Example/Use Case**: To analyze binary files, debug, and disassemble code. It is useful for finding vulnerabilities and understanding binary behavior.
-   **Command**:

```bash
`radare2 binary_file.bin` 
```
-   **Example Output**:

```plaintext
`-- Welcome to radare2! --
[0x004005f0]> aaa
[0x004005f0]> pdf @ main` 
```

### 5. GDB

-   **Description**: GDB (GNU Debugger) is a debugger for programs written in C, C++, and other languages. It allows you to inspect and control the execution of programs.
-   **Example/Use Case**: To debug and analyze the execution of a binary file, step through code, and inspect variables.
-   **Command**:

```bash
`gdb binary_file` 
```
-   **Example Output**:

```plaintext
`(gdb) break main
Breakpoint 1 at 0x4011b6: file main.c, line 5.
(gdb) run
Starting program: /path/to/binary_file
Break in main at 0x4011b6: file main.c, line 5.` 
```

## Web

### 1. Burp Suite

-   **Description**: Burp Suite is a comprehensive web vulnerability scanner and security testing tool used to find and exploit vulnerabilities in web applications.
-   **Example/Use Case**: To intercept and analyze HTTP requests and responses, perform security scans, and identify vulnerabilities.
-   **Command**: Burp Suite is typically run through its GUI. Start it with:

```bash
`burpsuite` 
```
-   **Example Output**: The output is graphical, showing tabs for Proxy, Target, Scanner, Repeater, etc., for analyzing and manipulating web traffic.

### 2. OWASP ZAP

-   **Description**: OWASP ZAP (Zed Attack Proxy) is an open-source web application security scanner used to find vulnerabilities in web applications.
-   **Example/Use Case**: To scan web applications for security issues and vulnerabilities. It provides automated and manual testing capabilities.
-   **Command**: Start OWASP ZAP with:

```bash
`zap.sh` 
```
-   **Example Output**: The output is graphical, showing the various security findings and vulnerabilities discovered during the scan.

### 3. sqlmap

-   **Description**: sqlmap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection vulnerabilities.
-   **Example/Use Case**: To test a web application for SQL injection vulnerabilities and exploit them to gain access to the database.
-   **Command**:

```bash
`sqlmap -u "http://example.com/page.php?id=1" --dbs` 
```
-   **Example Output**:

```plaintext
`[*] Testing connection to the target URL
[*] Database: example_db
[*] Available databases:
[*]  - information_schema
[*]  - mysql
[*]  - example_db` 
```

### 4. Burp Suite

-   **Description**: Burp Suite (repeated for emphasis) is a comprehensive tool for web application security testing.
-   **Example/Use Case**: Used for intercepting and manipulating HTTP requests, scanning for vulnerabilities, and testing web application security.
-   **Command**: Again, start Burp Suite through its GUI with:

```bash
`burpsuite` 
```
-   **Example Output**: The output is graphical and includes features for intercepting HTTP requests, scanning for vulnerabilities, and more.

# John the Ripper Tutorial

**John the Ripper** is a fast password-cracking tool, primarily used to detect weak Unix passwords. It supports a wide range of encrypted password formats including several crypt password hash types commonly found on Unix-based systems.

## Table of Contents
1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Using Wordlists](#using-wordlists)
4. [Cracking RAR Files](#cracking-rar-files)
5. [Advanced Options](#advanced-options)
6. [Tips & Best Practices](#tips--best-practices)
7. [Conclusion](#conclusion)

## Installation

### On Linux
```bash
sudo apt-get update
sudo apt-get install john
```
### On macOS
```bash
brew install john
```
### On Windows
```plaintext
Download the latest John the Ripper from OpenWall.
Extract the files and add the run directory to your system’s PATH.
```
## Basic Usage
### Cracking a Unix Password Hash
1. Create a file with the password hash:

```plaintext
user:$1$abc123$XYZ987654321:1000:1000::/home/user:/bin/bash
```
### Run John against the file:
```bash
john --format=crypt hash_file.txt
```
### Check the cracked password:

```bash
john --show hash_file.txt
```
## Cracking a Simple Password Hash (e.g., MD5)
1. Create a file with the hash:

```plaintext
$1$xyz$abcd12345678
```
2. Run John:

```bash
john hash_file.txt
```
### View the password:

```bash
john --show hash_file.txt
```
## Using Wordlists
John the Ripper can use wordlists to try passwords.

### Using a Default Wordlist
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash_file.txt
```
### Using a Custom Wordlist
```bash
john --wordlist=/path/to/your/wordlist.txt hash_file.txt
```
### Incremental Mode (Brute-force)
John can also brute-force passwords by trying every possible combination of characters:

```bash
john --incremental hash_file.txt
```
## Cracking RAR Files
### Extracting Hash from RAR File
1. Install rar2john:

```bash
sudo apt-get install john
```
2. Extract the hash:

```bash
rar2john yourfile.rar > rar.hash
```
3. Run John against the RAR hash:

```bash
john --wordlist=/path/to/wordlist.txt rar.hash
```
4. View the cracked password:

```bash
john --show rar.hash
```
## Advanced Options
### Setting a Specific Charset
You can set a custom charset for John to use:

```bash
john --incremental --custom-charset=?lud hash_file.txt
```
+ ?l = lowercase letters
+ ?u = uppercase letters
+ ?d = digits
### Limiting Password Length
You can limit the maximum length of passwords John attempts:

```bash
john --max-length=8 hash_file.txt
```
### Resume Cracking
If you stop John during an operation, you can resume it later:

```bash
john --restore
```
## Tips & Best Practices
1. Use a Strong Wordlist: A good wordlist can significantly reduce the time required to crack a password.
2. Combine Wordlists: Use cat to combine multiple wordlists into one.
3. Regularly Update John: Ensure you have the latest version of John to benefit from new features and optimizations.
4. Monitor System Resources: Cracking passwords is CPU-intensive, so monitor your system to avoid overloading it.
5. Legal Use Only: Ensure you have permission to crack any passwords. Unauthorized access is illegal and unethical.
