# MiniChef

A simple command line tool for encoding, decoding and hashing data.

MiniChef is a lightweight Python CLI utility inspired by tools like CyberChef.
It supports common data transformation operations such as Base64, URL encoding, ROT13, MD5 and SHA1.

No external dependencies are required. It only uses Python standard libraries.

## Features

Supported methods:

* Base64 encode/decode
* URL encode/decode
* ROT13 transform
* html-entity encode/decode
* MD5 hash
* SHA1 hash
* String input
* File input

## Requirements

* Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/yourname/minichef.git
cd minichef
```

No additional packages are required.

## Usage

Basic format:

```bash
python minichef.py -m <method> -s <string> -e/-d
```

or use a file:

```bash
python minichef.py -m <method> -f <file> -e/-d
```

## Examples

### MD5

Hash a string:

```bash
python minichef.py -m md5 -s hello -e
```

Output:

```text
5d41402abc4b2a76b9719d911017c592
```

Hash a file:

```bash
python minichef.py -m md5 -f test.txt -e
```

---

### SHA1

```bash
python minichef.py -m sha1 -s hello -e
```

---

### Base64 Encode

```bash
python minichef.py -m base64 -s hello -e
```

Output:

```text
aGVsbG8=
```

### Base64 Decode

```bash
python minichef.py -m base64 -s aGVsbG8= -d
```

Output:

```text
hello
```

---

### ROT13

```bash
python minichef.py -m rot13 -s abcdefg -e
```

Output:

```text
nopqrst
```

---

### URL Encode

MiniChef uses strict percent encoding.

Example:

```bash
python minichef.py -m url -s "https://a.com/a b" -e
```

Output:

```text
https%3A%2F%2Fa.com%2Fa%20b
```

---

### html-entity

MiniChef use default html encode

Example:

```text
python minichef.py -s '<html>' -m html-entity -e
```

Output:

```text
&lt;html&gt;
```

## File Input

MiniChef supports processing files:

```bash
python minichef.py -m sha1 -f example.txt -e
```

String input and file input cannot be used together.

## Available Options

| Option         | Description             |
|----------------|-------------------------|
| `-m, --method` | Select operation method |
| `-s, --string` | Input string            |
| `-f, --file`   | Input file              |
| `-e, --encode` | Encode mode             |
| `-d, --decode` | Decode mode             |
| `--example`    | Show examples           |

## Supported Methods

| Method      | Encode | Decode |
|-------------|--------|--------|
| md5         | ✅      | ❌      |
| sha1        | ✅      | ❌      |
| base64      | ✅      | ✅      |
| url         | ✅      | ✅      |
| rot13       | ✅      | ✅      |
| html-entity | ✅      | ✅      |

## Error Handling

MiniChef validates:

* Unknown methods
* Missing input
* Using string and file together
* Invalid encode/decode combinations
* Unsupported decode operations

## License

Apache License

## Author

Created with Python and curiosity.
