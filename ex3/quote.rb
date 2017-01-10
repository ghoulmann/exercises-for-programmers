# Exercise 3 (Ruby)

puts "What is the quote?"
quote = gets
quote = quote.chomp

puts "Who said it?"
author = gets
author = author.chomp

puts author + " says, " + "\"" + quote + "\"."
