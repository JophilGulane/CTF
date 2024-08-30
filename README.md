# Useful CTF Tools and Command-line Tips
## Tools:
### Operating System
- Kali WSL
- Win KeX
### How To Install WSL
- Install WSL Tutorial [https://learn.microsoft.com/en-us/windows/wsl/install]
## Basic Kali Linux Command-line Tips
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

