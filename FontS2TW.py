import sys
from pathlib import Path
from fontTools.ttLib import TTFont

if len(sys.argv) != 2:
    exit()

file = sys.argv[1]
path = Path(file)
font = TTFont(file)

cmap = font['cmap']
table = cmap.getBestCmap()

with open('STWCharacters.txt', 'r', encoding='utf-8') as f:
    for line in f.read().splitlines():
        sc, tc = line.split('\t')

        s = ord(sc)
        t = ord(tc)

        if s in table and t in table:
            t_s = table[s]
            t_t = table[t]

            table[s] = table[t]
            
            print(f'{sc} ({t_s})\t->\t{tc} ({t_t})')

font.save(f'{path.stem}_TW{path.suffix}')
