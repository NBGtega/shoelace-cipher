# Shoe-Lace Cipher Algorithm
An Entry for the Boot Dev Hackathon

Introduction

Shoe lace cipher:
Objective - Using the shoe lacing pattern to create a symmetric cipher, using lacing techniques, digital encoding, and alphabets.

This repo allows you to cipher texts using an algorithm derived from traditional shoe lacing methods. For the purpose of simplicity, we’d be focusing on three lacing patterns respectively:

-Cross cross
-Army
-Straight European

Lacing Technique Rules:
All letters are uppercase ASCII letters
Letters are placed in form of rows mapped side by side to their corresponding odds and evens index A-B, C-D… Y-Z forming a 13th row matrix.
The letters on the left sides are considered odds (letter % 2 != 0) while letters on the right are considered evens (letter % 2 ==0)

- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Contributors](#Contributors)

# Features

# Installation

# Usage
1 - Use `python3 <filename> -m [message|required] -e [algorithm method| cc (criss-cross), se (straight European), a (army) | one is required]`
  1.1 -m: represents the message we want to cipher. Required.
  1.2 -e: represents the shoe-lacing pattern we are going to use to cipher the message. Options are: cc, se, a. One is required.

Help option is also available through `python3 <filename> -h`

# Contributors
