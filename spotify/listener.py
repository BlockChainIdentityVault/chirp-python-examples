#!/usr/bin/python
"""
Listen out for spotify codes and play them with modipy-spotify.
"""
import argparse
import subprocess
import time

from chirpsdk import ChirpConnect, CallbackSet, CHIRP_CONNECT_STATE

# Short identifiers
USER_ID = '\xfa'
PLAYLIST_ID = '\xf9'
ARTIST_ID = '\xf8'
ALBUM_ID = '\xf7'
TRACK_ID = '\xf6'


def play(code):
    """ Play spotify code with modipy """
    print('Playing ' + code)
    subprocess.call(['mpc', 'clear'])
    subprocess.call(['mpc', 'add', code])
    subprocess.call(['mpc', 'play'])


def decode(payload):
    """ Decode the chirp payload into a spotify code """
    code = ''.join(chr(c) for c in payload)
    if code.startswith(ARTIST_ID):
        play('spotify:artist:{code}'.format(code=code[1:]))
    elif code.startswith(ALBUM_ID):
        play('spotify:album:{code}'.format(code=code[1:]))
    elif code.startswith(USER_ID):
        user, playlist = code[1:].split(PLAYLIST_ID)
        play('spotify:user:{user}:playlist:{code}'.format(
            user=user, code=playlist))
    elif code.startswith(TRACK_ID):
        play('spotify:track:{code}'.format(code=code[1:]))


class Callbacks(CallbackSet):

    def on_receiving(self, channel):
        print('Receiving data...')

    def on_received(self, payload, channel):
        if len(payload) == 23:
            decode(list(payload))


def main(input_device):

    # Initialise Connect SDK
    sdk = ChirpConnect()
    print(str(sdk))
    print(sdk.audio.query_devices())

    if sdk.protocol_name != 'standard':
        raise RuntimeError('Must use the standard protocol ' +
            'to be compatible with other Chirp Messenger apps.')

    # Configure audio
    sdk.audio.frame_size = 4096
    sdk.audio.input_device = input_device

    # Set callbacks and start SDK
    sdk.set_callbacks(Callbacks())
    sdk.start(send=False, receive=True)

    try:
        # Process audio streams
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print('Exiting')

    sdk.stop()
    sdk.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Chirp | Spotify',
        epilog='Listens out for spotify codes and plays them with modipy-spotify'
    )
    parser.add_argument('-i', type=int, default=None, help='Input device index (optional)')
    args = parser.parse_args()

    main(args.i)
