from cryptographyFramework import *

initializeWrite()
user = "jokas"
password = "123"
encryptedText = encryptMessage(user, password, "Vamo caramba")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "e o pingas")
saveNewLine(encryptedText)

