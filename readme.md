# Seedfinder

Given a NAND drive and a private file, this finds your SD seed.

This piggybacks off of Khangaroo's [very nice SD dumping guide](https://gist.github.com/khang06/84aabeac507fa99a676d22bb6120cea8)

## Usage:

1. Copy your private file to the same directory as the script
2. Use HacDiskMount to mount SYSTEM to your drive S
3. Run ``python3 ./seeder.py``
4. Profit

## Advanced usage:

```
usage: seeder.py [-h][--private PRIVATE] [--save SAVE]

optional arguments:
  -h, --help         show this help message and exit
  --private PRIVATE  Path to your sd:/Nintendo/contents/private file. Defaults
                     to ./private
  --save SAVE        Path to your SYSTEMNAND:/save/8000000000000043 file.
                     Defaults to S:/save/8000000000000043
```