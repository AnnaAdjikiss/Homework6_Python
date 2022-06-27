# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

def rle_compression(chars):
    chars = chars + ' '
    line_coded = ''
    prev_char = ''
    count = ''
    for char in chars:
        if char != prev_char:
                line_coded += str(count) + prev_char
                count = 1
                prev_char = char
        else:
            count += 1
    return line_coded


file = 'original_file.txt' 
with open(str(file), 'r') as data:
        text = data.read()
        print(text)

text_coded = rle_compression(text)
print(text_coded)

with open('RLE_compressed_file.txt', 'w') as data:
    data.write(text_coded)

#def unpacking_rle

with open('RLE_compressed_file.txt', 'r') as data:
    text_rle = data.read()

