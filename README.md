# Password Strength Calculator

This script need for evaluations password strength. *(Rating from 1 to 10)*

#For which points
If your password contains:
* numbers - 1 point
* lower case - 1 point
* upper case - 1 point
* symbols - 2 point
* length more 7 - 1 point
* length more 9 - 1 point
* length more 11 - 1 point
* length more 13 - 1 point
* length more 15 - 1 point

```blacklist_passwords``` contains 1000 most common passwords.

**If your password is blacklisted or length less 6, the score will be 1.**

# How to use
For run script need ```password_strength.py``` and ```blacklist_passwords``` from this repository.

*Script for launch on Linux, Python 3.5:*
```bash
$ python3 password_strength.py
```
Running on Windows is similar.

*(Possibly requires call of 'python' executive instead of just 'python3'.)*

# Example
```bash
$ python3 password_strength.py
Enter password for evaluation: hello_world!
Password strength: 7/10
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
