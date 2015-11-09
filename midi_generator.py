#!/usr/bin/python
from markov import markov_chain
from mido import MidiFile, parse_all, merge_tracks, MetaMessage, parse


class midi_generator(markov_chain):
    
    def __init__(self, filename, level=1):
        midi = MidiFile(filename)
        track = merge_tracks(midi.tracks)
        self.metamessages = []
        byte_list = []
        for message in track:
            if not isinstance(message, MetaMessage):
                byte_list.extend(message.bytes())
            else:
                self.metamessages.append(message)
        super().__init__(byte_list, level)

    def generate_midi(self, filename, length=100, delay=96):
        output = MidiFile()
        byte_list = super().generate_obj_list(length)
        track = parse_all(byte_list)
        for message in track:
            message.time = delay
        output.tracks.append(self.metamessages)
        output.tracks.append(track)
        output.save(filename)


if __name__ == "__main__":
    test = midi_generator("midi/santa.mid", 10)
    test.generate_midi("output.mid", 90000, 40)
