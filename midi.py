import mido
import pygame
import sys


def list_notes_from_midi(file_path):
    midi = mido.MidiFile(file_path)
    note_dict = {}
    current_instruments = {}

    for track in midi.tracks:
        absolute_time = 0
        for msg in track:
            absolute_time += mido.tick2second(msg.time, midi.ticks_per_beat, mido.bpm2tempo(187))  # Assuming 170 BPM
            if msg.type == 'program_change':
                current_instruments[msg.channel] = msg.program
            if msg.type == 'note_on' and msg.velocity > 0:
                note_name = msg.note
                instrument = current_instruments.get(msg.channel, 0)  # Default to instrument 0 if not set
                if note_name not in note_dict:
                    note_dict[note_name] = {'name': note_name, 'start_times': [], 'velocities': [], 'instruments': [],
                                            'durations': []}
                note_dict[note_name]['start_times'].append(absolute_time)
                note_dict[note_name]['velocities'].append(msg.velocity)
                note_dict[note_name]['instruments'].append(instrument)

            if msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                note_name = msg.note
                instrument = current_instruments.get(msg.channel, 0)  # Default to instrument 0 if not set
                if note_name not in note_dict:
                    note_dict[note_name] = {'name': note_name, 'start_times': [], 'velocities': [], 'instruments': [],
                                            'durations': []}
                note_dict[note_name]['start_times'].append(absolute_time)
                note_dict[note_name]['velocities'].append(0)
                note_dict[note_name]['instruments'].append(instrument)

    return note_dict
