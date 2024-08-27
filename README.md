# Useful CTF Tools and Command-line Tips
## Tools:
### Operating System
- Kali WSL
- Win KeX
## Basic Kali Linux Command-line Tips
### Run Win-KeX
- Inside of Kali WSL: kex --win -s
### Seamless Mode
- Inside of Kali WSL: kex --sl -s
### Shutdown WSL
- Inside of CMD: wsl --shutdown
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

2. **`./<filename>`**: Run the file.
   - Example:
     ```bash
     ./exploit.sh
     ```

3. **`file ./<filename>`**: View file contents or determine file type.
   - Example:
     ```bash
     file ./mystery_file
     ```
   - Output might be:
     ```
     mystery_file: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked
     ```

4. **`strings <filename>`**: Perform static analysis to extract readable strings from the file.
   - Example:
     ```bash
     strings mystery_file
     ```
   - Output might include:
     ```
     /bin/sh
     GLIBC_2.0
     ```
     
5. **`ltrace <filename>`**: Trace library calls made by a program.
   - Example:
     ```bash
     ltrace ./mystery_file
     ```
   - Output might show:
     ```
     __libc_start_main(0x4005ed, 1, 0x7ffdf1f37e18, 0x4006f0, 0x400770 <unfinished ...>
     ```

6. **`strace <filename>`**: Trace system calls and signals made by a program.
   - Example:
     ```bash
     strace ./mystery_file
     ```
   - Output might show:
     ```
     execve("./mystery_file", ["./mystery_file"], 0x7ffd41c0) = 0
     ```

7. **`xxd <filename>`**: Create a hexdump of a file, useful for analyzing binary data.
   - Example:
     ```bash
     xxd mystery_file
     ```
   - Output might include:
     ```
     00000000: 7f45 4c46 0201 0100 0000 0000 0000 0000  .ELF............
     ```

8. **`grep <pattern> <filename>`**: Search for a specific pattern within a file.
   - Example:
     ```bash
     grep "password" config.txt
     ```
   - Output might include:
     ```
     password=supersecretpassword
     ```

9. **`nc <hostname> <port>`**: Use Netcat to connect to a remote server, often for interacting with remote CTF challenges.
   - Example:
     ```bash
     nc example.com 12345
     ```

10. **`tar -xvf <filename>`**: Extract files from a tar archive.
    - Example:
      ```bash
      tar -xvf archive.tar
      ```

11. **`unzip <filename>`**: Extract files from a zip archive.
    - Example:
      ```bash
      unzip archive.zip
      ```

12. **`md5sum <filename>` / `sha256sum <filename>`**: Calculate and verify the hash of a file.
    - Example:
      ```bash
      md5sum mystery_file
      ```
    - Output might include:
      ```
      d41d8cd98f00b204e9800998ecf8427e  mystery_file
      ```

13. **`gdb <filename>`**: Start the GNU Debugger to analyze and debug binary files.
    - Example:
      ```bash
      gdb ./mystery_file
      ```
    - Within `gdb`, you can use commands like:
      ```gdb
      run
      break main
      ```

