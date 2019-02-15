# Chirp Python Examples

A selection of Python examples using Chirp

## Setup

For all of the example apps you will need to

- Sign up at [developers.chirp.io](https://developers.chirp.io) for an app key, secret and config
- Follow setup instructions for the Python SDK at [developers.chirp.io](https://developers.chirp.io/docs/getting-started/python)

----

### Demo

A simple demo script that sends out a random chirp, and then continuously listens out for further chirps.
This is used as an introduction to the Python SDK.

----

### Messenger

Chirp Messenger uses your device's speaker and microphone to send and receive messages via audio.

To be compatible with Chirp Messenger on other platforms, e.g., [messenger.chirp.io](https://messenger.chirp.io),
the `16khz-mono` protocol must be used.

----

### Audio Tools

Scripts to read/write Chirp data to a `.wav` file.

----

### Chirp + Spotify

Build a streaming music player for Spotify using a Raspberry Pi, with a remote control that uses sound to transfer data.
Use with the accompanying [chrome extension](https://chrome.google.com/webstore/detail/chirp-spotify/iepiajcokedpnhcafddeahecjliijlla)

See the [instructable](https://www.instructables.com/id/Spotify-Music-Player-With-Chirp-Connect)

To be compatible with the [chrome extension](https://chrome.google.com/webstore/detail/chirp-spotify/iepiajcokedpnhcafddeahecjliijlla),
the `standard` protocol must be used.
