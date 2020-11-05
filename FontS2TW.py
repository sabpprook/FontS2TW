# coding=utf-8

import json
import subprocess
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit

    fnt = sys.argv[1]

    '''
    obj = subprocess.check_output(('otfccdump.exe', '-n', '0', '--hex-cmap', fnt)).decode('utf-8', 'ignore')
    obj = json.loads(obj.encode('utf-8'))
    '''

    obj = json.loads(subprocess.check_output(('otfccdump.exe', '-n', '0', '--hex-cmap', fnt)))

    with open('STCharacters.txt', encoding='utf-8') as f:
        for line in f:
            st = line.rstrip('\n').split('\t')
            if st[0] == st[1]:
                continue
            s = f'U+{ord(st[0]):4X}'
            t = f'U+{ord(st[1]):4X}'
            try:
                obj['cmap'][s] = obj['cmap'][t]
            except:
                print('no %s' % st[0])

    subprocess.run(['otfccbuild.exe', '-o', '%s_TC.ttf' % fnt[0:fnt.rfind('.')]], input=json.dumps(obj), encoding='utf-8')
