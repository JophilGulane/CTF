## installs

## CLI Commands
- `wget` - downloads files using the command line
- `nautilus .` - open the file explorer in Ubuntu
- `eog` - Eye of GNOME, an image viewer
- `unzip` - unzip a ZIP file
- `file` - show the real file type
- `cat` - show the content of the file
- `nano` - open a file in a text editor
- `curl` - retrieve web pages
- `chmod` - change file permissions
- `nc` - Netcat, used to connect to another network
- `rev` - reverse the characters in a text
- `strings` - extract all strings from a file
- `whoami` - display the current username
- `tac` - reverse the order of lines in a file (opposite of `cat`)
- `tr -d <text>` - delete specified characters from the input
- `ceasar n` - decode a Caesar cipher with a shift of n
- `env` - display environment variables
- `hexedit` - open a file in a hex editor
- `ssh` - connect to a remote shell

  
### CLI Snippets

1. Search for text in a web page
```
curl "<url>" | grep -oE "picoCTF{.*}"
```

2. Runs a file
```
./file
```

3. Makes a file executable
```
chmod +x run
``` 

4. Decode base64
```
echo ""SGVsbG8gd29ybGQ=" | base64 -d
```

5. Decode rot13
```
echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}" | rot13
```

6. Netcat
```
nc <url> <port>
```

7. Search recursively
```
grep -R picoCTF{.*}
```

8. Connect to a shell using ssh
```
ssh <username>@<url>
```

## Python Snippets

1.  convert hex to ascii
```python
print(chr(0x41)) #A
```

2. convert the decimal 27(base 10) to binary(base 2)
```python
print(bin(27)) # 0b11011
print(bin(27)[2:]) # 11011
```

3. convert 0x3D(base 16) to decimal(base 10)
```python
print(int(hex(0x3D), 16)) # 61

### ==== OR ==== ####

print(str(0x3D)) # 61
```

4. Decode base64
```python
import base64

text = "SGVsbG8gd29ybGQ="
print(base64.b64decode(text)) #b'Hello world'
```

5. Decode rot13
```python
import codecs

text = "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
print(codecs.decode(text, encoding="rot13")) 
# The quick brown fox jumps over the lazy dog.
```


## Notes
### base64
- typically has a length that is a multiple of 4
- typically consisting of uppercase and lowercase letters (A-Z, a-z), digits (0-9), and two additional characters ('+' and '/')
- often ends with one or two '='
- Just decode it 
```python
import base64

text = "SGVsbG8gd29ybGQ="
print(base64.b64decode(text)) #b'Hello world'
```


### SQL injection
```
' OR '1' = '1' --
```

### Robots.txt
```
<url>/robot.txt # is a file that give instructions to web robots like google bot
```

##### look these up:
- vignere cipher from Blaise
- grep **-oE** [command]
- johntheripper [tool] - brute force password **
- rockyour - dictionary password attacker
- editthiscookie [extension] **
- foremost [command] **
- locate stegs [command]
- java [command]
- stegsolve [tool] **
- zsteg [command] **
- wireshark [tool]
- quipqiup [tool] - substitution cypher
- xxd [command]
- sql injection [tool]
- hopper disassembler [tool]
- gdb peda [tool]
- ltrace [command]

##### check if these are built-in libraries:
- base64
- codecs
- requests

