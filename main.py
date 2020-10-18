#!/usr/bin/env python3
import random
import signal

def signal_handler(signal, frame):
    global interrupted
    interrupted = True
    print("\nÀ bientôt !")
    exit()

signal.signal(signal.SIGINT, signal_handler)
interrupted = False

gamme = [
	{
		"note": "do",
		"tone_up": 1,
		"tone_down": 0.5
	},
	{
		"note": "ré",
		"tone_up": 1,
		"tone_down": 1
	},
	{
		"note": "mi",
		"tone_up": 0.5,
		"tone_down": 1
	},
	{
		"note": "fa",
		"tone_up": 1,
		"tone_down": 0.5
	},
	{
		"note": "sol",
		"tone_up": 1,
		"tone_down": 1
	},
	{
		"note": "la",
		"tone_up": 1,
		"tone_down": 1
	},
	{
		"note": "si",
		"tone_up": 0.5,
		"tone_down": 1
	}
]

intervals = [
	{
		"nb_notes": 2,
		"kind": "seconde",
		"name": "seconde mineur",
		"nb_tones": 0.5
	},
	{
		"nb_notes": 2,
		"kind": "seconde",
		"name": "seconde majeur",
		"nb_tones": 1
	},
	{
		"nb_notes": 3,
		"kind": "tierce",
		"name": "tierce mineur",
		"nb_tones": 1.5
	},
	{
		"nb_notes": 3,
		"kind": "tierce",
		"name": "tierce mineur",
		"nb_tones": 2
	},
	{
		"nb_notes": 4,
		"kind": "quarte",
		"name": "quarte juste",
		"nb_tones": 2.5
	},
	{
		"nb_notes": 4,
		"kind": "quarte",
		"name": "quarte augmentée",
		"nb_tones": 3
	},
	{
		"nb_notes": 5,
		"kind": "quinte",
		"name": "quinte juste",
		"nb_tones": 3.5
	},
	{
		"nb_notes": 5,
		"kind": "quinte",
		"name": "quinte diminuée",
		"nb_tones": 3
	},
	{
		"nb_notes": 6,
		"kind": "sixte",
		"name": "sixte mineure",
		"nb_tones": 4
	},
	{
		"nb_notes": 6,
		"kind": "sixte",
		"name": "sixte majeure",
		"nb_tones": 4.5
	},
	{
		"nb_notes": 7,
		"kind": "septième",
		"name": "septième mineure",
		"nb_tones": 5
	},
	{
		"nb_notes": 7,
		"kind": "septième",
		"name": "septième majeure",
		"nb_tones": 5.5
	}
]

nb_notes = len(gamme)

def uniq(key, lst):
	s = set()
	r = []

	for i in lst:
		k = key(i)
		if k not in s:
			s.add(k)
			r.append(k)
	return r

def find_note_index(note):
	return [i for i,_ in enumerate(gamme) if _['note'] == note][0]

def find_correct_index(dest):
	if dest > nb_notes - 1:
		return dest - 7
	elif dest < 0:
		return dest + 7
	else:
		return dest

def find_nb_tones(origin, dest, up):
	nb_tones = 0
	if up == true :
		pass

def find_up_note(origin, interval_kind):
	looked_intervals = list(filter(lambda interval: interval["kind"] == interval_kind, intervals))
	looked_nb_notes = 1
	nb_tones = 0
	i_origin = (find_note_index(origin))
	i = i_origin
	while looked_nb_notes < looked_intervals[0]["nb_notes"] :
		looked_nb_notes = looked_nb_notes + 1
		nb_tones = nb_tones + gamme[i]["tone_up"]
		i = i + 1
		if i == nb_notes :
			i = 0
	# i_dest = i_origin + looked_intervals[0]["nb_notes"] - 1
	# i_dest = find_correct_index(i_dest)
	interval = list(filter(lambda interval: interval["nb_tones"] == nb_tones, looked_intervals))[0]
	print(" >> %s <<  %s.•°%s est une %s montante (%1.1f tons)"% (gamme[i]["note"], origin, gamme[i]["note"], interval["name"], interval["nb_tones"]))

def find_down_note(origin, interval_kind):
	looked_intervals = list(filter(lambda interval: interval["kind"] == interval_kind, intervals))
	looked_nb_notes = 1
	nb_tones = 0
	i_origin = (find_note_index(origin))
	i = i_origin
	while looked_nb_notes < looked_intervals[0]["nb_notes"] :
		looked_nb_notes = looked_nb_notes + 1
		nb_tones = nb_tones + gamme[i]["tone_down"]
		i = i - 1
		if i == -1 :
			i = 6
	# i_dest = i_origin - looked_intervals[0]["nb_notes"] + 1
	# i_dest = find_correct_index(i_dest)
	interval = list(filter(lambda interval: interval["nb_tones"] == nb_tones, looked_intervals))[0]
	print(" >> %s <<  %s°•.%s est une %s descendante (%1.1f tons)"% (gamme[i]["note"], origin, gamme[i]["note"], interval["name"], interval["nb_tones"]))

def find_interval(note1, note2):
	pass

def main():
	note_list = list(map(lambda note: note["note"], gamme))
	interval_list = uniq(lambda item: item["kind"], intervals)
	play = [
		{
			"question": "Quelle est la %s montante de %s ?",
			"function": find_up_note
		},
		{
			"question": "Quelle est la %s descendante de %s ?",
			"function": find_down_note
		}
	]
	n_max = len(note_list) - 1
	i_max = len(interval_list) - 1
	p_max = len(play) - 1
	input("Prêt ?")
	while 1:
		note = note_list[random.randint(0, n_max)]
		interval = interval_list[random.randint(0, i_max)]
		quest = play[random.randint(0, p_max)]
		input(quest["question"]% (interval, note))
		quest["function"](note, interval)
		input("=================================")

if __name__ == "__main__":
    main()