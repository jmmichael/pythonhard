def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "That's enough for a a party"
	print "Get a blanket\n"
print "give the function's number directly:"
cheese_and_crackers(20,30)

print "OR use variables form the script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) 

print "do maths as well:"
cheese_and_crackers(10+20, 5+6)

print "and combine the two:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

