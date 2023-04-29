import argparse
import hashlib

def hash_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as in_file, open(output_file, 'w', encoding='utf-8') as out_file:
        for line in in_file:
            verb = line.strip()
            hashed_verb = hashlib.sha512(verb.encode('utf-8')).hexdigest()
            otp = f"{verb}:{hashed_verb}"
            out_file.write(otp + '\n')

def main():
    parser = argparse.ArgumentParser(description='Read a file and hash each line')
    parser.add_argument('input_file', help='Name of file to read')
    parser.add_argument('--output', '-o', help='Name of output file', default='keyValueHashed.txt')
    args = parser.parse_args()

    hash_file(args.input_file, args.output)

    print(f"{args.input_file} has been processed and saved as {args.output}.")

if __name__ == '__main__':
    main()
