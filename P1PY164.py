# import PY164

# PY164.greeting("Sridhar")

# PY164.add(10,20)
# PY164.sub(10,5)
# PY164.mul(10,2)
# PY164.div(10,2)
# PY164.mod(10,2)

##################################################

# import PY164 as PY 

# PY.add(100,200)


##################################################

# import platform
# answer=platform.system()
# print(answer)

###################################################

# import platform 
# answer=dir(platform)
# print(answer)

###################################################

# QR Code Generator - pip install qrcode 

# import qrcode 

# data="Credo Systemz"
# qr=qrcode.make(data)
# qr.save("cszqrcode.png")
# print("QR Code Generated!!!")


#################################################

# Text to Voice using pyttsx3


# import pyttsx3 

# engine=pyttsx3.init()
# engine.say("Welcome to Python Programming - Welcome to Credo Systemz")
# engine.runAndWait()

#####################################################


# Number to Word using num2words

from num2words import num2words 

number=12345
print(num2words(number))
