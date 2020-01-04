"""

Using a markov chain, 
generate similar passages

"""
import os,sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.markov.markov_chain import MarkovChain 

def main():
	if len(sys.argv) > 2:
		fp = sys.argv[1]
		seq_len = int(sys.argv[2])
	else:
		fp = "data/dna/IAI39.fasta"
		seq_len = 10

	with open(fp, "r") as f:
		header = f.readline()

		m = MarkovChain(f, split_re=r".{3}")
		m.save(jsonfile="mrkv.json")
		seq = m.generate(seq_len)
		print(seq)


if __name__ == '__main__':
	main()
