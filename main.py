import unicodedata
def get_unicode_variations(letter):
    letter_code = ord(letter)
    # For some characters, you might want to check all
    # code points up to 0x10FFFF
    for i in range(65536):
        decomp = unicodedata.decomposition(chr(i))
        # Mappings starting with '<...>' indicate a
        # compatibility mapping (NFKD, NFKC) which we ignore.
        while decomp != '' and not decomp.startswith('<'):
            first_code = int(decomp.split()[0], 16)
            if first_code == letter_code:
                print(chr(i), unicodedata.name(chr(i)))
                break
            # Try to decompose further
            decomp = unicodedata.decomposition(chr(first_code))

get_unicode_variations("C")