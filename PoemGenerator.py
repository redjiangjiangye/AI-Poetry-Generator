import random

nouns = ["love", "hope", "sorrow", "ocean", "moonlight"] 
verbs = ["dance", "shine", "cry", "flow", "glisten"]
adjectives = ["gentle", "rolling", "silent", "breaking", "glimmering"]

def generate_poem():
  poem = ""
  for i in range(4): 
    random_noun = random.choice(nouns)
    random_verb = random.choice(verbs)
    random_adjective = random.choice(adjectives)
    
    line = random_adjective + " " + random_noun + " " + random_verb + "\n"
    poem += line
  
  return poem

print(generate_poem())

explain：1.This code generates a simple poem using randomly selected words from three pre-defined lists: 
nouns, verbs, and adjectives. The lists contain common words associated with emotions, nature,
and sensory experiences.（The source code is the first to 19th line.）

2.This is a code for automatically generating poetry based on python,
which can be run directly in pychahrm
3.When the code is run, it prints the generated poem to the console using the print() function.
