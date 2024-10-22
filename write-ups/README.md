 ## Important Links
+ [CTF Write-Ups](https://ctftime.org/writeups)
+ [p0isonp4wn - Hack4Gov 2019 CTF Writeups](https://james-mercado-work.medium.com/p0isonp4wn-hack4gov-2019-ctf-writeups-9c405f4d9e16)
+ [p0isonp4wn - Haxxor4.0 CTF Writeups](https://james-mercado-work.medium.com/p0isonp4wn-haxxor4-0-ctf-writeups-31ca7ce6570d)
+ [John Hammond's Repo] (https://github.com/JohnHammond/ctf-katana)

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

### INSPECTION STEPS YOU CAN TAKE

**CTRL+U/Inspect**

**Login related**
	Inspect then check css, javascript, php, or javascript embedded pages
	Navigate application<cookies<edit value to true
**Cookies**
	Navigate to `inspect<application<cookies<edit value`
 
**Javascript**
If given javascript code try bookmarking the website then edit the bookmark putting the javascript code as the URL

**Navigation**
Append on given link  `/robots.txt`
Append on given link `/.DS_Store`
A .DS_Store, short for Desktop Services Store, is an invisible file on the macOS operating system that gets automatically created anytime you look into a folder with ‘Finder.’ This file will then follow the folder everywhere it goes, including when archived, like in ‘ZIP.’


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

###### common commands for forensics
1. `file fileName`
2. `Exiftool fileName`
3. `zsteg imageName`
4. `unzip fileName`
5. `unrar fileName`
6. `Hexedit filename`
7. `Hexeditor (e.g Ghex) and CTRL F`
8. `binwalk -e  fileName`
9. `7z x [to be extracted file]`
10. `strings fileName | grep -i  keyword`

#### if encountered with directory array/list
      **example** given directory 001 - 999 
      `for i in $(seq -w 001 999) ; do cat $i/$i; done | grep H4G`



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
1. Extract the hash:

```bash
rar2john yourfile.rar > rar.hash
```
2. Run John against the RAR hash:

```bash
john --wordlist=/path/to/wordlist.txt rar.hash
```
3. View the cracked password:

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


# DCODE CIPHER IDENTIFIER

**DCODE CIPHER IDENTIFIER** is a computer tool designed to recognize encryption/encoding from a text message. The detector performs cryptanalysis, examines various features of the text, such as letter distribution, character repetition, word length, etc. to determine the type of encryption and guide users to the right tools based on the type of code or encryption identified.

## link: https://www.dcode.fr/cipher-identifier


# Sonic visualiser 

## Usage:


-   **Analyze Hidden Messages**: Investigators can use it to uncover hidden messages in audio files, such as those embedded in spectrograms, often seen in steganography.
-   **Identify Audio Manipulation**: It helps in detecting tampering or editing within audio recordings by examining inconsistencies in waveforms or spectrograms.
-   **Speaker Identification**: The tool can aid in voice analysis, potentially helping to identify speakers in a forensic investigation.
-   **Content Authentication**: By analyzing the spectral content, investigators can determine whether an audio file has been altered or manipulated.
-   **Transcription Assistance**: The visualization tools can assist in transcribing difficult-to-hear audio by isolating specific frequencies or components.

### On Linux

```bash   
`sudo apt-get install sonic-visualiser` 
```

# Symlinks
symlinks (ln)
If there is a file like flag.txt that we have no permission to access (even with chmod) and there's a file for example named banner, we can link that banner oso that when it runs, it is redirected to the flag.txt

ex. 
remove the banner file first
$ rm banner
locate the flag.txt
make the ln file
$ln -s /<location>/flag.txt banner
exit out the program and enter again
it should print the flag.txt instead of the banner

# WIRESHARK  NAVIGATION 

## Basic Navigation

### Packet List Pane:
	Displays all captured packets. Each row represents a packet, showing details like timestamp, source/destination IP, protocol, and info.
### Packet Details Pane:
	Provides detailed information about the selected packet. This is where you can drill down into the protocol layers (Ethernet, IP, TCP, HTTP, DNS, etc.).
### Packet Bytes Pane: 
	Shows the raw data of the packet in both hexadecimal and ASCII format. Useful for inspecting data within packets.

## Filters
Display Filters: Use these to filter packets based on specific criteria. Some common filters include:

- `http` : Filters for HTTP traffic.
- `dns` : Filters for DNS traffic.
- `tcp.port == 80 `: Filters for packets on port 80 (HTTP).
- `ip.addr == 192.168.1.1`: Filters packets involving a specific IP address.
- `frame contains "flag"`: Filters packets containing the word "flag".
- `Follow TCP/UDP Stream`: `Right-click` on a packet, then select `“Follow” -> “TCP Stream” `or `“UDP Stream”` to see the full conversation between a client and server. This can reveal flags embedded in communications.


## Inspecting Protocols
- `HTTP` : Look for GET and POST requests. Often flags can be hidden in URLs, headers, or responses.
- `DNS` : Investigate queries and responses. Sometimes flags are encoded in domain names or response data.
- `FTP/SMTP/IMAP` : If these protocols are present, check for transferred files or emails which may contain flags.
- `ICMP` : Occasionally, flags are hidden in ICMP packets (like ping requests/replies).




## Search and Find

- **Find Packet** : Use **Ctrl + F** to search for specific strings, like **"flag"**, within the packet list or details.
- **String Search** : In the `“Find Packet”` window, switch to `“String”` search, then choose to search in packet bytes, packet details, or packet list.

## Reassembling Data

- **Reassemble TCP Streams** : Sometimes data is split across multiple packets. Use the “Follow TCP Stream” feature to reassemble this data.
- **Export Objects**: If you see `HTTP, SMB, or other protocols` that can transfer files, you can export these objects (e.g., files, images) from the capture via `File -> Export Objects`.

## Analyzing Payloads

**Hex/ASCII View**: In the `Packet Bytes Pane`, you can see the `raw `payload. Flags are often hidden in` ASCII data or as hex-encoded strings`.
- **Decode As**: If you suspect that a certain protocol isn't being decoded correctly, right-click on a packet and choose `"Decode As"` to manually set the protocol.

## Statistics and Summaries

- **Protocol Hierarchy**: `Statistics -> Protocol Hierarchy` shows a breakdown of protocols in the capture, helping you quickly identify which protocols are in use.
-  **Conversations**: `Statistics -> Conversations` displays communication sessions between IPs. This is useful to identify suspicious or significant exchanges.
- **Endpoints**: `Statistics -> Endpoints` gives a list of all IPs, MAC addresses, etc., that have communicated.

## Time and Sequence Analysis

- **Time Shift**: If timestamps are important, you can adjust them via `Edit -> Time Shift` to sync them with other data sources.
- **TCP Stream Graphs**: `Statistics -> TCP Stream Graphs` can visualize data flows, helping spot anomalies.

## Decryption
- **SSL/TLS Decryption**: If you have access to the private key, Wireshark can decrypt SSL/TLS traffic, revealing the plaintext data.

## Exporting Data
- Export Packets: `Use File -> Export Specified Packets` to save only the relevant packets.
- Export As CSV/JSON: You can export packet data in different formats for further analysis using` File -> Export Packet Dissections`.

## Command Line (tshark)
- Automate Searches: Use tshark with filters and redirections in command line to automate searching and extraction of potential flags.
- Extract Specific Data: Use `fields with -T fields -e field_name` to extract specific parts of packet data.

# Example filtering suspicious redundant conversation request on wireshark

`tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response | grep local | awk '{print $12}' | sed -e 's/\..*//'`
`tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response | grep local | awk '{print $12}' | sed -e 's/\..*//'`

### command exaplanation breakdown

- `tshark -nr shark2.pcapng -Y 'dns'`: Reads the shark2.pcapng file and filters to display only DNS-related packets.

- `grep -v '8.8.8.8'`: Excludes any lines that contain the IP address `8.8.8.8`, which is commonly used by Google's public DNS servers.

- `grep -v response`: Excludes any lines that contain the word `"response,"` focusing on `DNS` queries.

- `grep local`: Filters lines that contain the word `"local,"` likely targeting .local domains or similar.

- `awk '{print $12}'`: Extracts the 12th field from each line. This field might represent the DNS query name or another relevant piece of data, depending on the packet structure.

- `sed -e 's/\..*//'`: Removes everything after the first dot (.) in the `12th field`, leaving only the initial part of the domain or name.



# Using ssldump to Decode/Decrypt SSL/TLS Packets 
(crdts:https://zomry1.github.io/webnet0/)

- decrypting TLS stream with  provided pcap and KEY
- `ssldump -r capture.pcap -k picopico.key -d`

- Capturing the flag directly
- `ssldump -r capture.pcap -k picopico.key -d | grep -C 5 pico`


# How to Reconstruct a QR Code from 9 Pieces
### Step 1: Install ImageMagick
First, you need to install ImageMagick, a powerful image manipulation tool that includes the convert command.

For Ubuntu/Debian-based systems:
```bash
sudo apt-get install imagemagick
```

### Step 2: Prepare Your QR Code Pieces
Ensure that your 9 QR code pieces are named consistently and placed in the same directory. For example, name them as follows:

+ qr_1.png (top-left)
+ qr_2.png (top-center)
+ qr_3.png (top-right)
+ qr_4.png (middle-left)
+ qr_5.png (middle-center)
+ qr_6.png (middle-right)
+ qr_7.png (bottom-left)
+ qr_8.png (bottom-center)
+ qr_9.png (bottom-right)

Ensure that each piece aligns correctly when combined.

### Step 3: Reconstruct the QR Code in One Command
You can combine the 9 pieces into a single QR code using the following one-liner command:

```bash
convert \( +append qr_1.png qr_2.png qr_3.png \) \( +append qr_4.png qr_5.png qr_6.png \) \( +append qr_7.png qr_8.png qr_9.png \) -append qr_combined.png
```
#### Explanation of the Command:
1. \( +append qr_1.png qr_2.png qr_3.png \): This merges the top row (1st, 2nd, 3rd pieces) horizontally.
2. \( +append qr_4.png qr_5.png qr_6.png \): This merges the middle row (4th, 5th, 6th pieces) horizontally.
3. \( +append qr_7.png qr_8.png qr_9.png \): This merges the bottom row (7th, 8th, 9th pieces) horizontally.
+ -append: This stacks the three rows vertically to form the complete QR code.
+ qr_combined.png: This is the output file where the combined image will be saved.


## Basic Use of Nmap
Nmap (Network Mapper) is a powerful open-source tool used for network exploration, security auditing, and network discovery. This tutorial will guide you through the basic use of Nmap to help you get started with network scanning.

### Step 1: Installing Nmap
For Ubuntu/Debian-based systems:
```bash
sudo apt-get install nmap
```

### Step 2: Basic Nmap Commands
Here are some basic Nmap commands to help you get started:

#### 1. Scanning a Single IP Address
To scan a single IP address, use the following command:

```bash
nmap 192.168.1.1
```
This command will perform a basic scan of the target IP (192.168.1.1) and provide information on the open ports and services running on that IP.

#### 2. Scanning a Range of IP Addresses
You can also scan a range of IP addresses using Nmap:

```bash
nmap 192.168.1.1-254
```
This command will scan all IP addresses from 192.168.1.1 to 192.168.1.254 within the network.

#### 3. Scanning a Specific Port
To scan a specific port, use the -p option followed by the port number:

```bash
nmap -p 80 192.168.1.1
```
This command scans port 80 (HTTP) on the target IP (192.168.1.1).

#### 4. Scanning Multiple Ports
You can scan multiple ports by specifying them with a comma:

```bash
nmap -p 22,80,443 192.168.1.1
```
This command scans ports 22 (SSH), 80 (HTTP), and 443 (HTTPS) on the target IP.

#### 5. Performing a Quick Scan
A quick scan focuses on the 100 most common ports:

```bash
nmap -F 192.168.1.1
```
The -F option tells Nmap to perform a fast scan.

#### 6. Service Version Detection
To identify the versions of services running on open ports, use the -sV option:

```bash
nmap -sV 192.168.1.1
```
This command attempts to determine the version of the services running on the open ports of the target IP.

#### 7. Operating System Detection
Nmap can also detect the operating system of the target by using the -O option:

```bash
sudo nmap -O 192.168.1.1
```
This command attempts to determine the target's operating system. Note that OS detection requires root privileges, so you may need to use sudo.

#### 8. Scanning a Host to Determine if it is Up
To check if a host is up or reachable, you can use:

```bash
nmap -sn 192.168.1.1
```
The -sn option tells Nmap to only perform a ping scan, which checks if the host is online without doing a full port scan.

#### 9. Saving Scan Results to a File
You can save the results of an Nmap scan to a file using the -o options:

```bash
nmap -oN scan_results.txt 192.168.1.1
```
This saves the output in a normal format to scan_results.txt.

##### For XML format:

```bash
nmap -oX scan_results.xml 192.168.1.1
```
##### For a grepable format:

```bash
nmap -oG scan_results.grep 192.168.1.1
```
#### 10. Performing a Verbose Scan
To get more detailed information about the scanning process, use the -v option:

```bash
nmap -v 192.168.1.1
```
The -v option increases verbosity, showing more detailed output.

### Step 3: Combining Options
Nmap allows you to combine multiple options to perform more complex scans. For example, to perform a service version detection scan with OS detection and save the results to a file, you can use:

```bash
sudo nmap -sV -O -oN detailed_scan.txt 192.168.1.1
```

# Important Scripts 
This command combines service version detection, OS detection, and saves the output to detailed_scan.txt.

# Hashcat

To use Hashcat for cracking passwords on ZIP, RAR, or other file types, you'll need to follow these steps. Hashcat requires the hash of the password you want to crack, so the first step is to extract the hash from the file.

## 1. Extract the Hash from the File
### For ZIP files:

You can use a tool like zip2john from the John the Ripper suite to extract the hash.
Command:
```bash
zip2john encrypted.zip > zip_hash.txt
```
This will generate a hash file zip_hash.txt containing the hash you can use with Hashcat.
### For RAR files:

Similarly, you can use rar2john to extract the hash.
Command:
```bash
rar2john encrypted.rar > rar_hash.txt
```
This will generate a hash file rar_hash.txt.
### For 7z (7-Zip) files:

You can use a tool like 7z2hashcat to extract the hash.
Command:
```bash
7z2hashcat.pl encrypted.7z > 7z_hash.txt
```
This will generate a hash file 7z_hash.txt.
## 2. Identify the Correct Hash Mode
Hashcat requires you to specify the hash type using a specific mode identifier. Here are some common modes for file types:

### ZIP: 
For ZIP: Use mode 13600.
### RAR:
For RAR3: Use mode 12500.
For RAR5: Use mode 13000.
7z: Use mode 11600.
## 3. Run Hashcat with the Extracted Hash
With the hash file ready, you can now use Hashcat to attempt to crack the password.

### Example Command:
```bash
hashcat -m [hash_mode] -a 0 hash_file.txt wordlist.txt
Replace [hash_mode] with the appropriate number from the list above (e.g., 13600 for ZIP).
Replace hash_file.txt with the path to your hash file (e.g., zip_hash.txt).
Replace wordlist.txt with the path to your wordlist file (e.g., rockyou.txt).
```
### Example for a ZIP File:
```bash
hashcat -m 13600 -a 0 zip_hash.txt /path/to/wordlist.txt
```
## 4. Monitor the Cracking Process
Hashcat will now attempt to crack the password using the provided wordlist. You can monitor the progress in the terminal, and if successful, the cracked password will be displayed.

## 5. Additional Options
You can use a brute-force attack by changing the attack mode to -a 3.
You can specify rules, GPU options, or other advanced features depending on your hardware and requirements.
## 6. Recovering the Password
If Hashcat successfully cracks the password, it will display it in the output, and you can use it to unlock the file.
