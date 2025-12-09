# Shoe-Lace Cipher Algorithm
An Entry for the Boot Dev Hackathon  

* [Introduction](#introduction)
* [Usage](#usage)
* [Contributors](#contributors)

# Introduction

Shoe lace cipher:  

**Objective**  
- Using the shoe lacing pattern to create a symmetric cipher, using lacing techniques, digital encoding, and alphabets.

**Encoding techniques**  
This repo allows you to cipher texts using an algorithm derived from traditional shoe lacing methods.  
For the purpose of simplicity, we’d be focusing on three lacing patterns respectively:

- Criss cross

![Criss Cross](https://raw.githubusercontent.com/NBGtega/shoelace-cipher/assets/Criss-cross.gif)

- Army

![Army](https://raw.githubusercontent.com/NBGtega/shoelace-cipher/assets/Criss-cross.gif)

- Straight european

![Straight-euro](https://raw.githubusercontent.com/NBGtega/shoelace-cipher/assets/Criss-cross.gif)

Lacing Technique Rules:
All letters are uppercase ASCII letters
Letters are placed in form of rows mapped side by side to their corresponding odds and evens index A-B,C-D… Y-Z forming a 13th row matrix.
The letters on the left sides are considered odds (letter % 2 != 0) while letters on the right are considered evens (letter % 2 ==0)


# Usage
1. Clone the repo with: `git clone https://github.com/NBGtega/shoelace-cipher.git`
2. cd to the repo name: `cd shoelace-cipher`
3. Example for criss-cross encryption:
   ```bash
   python3 main.py -m [your msg here] -e cc
   ```

Use help option for details: `python3 main.py -h`

# Contributors

<a href="https://github.com/NBGtega/shoelace-cipher/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=NBGtega/shoelace-cipher" />
</a>
