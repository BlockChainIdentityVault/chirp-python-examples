# Demo

This script sends out a random chirp, then continuously listens out for chirps.
It accepts a Chirp app key and secret as required parameters, you can retrieve
these from [developers.chirp.io](https://developers.chirp.io).

You can pass in a config file as an optional parameter with `-c <config_file`,
if one if not specified, the default configuration set in
[developers.chirp.io](https://developers.chirp.io) will be downloaded from the
network and used.

The script will print out the available audio i/o devices, and point to the
default audio devices. You may find that on some platforms you may find you need to
explicitly set the input/output device. Use the desired device index with the
`-i` and `-o` parameters accordingly to change devices.

There are also options to alter the block size and sample rate, however you
shouldn't need to use these.


## Usage

```bash
ChirpSDK Demo

positional arguments:
  key         Chirp application key
  secret      Chirp application secret

optional arguments:
  -h, --help  show this help message and exit
  -c C        Path to config file (optional)
  -i I        Input device index (optional)
  -o O        Output device index (optional)
  -b B        Block size (optional)
  -s S        Sample rate (optional)

Sends a random chirp payload, then continuously listens for chirps
```

