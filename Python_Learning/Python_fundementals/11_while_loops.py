import time

#While loops

# syntax
#while <condition>

  #Block of code
  #while <condition>
  #Block of code
  #** Optional** if <condition>
                 #    break

counter = 0

while counter < 28:
    print("let's go out my age is:", counter)
    counter+= 1
    time.sleep(0.5)


print("end")


while True:
    print('Welcome to the loop')
    word = input ("Tell me a word")
    if word == "bananas":
        print(" you've cracked the code")
        break
    else:
        print("HAHAHAHAHA YOU FOOL. YOU WILL NEVER LEAVE")
        print("HAHAHHAHAHAHA")