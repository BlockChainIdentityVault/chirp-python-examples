"""
read.py

Read a chirp payload from an audio file.
"""
import argparse
import os
import sys
import wave

from chirpsdk import ChirpConnect, CallbackSet, CHIRP_SDK_BUFFER_SIZE


class Callbacks(CallbackSet):

    def __init__(self, args):
        self.args = args

    def on_receiving(self, channel):
        print('Receiving data [ch{ch}]'.format(ch=channel))

    def on_received(self, payload, channel):
        if payload is None:
            print('Decode failed!')
        else:
            if self.args.unicode:
                print('Received: {data} [ch{ch}]'.format(
                    data=payload.decode('utf-8'), ch=channel))
            elif self.args.hex:
                print('Received: {data} [ch{ch}]'.format(
                    data=str(payload), ch=channel))
            else:
                print('Received: {data} [ch{ch}]'.format(
                    data=list(payload), ch=channel))


def main(args):
    # ------------------------------------------------------------------------
    # Initialise the Connect SDK.
    # ------------------------------------------------------------------------
    sdk = ChirpConnect()
    print(str(sdk))
    if args.network_config:
        sdk.set_config_from_network()

    print('Protocol: {protocol} [v{version}]'.format(
        protocol=sdk.protocol_name,
        version=sdk.protocol_version))

    # ------------------------------------------------------------------------
    # Disable audio playback.
    # ------------------------------------------------------------------------
    sdk.audio = None
    sdk.set_callbacks(Callbacks(args))
    sdk.start(send=False, receive=True)

    w = wave.open(args.infile, 'r')
    data = w.readframes(w.getnframes())
    sdk.input_sample_rate = w.getframerate()

    for f in range(0, len(data), CHIRP_SDK_BUFFER_SIZE):
        if w.getsampwidth() == 2:
            sdk.process_shorts_input(data[f: f + CHIRP_SDK_BUFFER_SIZE])
        elif w.getsampwidth() == 4:
            sdk.process_input(data[f: f + CHIRP_SDK_BUFFER_SIZE])

    sdk.stop()


if __name__ == '__main__':
    # ------------------------------------------------------------------------
    # Parse command-line arguments.
    # ------------------------------------------------------------------------
    parser = argparse.ArgumentParser(
        description='Chirp Connect Audio Reader',
        epilog='Reads a .wav file containing Chirp audio payloads, and outputs any payloads found'
    )
    parser.add_argument('infile', help='Input WAV file to read')
    parser.add_argument('-u', '--unicode', action='store_true', help='Parse payloads as unicode')
    parser.add_argument('-x', '--hex', action='store_true', help='Parse payloads as hexstrings')
    parser.add_argument('--network-config', action='store_true', help='Optionally download a config from the network')
    args = parser.parse_args()

    main(args)
