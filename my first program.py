"""My first Program"""

print                 'Welcome to Calvins first program'

print     'This program will tell you what is the attribute of Pikachu or Charmander pokemons'


pikachu = "pikachu is an electric type pokemon"

charmander = "charmander is a fire type pokemon"

original = raw_input("Please type in pikachu or charmander:")

if len(original) == 0 or not original.isalpha:
  print 'please enter either charmander or pikachu'

elif  original == int:
  print 'Please enter a pokemon not a number'

elif original == "pikachu":
  print pikachu

elif original == "charmander":
  print charmander

else:
  print 'try again'

again = raw_input("Would you like to try again? Or would you prefer more options? : ")

options = "somthing"

if again == "yes":
  print original

elif again == "no":
   print "thanks for playing"

elif original == options:
   print "something"

else:
   print  'please type in a valid option yes or no'




quit()
