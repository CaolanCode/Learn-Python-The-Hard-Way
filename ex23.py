import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline() # read one line from languages.txt

    if line: # if line contains something
        print_line(line, encoding, errors) 
        return main(language_file, encoding,errors)

def print_line(line, encoding, errors):
    next_lang = line.strip() # remove leading and trailing bytes
    raw_bytes = next_lang.encode(encoding, errors=errors) # encode into raw bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors) # decode the raw bytes back to a string
    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf=8")

main(languages, encoding, error)
