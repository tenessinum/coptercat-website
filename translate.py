import os
import argparse
from json import dump, load
import googletrans


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Auto translate script')
    parser.add_argument('-f', dest='ifile', help='Input file',
                        default='src/locales/ru.json')
    parser.add_argument('-l', dest='language', help='Language', default='en')
    parser.add_argument('--force', dest='force', help='No help. No motivation', required=False, default=False)
    args = parser.parse_args()
    translator = googletrans.Translator()

    try:
        with open(args.ifile, 'r', encoding='utf-8') as f:
            parsed_data = load(f)
    except FileNotFoundError:
        print('File not found')
        quit()

    try:
        if args.ifile[-5:len(args.ifile)] != '.json':
            raise Exception
    except:
        print('Invalid file')
        quit()

    output_file = os.path.join(os.path.split(args.ifile[:-5])[0], args.language + '.json')
    
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            translated = load(f)
    except FileNotFoundError:
        translated = {}
    
    translation_result = {}
    
    def rec_find(k, d):
        if args.force != False: return None
        for key in d.keys():
            if type(d[key]) == str:
                if key == k: return d[key]
            else:
                res = rec_find(k, d[key])
                if res != None:
                    return res

        return None 

    def translate_string(s, k):
        res = rec_find(k, translated)
        if res != None:
            return res
        else:
            print('Translating', s)
            return translator.translate(s, src=os.path.split(
                    args.ifile[:-5])[1], dest=args.language).text

    def translate_json(input, output):
        for k in input:
            if type(input[k]) == str:
                output[k] = translate_string(input[k], k)
            else:
                output[k] = {}
                translate_json(input[k], output[k])

    translate_json(parsed_data, translation_result)

    with open(output_file, 'w') as of:
        dump(translation_result, of, indent=4, ensure_ascii=False)
