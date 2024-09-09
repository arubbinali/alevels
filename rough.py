def ReadWords(file_name):
    File = open(file_name, 'r')
    DataRead = File.read().strip()
    WordArray = DataRead.split()
    