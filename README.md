# Shoe-Lace Cipher Algorithm
An Entry for the Boot Dev Hackathon

Introduction

Shoe lace cipher:
Objective - Using the shoe lacing pattern to create a symmetric cipher, using lacing techniques, digital encoding, and alphabets.

This repo allows you to cipher texts using an algorithm derived from traditional shoe lacing methods. For the purpose of simplicity, we’d be focusing on three lacing patterns respectively:

- Criss cross

![](https://github.com/NBGtega/shoelace-cipher/tree/assets/Criss-cross.gif)

- Army

![](https://github.com/NBGtega/shoelace-cipher/tree/assets/Army.gif)

- Straight european

![](https://github.com/NBGtega/shoelace-cipher/tree/assets/straight_european.gif)

Lacing Technique Rules:
All letters are uppercase ASCII letters
Letters are placed in form of rows mapped side by side to their corresponding odds and evens index A-B,C-D… Y-Z forming a 13th row matrix.
The letters on the left sides are considered odds (letter % 2 != 0) while letters on the right are considered evens (letter % 2 ==0)

- [Usage](#Usage)
- [Contributors](#Contributors)

# Usage
1. Clone the repo with: `git clone <put clone url here>`
2. CD to the repo name: `cd repo-name`
3. Use: `python3 main.py -m [message|required] -e [algorithm method| cc (criss-cross), se (straight European), a (army) | one is required]`

Help option is also available through `python3 main.py -h`

# Contributors

<a href="https://github.com/NBGtega/shoelace-cipher/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=NBGtega/shoelace-cipher" />
</a>
