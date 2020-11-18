#!/usr/bin/env python3
import sys, os
import argparse
import markovify

# parse command-line arguments 
parser = argparse.ArgumentParser( description='Train a markovify model from a directory full of test files.' )
parser.add_argument( 'source_dir', metavar='SOURCE_DIRECTORY',
                    help='path to a folder containing text files')
parser.add_argument( 'model_file', metavar='MODEL_FILE',
                    help='filename for the trained model')
args = parser.parse_args()

# stick all the file contents together into one big string
# this is very inefficient, but probably OK when our corpora are relatively small
all_text = ""
ignore_files = [ "sources.txt" ]  
for fn in os.listdir(  args.source_dir ):
    
    # skip files we should ignore
    if fn in ignore_files:
        continue
    
    with open( os.path.join(args.source_dir, fn) ) as fp:
        this_text = fp.read()
        all_text += this_text

# build the markov model
text_model = markovify.Text( all_text )

# write it to a file
with open( args.model_file, "w" ) as fp:
    fp.write( 
        text_model.to_json()
    )