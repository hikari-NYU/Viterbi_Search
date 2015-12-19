import numpy
import nltk
import json

#Viterbi path selection by grid search
#@Input: words:list(string):words to be tagged; transit:dict:state transit map; emit:dict:word emit map
#@Output: path:list(tag):Tag sequence corresponding to the word sequence
def viterbi(words,transit,emit):
	states=[val for val in transit]
	#Adding start and end signs to the sentence
	matrix=numpy.array([[(0.0,0)]*(len(words)+2)]*len(states))
	#Initialization
	matrix[states.index('null'),0]=(1.0,-1)
	#Fill the transition table with the probability dictionaries
	pre=matrix[:,0]
	for i in range(len(words)):
		post=matrix[:,i+1]
		postWord=words[i]
		for j in range(len(states)):
			for k in range(len(states)):
				try:
					if pre[j][0]+transit[states[j]][states[k]]*emit[states[k]][postWord]>post[k][0]:
						post[k]=(pre[j][0]+transit[states[j]][states[k]]*emit[states[k]][postWord],j)
				except:
					#If no such transaction, pass
					pass
		matrix[:,i+1]=post
		pre=post
	#Attach the end node
	end=states.index('nil')
	for j in range(len(states)):
		try:
			if pre[j][0]+transit[states[j]]['nil']*1.0>matrix[end,-1][0]:
				matrix[end,-1]=(pre[j][0]+transit[states[j]]['nil']*1.0,j)
		except:
			pass
	#Generate the sequence of POS tag
	path=[]
	for i in range(len(words),0,-1):
		state=states[int(matrix[end,i+1][1])]
		end=matrix[end,i+1][1]
		path.append(state)
	path.reverse()
	return path

#Load the dictionaries built by the bigram HMM part
#@Input: transitPath:String:transit dict store path; emitPath:String:emit dict store path
#@Output: transit:dict:loaded transit dict; emit:dict:loaded emit dict
def loadDict(transitPath='',emitPath=''):
	if len(transitPath)<1 or len(emitPath)<1:
		return None
	with open(transitPath, 'r') as f:
		transit = json.load(f)
	with open(emitPath,'r') as f:
		emit=json.load(f)
	return (transit,emit)

def main():
	(transit,emit)=loadDict('transit.txt','emit.txt')
	sentence=raw_input('Please enter the sentence to tag:\n')
	words=nltk.word_tokenize(sentence.lower())
	print ' '.join(viterbi(words,transit,emit))

if __name__=="__main__":
	main()