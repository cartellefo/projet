
class whitesheet:

    def __init__(self):
        
        self.surface = ""
    def write(self, message_a_ecrire):
        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def read(self):
    	print(self.surface)

    def cancel(self):
    	self.surface = ""
#if __name__ == '__main__':
tab = whitesheet()
tab.read()
tab.write("Coooool ! Ce sont les vacances !")
tab.read()
tab.write("joyeux noel")
tab.read()
tab.cancel()
print(tab.surface)

# class complex:
# 	complexCount = 0
# 	def __init__(self, real,imag):
# 		self.r = real
# 		self.i = imag
# 		complex.complexCount += 1

# c1 = complex(2,4)
# print(c1.r, c1.i)
# #print(c1.i)







 

