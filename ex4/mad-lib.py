# ISM 2
# Exercise 4 (Hogan/Mad Lib)
# Python
# modified: function + substitution

prompt = "What's a good "

def question( prompt, part ):
    part = raw_input(prompt + part + "? ")
    return part



noun = question( prompt, "noun")
verb = question( prompt, "verb")
adjective = question( prompt, "adjective" )
adverb = question( prompt, "adverb" )

madlib = "Does your %s %s %s %s?" % (adjective, noun, verb, adverb)

print madlib




