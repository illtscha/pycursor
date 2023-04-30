from pycursor.pycursor import pyCursor
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--byPath', action='store_true', required="--createCRS" in sys.argv and "--byFile" not in sys.argv and "--byName" not in sys.argv)
    parser.add_argument('--byFile', action='store_true', required="--createCRS" in sys.argv and "--byPath" not in sys.argv and "--byName" not in sys.argv)
    parser.add_argument('--byName', action='store_true', required="--createCRS" in sys.argv and "--byPath" not in sys.argv and "--byFile" not in sys.argv)
    parser.add_argument('--byCRS', action='store_true')
    parser.add_argument('--createCRS', action='store_true')


    parser.add_argument('--alternate', type=str, required=False)
    parser.add_argument('--handwriting', type=str, required=False)
    parser.add_argument('--precision', type=str, required=False)
    parser.add_argument('--link', type=str, required=False)
    parser.add_argument('--move', type=str, required=False)
    parser.add_argument('--diagonal1', type=str, required=False)
    parser.add_argument('--diagonal2', type=str, required=False)
    parser.add_argument('--horizontal', type=str, required=False)
    parser.add_argument('--vertical', type=str, required=False)
    parser.add_argument('--unavailable', type=str, required=False)
    parser.add_argument('--text', type=str, required=False)
    parser.add_argument('--busy', type=str, required=False)
    parser.add_argument('--working', type=str, required=False)
    parser.add_argument('--help', type=str, required=False)
    parser.add_argument('--normal', type=str, required=False)
    parser.add_argument('--person', type=str, required=False)
    parser.add_argument('--location', type=str, required=False)



    parser.add_argument('-o', '--open', action='store_true')

    parser.add_argument('-p', '--path', type=str, required="--byPath" in parser._option_string_actions or "--byFile" in parser._option_string_actions or "--byName" in parser._option_string_actions or "--byCRS" in parser._option_string_actions)

    parser.add_argument('-n', '--name', type=str, required="--byPath" in parser._option_string_actions or "--byFile" in parser._option_string_actions or "--byName" in parser._option_string_actions or "--byCRS" in parser._option_string_actions)

    args = parser.parse_args()


    kwargspath = {}
    for arg in ['alternate', 'handwriting', 'precision', 'link', 'move', 'diagonal1', 'diagonal2', 'horizontal', 'vertical', 'unavailable', 'text', 'busy', 'working', 'help', 'normal', 'person', 'location']:

        value = getattr(args, arg)
        if value is not None:
            kwargspath[arg] = value

    if args.open:
        pyCursor("none", "none").openMainCpl()

    if args.createCRS:
        if args.byPath:
            cursor = pyCursor(args.path, args.name)
            cursor.createCRSByPath()
        if args.byName:
            cursor = pyCursor(args.path, args.name)
            cursor.createCRSByName()
        if args.byFile:
            cursor = pyCursor(args.path, args.name)
            cursor.createCRS(**kwargspath)
    elif args.byPath:
        cursor = pyCursor(args.path, args.name)
        cursor.matchByPath()
    elif args.byFile:
        cursor = pyCursor(args.path, args.name)
        cursor.matchByFile(**kwargspath)
    elif args.byName:
        cursor = pyCursor(args.path, args.name)
        cursor.matchByFile()
    elif args.byCRS:
        cursor = pyCursor(args.path, args.name)
        cursor.matchByCRS()

#    print(args)