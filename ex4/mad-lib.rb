# exercise 4
# ruby
# function plus variable interpellation

def question(prompt)
    puts prompt
    output = gets.chomp
    return output
end
    
noun = question("What singular noun?")
adjective = question("What adjective?")
verb = question("What singular verb \(e.g. eats\) ?")
adverb = question("What adverb?")

madlib = "The #{adjective} #{noun} #{verb} #{adverb}."
puts madlib

