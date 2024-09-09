def ReadWords(file_name):
    file = open(file_name, 'r')
    file_data = file.read()
    file.close()
    WordArray = file_data.strip().split()
    number_of_answers = len(WordArray)