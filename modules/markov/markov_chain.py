"""

Building efficient markov db's for markov chain generators

"""
import pickle,json
import re
import random
import numpy as np

from collections import Counter

class MarkovChain():
	"""
	Markov, 
	general purpose markov chain generator

	"""

	def __init__(self, filehandle=None, split_re=r"\s+"):
		"""
			Split is the regex pattern to split on
			useful dna split is ".{3}"

		"""
		self.filehandle = filehandle
		self.split_re = split_re
		self.observations = {}
		self.num_observations = 0
		self.probabilities = {}
		if filehandle:
			self.run(filehandle)


	def run(self, filehandle):
		""" full run from a file, 
		will add to our observations
		"""
		self.read_file(filehandle)
		self.calc_prob()


	def read_file(self, filehandle):
		""" read a file, 
		for each line of file split using the global split_re
		maintain a data structure for occurences of each observation
		"""

		prev = ""
		for item in re.findall(self.split_re, filehandle.read()):
			self.add_observation(prev, item)
			prev = item
			
		#add a final empty observation
		self.add_observation(prev, "")


	def add_observation(self, prev, item):
		""" given an observation
		add it to our data structure
		"""

		if prev not in self.observations:
			self.observations[prev] = Counter()
			
		if item not in self.observations[prev]:
			self.observations[prev][item] = 1
		else:
			self.observations[prev][item] += 1


	def calc_prob(self):
		""" save encodings in efficient map format 
			(occurence is encoded in file format)
			key --> [(observed, probability),...]

			eg:
			ATC --> [(GAT, 0.2),(ATA, 0.8)]

			todo: refactor to build list of keys / probs
			keys: ["GAT", "ATA"]
			probs: [0.2,0.8]
		"""
		db = {}
		for k in self.observations:
			if not k in db:
				db[k] = {"keys":[],"probs":[]}
			total_obs = 0
			#count totoal observances
			for k2 in self.observations[k]:
				total_obs += self.observations[k][k2]
			#add probabilities
			for k2 in self.observations:
				prob = self.observations[k][k2] / total_obs #requires python3
				db[k]["keys"].append(k2)
				db[k]["probs"].append(prob)
		self.probabilities = db


	def save(self,output="mrkv.mrkvdb", jsonfile=None):
		""" save encodings to file (pickle)
		"""
		with open(output, "wb") as f:
			pickle.dump(self.probabilities, f)
		if jsonfile:
			with open(jsonfile, "w") as jf:
				json.dump(self.probabilities, jf, indent=4)

	def load(self, filepath="mrkv.mrkvdb"):
		""" Load encodings to local probabilities
		"""
		with open(output, "rb") as f:
			self.probabilities = pickle.load(f)

	def generate(self, length, start=None, join_c=""):
		""" generate a sequence of length provided
			len: int, the length of the sequence to generate
			state: None or str, this is the key to start the sequence with
		"""
		if not start:
			start = random.choice(list(self.probabilities.keys()))

		sequence = []
		prev = start
		for i in range(0,length):
			n = self.select_next(key=prev)
			sequence.append(n)
			prev = n
		return join_c.join(sequence)


	def select_next(self, key=None):
		if key == None:
			return ""
		p = self.probabilities[key]
		keys = p["keys"]
		probs = p["probs"]
		#print(keys, probs)
		return np.random.choice(keys, 1, p=probs)[0]


		

		

