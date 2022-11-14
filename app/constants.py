exit_words = ['close', 'bye', 'quit', 'exit']
hello_words = ['hi', 'hello', 'q', 'privet']

# for filter_folder
CYRILLIC_SYMBOLS = " абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "_", "a", "b", "v", "g", "d", "e", "e", "j", "z",
    "i", "j", "k", "l", "m", "n", "o", "p", "r", "s",
    "t", "u", "f", "h", "ts", "ch", "sh", "sch", "",
    "y", "", "e", "yu", "ya", "je", "i", "ji", "g"
)
IGNORE_FOLDERS = ("image", "video", "documents", "audio", "archives")
TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


EXTENSIONS = {
    "image": ['JPEG', 'PNG', 'JPG', 'SVG'],
    "video": ['AVI', 'MP4', 'MOV', 'MKV'],
    "documents": ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'PPT'],
    "audio": ['MP3', 'OGG', 'WAV', 'AMR'],
    "archives": ['ZIP', 'GZ', 'TAR']
}
