# Chirp + Spotify

Build a streaming music player for Spotify using a Raspberry Pi, with a remote control that uses sound to transfer data.
Use with the accompanying [chrome extension](https://chrome.google.com/webstore/detail/chirp-spotify/iepiajcokedpnhcafddeahecjliijlla)

See the [instructable](https://www.instructables.com/id/Spotify-Music-Player-With-Chirp-Connect)

Please note that to be compatible with the chrome extension, the `standard` protocol
must be added to the [default] block in your `~/.chirprc` file.

To start listening

    python3 listener.py


## Usage

```bash
usage: listener.py [-h] [-i I]

Chirp | Spotify

optional arguments:
  -h, --help  show this help message and exit
  -i I        Input device index (optional)

Listens out for spotify codes and plays them with modipy-spotify
```
