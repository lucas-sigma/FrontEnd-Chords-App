ref_file = open("songs-teste.txt", "r")
mak_file = open("make-teste.txt", "w")

linha = ref_file.readlines()
linha = ' '.join(linha)
#linha = linha.split()

i = 0
for each in linha:
    if i % 2 == 0:
        linha = linha.replace('(', '<pre>')
        linha = linha.replace(')', '</pre>')
        linha = linha.replace('[', '<bkd>')
        linha = linha.replace(']', '</bkd>')
    else:
        linha = linha.replace('-', '<p>')
        linha = linha.replace('+', '</p>\n')
    i += 1

print(linha)

mak_file.write(linha)

ref_file.close()
mak_file.close()
