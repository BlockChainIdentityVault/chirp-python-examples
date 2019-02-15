# Audio Tools

Here are two scripts that allow you to read/write Chirp data to audio `.wav` files.

## Writing data

To write a unicode string of data to a `.wav` file.

    python3 write.py -u hello output.wav

To write a hexadecimal string of data to a `.wav` file.

    python3 write.py -x deadbeef output.wav

To view the scripts help text

    python3 write.py --help


## Reading data

To read string data from a Chirp `.wav` file.

    python3 read.py -u input.wav

To read a hexadecimal string of data from a `.wav` file.

    python3 read.py -x input.wav

To view the scripts help text

    python3 read.py --help
