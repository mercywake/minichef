import argparse
import base64
import codecs
import hashlib
import html
from urllib.parse import quote, unquote

DESCRIPTION = """
MiniChef - a simple data encode/decode tool.

Supported methods:
  base64, md5, sha1, rot13, url, html-entity

Examples:

  md5:
    python minichef.py -m md5 -s hello -e

  sha1:
    python minichef.py -m sha1 -s hello -e

  base64 encode:
    python minichef.py -m base64 -s hello -e

  base64 decode:
    python minichef.py -m base64 -s aGVsbG8= -d

  rot13:
    python minichef.py -m rot13 -s hello -e

  url encode:
    python minichef.py -m url -s "https://a.com/a b" -e
  
  html-entity:
    python minichef.py -s '<html>' -m html-entity -e         
         
  file:
    python minichef.py -m md5 -f test.txt -e
"""


def main():
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '-m',
        '--method',
        choices=[
            'base64',
            'md5',
            'sha1',
            'rot13',
            'url',
            'html-entity'
        ],
        help='calculate method'
    )

    input_group = parser.add_mutually_exclusive_group(
    )

    input_group.add_argument(
        '-s',
        '--string',
        help='input string'
    )

    input_group.add_argument(
        '-f',
        '--file',
        help='input file'
    )

    mode_group = parser.add_mutually_exclusive_group()

    mode_group.add_argument(
        '-e',
        '--encode',
        action='store_true',
        help='encode mode'
    )

    mode_group.add_argument(
        '-d',
        '--decode',
        action='store_true',
        help='decode mode'
    )

    parser.add_argument(
        '--example',
        action='store_true',
        help='python minichef.py -m base64 -s a -e'
    )

    args = parser.parse_args()

    if args.example:
        print(DESCRIPTION)
        return

    if not args.method:
        raise ValueError(
            "please specify method, example: -m md5"
        )

    # md5/sha1 only encode
    if args.decode and args.method in [
        "md5",
        "sha1"
    ]:
        raise ValueError(
            "md5 and sha1 only support encode"
        )

    result = ''
    if args.method == "base64":
        result = base64_func(
            args.string,
            args.file,
            args.decode
        )

    elif args.method == "md5":
        result = md5_hash(
            args.string,
            args.file
        )

    elif args.method == "sha1":
        result = sha1_hash(
            args.string,
            args.file
        )

    elif args.method == "rot13":
        result = rot13_func(
            args.string,
            args.file
        )

    elif args.method == "url":
        result = url_func(
            args.string,
            args.file,
            args.decode
        )
    elif args.method == "html-entity":
        result = html_entity_func(
            args.string,
            args.file,
            args.decode
        )

    print(result)


def md5_hash(string, file):
    if file:
        with open(file, 'rb') as f:
            string = f.read()
    else:
        string = string.encode()

    return hashlib.md5(string).hexdigest()


def sha1_hash(string, file):
    if file:
        with open(file, 'rb') as f:
            string = f.read()
    else:
        string = string.encode()

    return hashlib.sha1(string).hexdigest()


def base64_func(string, file, decode):
    if file:
        with open(file, 'rb') as f:
            string = f.read()
    else:
        string = string.encode()

    if decode:
        return base64.b64decode(string).decode()

    return base64.b64encode(string).decode()


def url_func(string, file, decode):
    if file:
        with open(file, 'r', encoding='utf-8') as f:
            string = f.read()

    if decode:
        return unquote(string)

    return quote(string, safe="")


def rot13_func(string, file):
    if file:
        with open(file, 'r', encoding='utf-8') as f:
            string = f.read()

    return codecs.encode(string, 'rot13')


def html_entity_func(string, file, decode):
    if file:
        with open(file, 'r', encoding='utf-8') as f:
            string = f.read()
    if decode:
        return html.unescape(string)
    return html.escape(string)


if __name__ == '__main__':
    main()
