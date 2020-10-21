import argparse
import tarfile
import os


parser = argparse.ArgumentParser()
parser.add_argument("file", help="Point me to the file", type=str)
parser.add_argument("string", help="Enter string you want to search for.", type=str)
args = parser.parse_args()
os.mkdir('searchoutput')

with open(args.file, 'rb') as f:
    tar = tarfile.open(args.file)
    memberdata = tar.getmembers()
    for member in memberdata:
        if args.string in member.name:
            print(tar.extract(member, "searchoutput"))
print(os.listdir('searchoutput'))
