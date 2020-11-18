#!/usr/bin/env python3
import sys, os
import argparse
import markovify

# parse command-line arguments 
parser = argparse.ArgumentParser( description='Generate text from a saved Markovify model' )
parser.add_argument( 'model_file', metavar='MODEL_FILE',
                    help='filename for the trained model')
parser.add_argument( '--num_sentences', metavar='NUM_SENTENCES', type=int, default=5,
                    help='number of sentences to generate')
args = parser.parse_args()

# read the saved model
with open( args.model_file ) as fp:
    model_json = fp.read()
    model = markovify.Text.from_json( model_json )

# generate some text
sentences = []
for i in range( args.num_sentences ):
    sentences.append(
        model.make_sentence()
    )

print( " ".join(sentences) )