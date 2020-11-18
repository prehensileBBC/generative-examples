#!/usr/bin/env python3
import os, sys
from bs4 import BeautifulSoup
import requests

ignore_list  = [ "fetch_sources.py", "sources.txt" ]


# return the plain text of the page referenced by url
def process_url( url ):
    # fetch the web page referenced by url
    req = requests.get( url )
    # use BeautifulSoup to extract page text
    soup = BeautifulSoup( req.content, 'html.parser' )
    return soup.text


# process a single source directory
def process_sourcedir( source_dir ):
    # source_files = os.listdir( source_dir )
    # source_files = [ fn for fn in source_files if fn not in ignore_list ]
    # assume that this directory contains a file named "sources.txt" which contains a list of urls
    sources_file = os.path.join(source_dir,"sources.txt")
    # ...open it...
    with open( sources_file ) as fp:
        # read a list of urls from the file and remove trailing newlines
        urls = [line.rstrip() for line in fp]
        # step through list of urls
        for url in urls:
            # get page text for a url
            text = process_url( url )
            # construct the filename we'll be writing to...
            # get the last bit of the url
            fn_out = os.path.basename( url )
            # stick ".txt" on the end
            fn_out = "{}.txt".format( fn_out )
            # construct a full file path by joining this source directory name and our constructed filename
            fn_out = os.path.join( source_dir, fn_out )
            # write the fetched page text to that file path
            with open( fn_out, "w" ) as fp_out:
                fp_out.write( text )
            

# process all source directories
def process_all_sources( source_path ):

    # get a listing of everything in source_path
    list_source = os.listdir( source_path )

    # remove files from list_source that we don't want
    list_source = [ fn for fn in list_source if fn not in ignore_list ]
    
    # step through everything in list_source, assume it's all subdirectories
    for fn in list_source:
        process_sourcedir( 
            os.path.join( source_path, fn )
        )


# kick off main processing task
process_all_sources( '.' )
    