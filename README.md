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
1. **`chmod +x <filename>`**: Change file permissions to make it executable.
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
