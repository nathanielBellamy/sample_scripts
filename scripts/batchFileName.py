import os

# motivation
#   => batch edit file names
#   => useful when managing sample kits without relying upon a directory structure
#
#
# use 
#   => assemble a kit of samples in a source directory
#   => chose a kit prefix (e.g. "my_kit_")
#

directory = "/Users/etaote/Samples/Drums/Roland_TR626/"
for filename in os.listdir(directory):
 #  os.rename(directory + filename, directory + filename)
 name = filename[2:len(filename)]
 os.rename(directory + filename, directory + "my_kit_ " + name)

