# Understanding Endianness in PicoCTF

#Cybershef Solution
1. Copy The Word
2. Reverse The Word
3. Convert The Word into Hex
4. This Hex Should be The Small Endianness
5. Remove The Reverse Method
6. This Hex Should be The Big Endianness

Endianness refers to the order in which bytes are stored in memory. This concept is crucial when dealing with binary data and can affect how you interpret data during Capture The Flag (CTF) challenges. There are two primary types of endianness:

## 1. Little-Endian
In little-endian systems, the **least significant byte (LSB)** is stored first (at the lowest memory address), followed by the more significant bytes. For example, consider the hexadecimal number `0x12345678`:

- Memory Address 0x00: `0x78`
- Memory Address 0x01: `0x56`
- Memory Address 0x02: `0x34`
- Memory Address 0x03: `0x12`

In this format, the byte order is `78 56 34 12`.

## 2. Big-Endian
In big-endian systems, the **most significant byte (MSB)** is stored first (at the lowest memory address), followed by the less significant bytes. Using the same hexadecimal number `0x12345678`:

- Memory Address 0x00: `0x12`
- Memory Address 0x01: `0x34`
- Memory Address 0x02: `0x56`
- Memory Address 0x03: `0x78`

Here, the byte order is `12 34 56 78`.

## Why It Matters in CTF Challenges

Understanding endianness is crucial for tasks such as:

- **Reverse Engineering:** Interpreting binary files and data dumps correctly.
- **Exploits:** Crafting payloads that depend on specific byte orders.
- **Data Parsing:** Reading and writing data across different systems with varying endianness.

## Checking Endianness

You can check the endianness of your system with a simple C program:

```c
#include <stdio.h>

int main() {
    unsigned int x = 1;
    char *c = (char*)&x;
    if (*c) 
        printf("Little-endian\n");
    else 
        printf("Big-endian\n");
    return 0;
}
