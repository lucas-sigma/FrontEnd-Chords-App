ref_file = open("songs.txt", "r", encoding="utf8")
mak_file = open("make.txt", "w", encoding="utf8")

linha = ref_file.readlines()
linha = ' '.join(linha)

for text in linha:
        linha = linha.replace('(', '<pre>')
        linha = linha.replace(')', '</pre>')
        linha = linha.replace('[', '<kbd>')
        linha = linha.replace(']', '</kbd>')
        linha = linha.replace('-', '<p>')
        linha = linha.replace('+', '</p>\n')

mak_file.write(linha)

ref_file.close()
mak_file.close()
