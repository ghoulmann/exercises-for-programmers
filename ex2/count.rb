# ISM 1
# 1/9/17
# ruby
# count characters (ex2)

puts "What is the input string? "
thestring = gets
thestring = thestring.chomp
num = thestring.size
puts thestring + " has " + num.to_s + " characters."
