# Chirp Messenger

This script allows you to send/receive messages to/from other Chirp Messenger apps.

Please note that to be compatible with other Chirp Messenger apps, the `16khz-mono` protocol
must be added to the [default] block in your `~/.chirprc` file.

To send a message

    python3 messenger.py hello


## Usage

```bash
usage: messenger.py [-h] [-v VOLUME] [-o O] [--network-config] message

Chirp Messenger

positional arguments:
  message               Text or emoji message to send

optional arguments:
  -h, --help            show this help message and exit
  -v VOLUME, --volume VOLUME
                        Volume
  -o O                  Output device index (optional)
  --network-config      Optionally download a config from the network

Send a message to other Chirp Messengers
```
