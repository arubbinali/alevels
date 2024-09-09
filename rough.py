#1a
def ReadWords(file_name):
    file = open(file_name, 'r')
    file_data = file.read()
    file.close()
    WordArray = file_data.strip().split()
    number_of_answers = len(WordArray)

def Readwords(file_name):
    with open(file_name, 'r') as file:
        file_data = file.read()
    WordArray = file_data.strip().split()
    number_of_answers = len(WordArray)

#1b
choice = input("Enter easy/medium/hard:   ")