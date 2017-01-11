# Exercise 3 (Ruby)

puts "What is the quote?" #  asks (prints What is the quote
quote = gets              # ask for input (in response to question)
quote = quote.chomp       # gets rid of \n

puts "Who said it?"       # asks (prints the question)
author = gets             # asks for input (after the question is asked
author = author.chomp     # gets rid of \n

puts author + " says, " + "\"" + quote + "\"."  # example of escape character using backslash
