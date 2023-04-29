# SHA-512
A simple script to hash file contents to SHA-512 in the form of a Key:value. This simple script led to a complete Account Takeover.
The web app was randomly omitting characters, so I had to find a way to recover those omitted characters in order to successfully identify and crack those hashes.

--usage--

```diff
! python3 filetosha.py filetohash.txt -o outputfile.txt
```
