#!/usr/bin/env python3
import random
import signal

def signal_handler(signal, frame):
    print("\nÀ bientôt !")
    exit()

signal.signal(signal.SIGINT, signal_handler)

gamme = [
	{
		"note": "do",
		"tone_up": 1,
		"tone_down": 0.5,
	},
	{
		"note": "ré",
		"tone_up": 1,
		"tone_down": 1,
	},
	{
		"note": "mi",
		"tone_up": 0.5,
		"tone_down": 1,
	},
	{
		"note": "fa",
		"tone_up": 1,
		"tone_down": 0.5,
	},
	{
		"note": "sol",
		"tone_up": 1,
		"tone_down": 1,
	},
	{
		"note": "la",
		"tone_up": 1,
		"tone_down": 1,
	},
	{
		"note": "si",
		"tone_up": 0.5,
		"tone_down": 1,
	}
]

intervals = [
	{
		"nb_notes": 2,
		"kind": "seconde",
		"name": "seconde mineure",
		"nb_tones": 0.5,
		"opposite": "septième majeure"
	},
	{
		"nb_notes": 2,
		"kind": "seconde",
		"name": "seconde majeure",
		"nb_tones": 1,
		"opposite": "septième mineure"
	},
	{
		"nb_notes": 3,
		"kind": "tierce",
		"name": "tierce mineure",
		"nb_tones": 1.5,
		"opposite": "sixte majeure"
	},
	{
		"nb_notes": 3,
		"kind": "tierce",
		"name": "tierce majeure",
		"nb_tones": 2,
		"opposite": "sixte mineure"
	},
	{
		"nb_notes": 4,
		"kind": "quarte",
		"name": "quarte juste",
		"nb_tones": 2.5,
		"opposite": "quinte juste"
	},
	{
		"nb_notes": 4,
		"kind": "quarte",
		"name": "quarte augmentée",
		"nb_tones": 3,
		"opposite": "quinte diminuée"
	},
	{
		"nb_notes": 5,
		"kind": "quinte",
		"name": "quinte diminuée",
		"nb_tones": 3,
		"opposite": "quarte augmentée"
	},
	{
		"nb_notes": 5,
		"kind": "quinte",
		"name": "quinte juste",
		"nb_tones": 3.5,
		"opposite": "quarte juste"
	},
	{
		"nb_notes": 6,
		"kind": "sixte",
		"name": "sixte mineure",
		"nb_tones": 4,
		"opposite": "tierce majeure"
	},
	{
		"nb_notes": 6,
		"kind": "sixte",
		"name": "sixte majeure",
		"nb_tones": 4.5,
		"opposite": "tiere mineure"
	},
	{
		"nb_notes": 7,
		"kind": "septième",
		"name": "septième mineure",
		"nb_tones": 5,
		"opposite": "seconde majeure"
	},
	{
		"nb_notes": 7,
		"kind": "septième",
		"name": "septième majeure",
		"nb_tones": 5.5,
		"opposite": "seconde mineure"
	# },
	# {
	# 	"nb_notes": 8,
	# 	"kind": "octave",
	# 	"name": "octave",
	# 	"nb_tones": 6,
	# 	"opposite": "octave"
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
	if origin == dest:
		return 6
	i_origin = find_note_index(origin)
	i_dest = find_note_index(dest)
	origin = gamme[i_origin]
	dest = gamme[i_dest]
	nb_tones = 0
	i = i_origin
	count = 0

	if up == True:
		while gamme[i]["note"] != dest["note"]:
			nb_tones += gamme[i]["tone_up"]
			i += 1
			count += 1
			if i == len(gamme):
				i = 0
		diff = {"nb_tones": nb_tones, "nb_notes": count + 1}
	else:
		while gamme[i]["note"] != dest["note"]:
			nb_tones += gamme[i]["tone_down"]
			i -= 1
			count += 1
			if i == -1:
				i = len(gamme) - 1
		diff = {"nb_tones": nb_tones, "nb_notes": count + 1}
	return diff

def find_up_note(origin, interval_kind):
	looked_intervals = list(filter(lambda interval: interval["kind"] == interval_kind, intervals))
	looked_nb_notes = 1
	nb_tones = 0
	i_origin = (find_note_index(origin))
	i = i_origin
	while looked_nb_notes < looked_intervals[0]["nb_notes"]:
		looked_nb_notes += 1
		nb_tones += gamme[i]["tone_up"]
		i += 1
		if i == nb_notes:
			i = 0
	interval = list(filter(lambda interval: interval["nb_tones"] == nb_tones, looked_intervals))[0]
	answer = " >> %-3s <<  %3s.•°%-3s est une %s montante (%1.1f tons)"% (gamme[i]["note"], origin, gamme[i]["note"], interval["name"], interval["nb_tones"])
	return {"origin": origin, "dest": gamme[i]["note"], "interval": interval, "answer": answer}

def find_down_note(origin, interval_kind):
	looked_intervals = list(filter(lambda interval: interval["kind"] == interval_kind, intervals))
	looked_nb_notes = 1
	nb_tones = 0
	i_origin = (find_note_index(origin))
	i = i_origin
	while looked_nb_notes < looked_intervals[0]["nb_notes"]:
		looked_nb_notes += 1
		nb_tones += gamme[i]["tone_down"]
		i -= 1
		if i == -1:
			i = 6
	interval = list(filter(lambda interval: interval["nb_tones"] == nb_tones, looked_intervals))[0]
	answer = " >> %-3s <<  %3s°•.%-3s est une %s descendante (%1.1f tons)" % (gamme[i]["note"], origin, gamme[i]["note"], interval["name"], interval["nb_tones"])
	return {"origin": origin, "dest": gamme[i]["note"], "interval": interval, "answer": answer}

def go_round_up(origin, interval_kind):
	r = []
	next = find_up_note(origin, interval_kind)
	while next["dest"] != origin:
		r.append(next)
		next = find_up_note(next["dest"], interval_kind)
	r.append(next)
	answer = "\n".join(map(lambda item: item["answer"], r))
	return {"answer": answer}

def go_round_down(origin, interval_kind):
	r = []
	next = find_down_note(origin, interval_kind)
	while next["dest"] != origin:
		r.append(next)
		next = find_down_note(next["dest"], interval_kind)
	r.append(next)
	answer = "\n".join(map(lambda item: item["answer"], r))
	return {"answer": answer}

def find_intervals(note1, note2):
	if note1 == note2:
		return {"answer": "%s <> %s est un octave"% (note1, note2)}
	r = []
	diff = find_nb_tones(note1, note2, True)
	interval1 = list(filter(lambda interval: interval["nb_notes"] == diff["nb_notes"] and interval["nb_tones"] == diff["nb_tones"], intervals))[0]

	diff = find_nb_tones(note1, note2, False)
	interval2 = list(filter(lambda interval: interval["nb_notes"] == diff["nb_notes"] and interval["nb_tones"] == diff["nb_tones"], intervals))[0]

	r.append("%3s.•°%-3s est une %s montante (%1.1f tons)"% (note1, note2, interval1["name"], interval1["nb_tones"]))
	r.append("%3s.•°%-3s est une %s montante (%1.1f tons)"% (note2, note1, interval2["name"], interval2["nb_tones"]))

	r.append("%3s°•.%-3s est une %s descendante (%1.1f tons)"% (note1, note2, interval2["name"], interval2["nb_tones"]))
	r.append("%3s°•.%-3s est une %s descendante (%1.1f tons)"% (note2, note1, interval1["name"], interval1["nb_tones"]))

	answer = "\n".join(map(lambda item: item, r))
	return {"answer": answer}



def main():
	note_list = list(map(lambda note: note["note"], gamme))
	interval_list = uniq(lambda item: item["kind"], intervals)
	quests = [
		{
			"type": "find_note",
			"question": "Quelle est la %s montante de %s ?",
			"function": find_up_note
		},
		{
			"type": "find_note",
			"question": "Quelle est la %s descendante de %s ?",
			"function": find_down_note
		},
		{
			"type": "round",
			"question": "Passez de %s en %s montante à partir de %s :",
			"function": go_round_up
		},
		{
			"type": "round",
			"question": "Passez de %s en %s descendante à partir de %s :",
			"function": go_round_down
		},
		{
			"type": "find_interval",
			"question": "Quels sont les intervalles possibles entre %s et %s ?",
			"function": find_intervals
		}
	]
	n_max = len(note_list) - 1
	i_max = len(interval_list) - 1
	p_max = len(quests) - 1
	input("Prêt ?")
	while 1:
		note = note_list[random.randint(0, n_max)]
		interval = interval_list[random.randint(0, i_max)]
		quest = quests[random.randint(0, p_max)]
		if quest["type"] == "find_note":
			question = quest["question"]% (interval, note)
			rep = quest["function"](note, interval)
		elif quest["type"] == "round":
			question = quest["question"]% (interval, interval, note)
			rep = quest["function"](note, interval)
		elif quest["type"] == "find_interval":
			note2 = note_list[random.randint(0, n_max)]
			question = quest["question"]% (note, note2)
			rep = quest["function"](note, note2)
		else:
			question = "?"
			rep = {"answer": "."}
		input(question)
		print(rep["answer"])
		input("=================================")

if __name__ == "__main__":
    main()