#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Python script for internetarchive wrapper to upload contents of a folder to the Internet Archive.
# Script created by the Bibliotheca Anonoma
"""EZ-IAS3 Uploader.

Usage: 
    ezias3 create <item_id>
    ezias3 upload <item_id> <file>
Options:
    --metadata=<META_FILE>   Set custom YAML metadata file for item.
    --timeout=<LOOPS>        How many times to retry upload before quitting. [Default: 3]
"""

from internetarchive import get_item
import os
import time
import yaml
from docopt import docopt

# generator that lists all files within given directory
def all_files(top):
    for root, dirs, files in os.walk(top, topdown=True):
        for name in files:
            yield os.path.join(root, name)

class Uploader(object):
    """
        IA S3 Uploader Class
    """
    def __init__(self, item_id, dst_dir, metadata):
        self.item_id = item_id
        self.item = get_item(item_id)        # create IA item
        self.dst_dir = dst_dir
        self.metadata = metadata
        
        # three strikes and we're out
        self.timeout = 3
        
        # IA S3 API keys
        self.access_key = None
        self.secret_key = None

    def configure(self):
        """
            Grab IA S3 ACCESS_KEY and SECRET_KEY.
            Reuse existing code in the Python InternetArchive wrapper.
            
            https://github.com/jjjake/internetarchive/blob/master/internetarchive/iacli/ia_configure.py
        """
        
        # check if yml config exists and load access keys
        
        # if yml config doesn't exist, run ia_configure
        
        pass

    def load(self):
        """
            Get a list of all previously uploaded files.
        """
        pass

    def record(self, src_path):
        """
            Note down successful upload.
        """
        print("recorded %s" % src_path)
    
    def is_uploaded(self, src_path):
        """
            Check if file was previously uploaded.
        """
        return True
    
    def upload(self, src_path):
        """ 
            Upload a single item to the Internet Archive.
            Returns True if item successfully uploaded.
            
            * src_path - item to upload
        """
        # attempt to upload
        uploaded = False
        loops = 0
        while not uploaded and (loops <= self.timeout):
            # upload to IA
            uploaded = self.item.upload(src_path, 
                metadata = self.metadata, 
                access_key = self.access_key, 
                secret_key = self.secret_key
            )
            
            # wait 5-30 seconds before next upload
            if not uploaded:
                wait_time = 5 * (loops + 1)
                time.sleep(wait_time)
                print("Upload failed. Retrying in %i seconds...", )
                
            loops += 1
        
        print("`%s` uploaded to %s." % (src_path, self.dst_dir))
        
        return uploaded
        
    def upload_dir(self, src_path):
        """
            Upload an entire directory to the Internet Archive.
        """
        # load the list of files already uploaded
        self.load()
        
        # os.walk is used to list out entire directory structure
        for f in all_files('.'):
            # check if file was already uploaded, don't upload again if it was
            if self.is_uploaded(f):
                continue
            
            # upload item to IA
            self.upload(f)
        
            # if successful, note it down
            self.record(f)

def main():
    """Set up Arguments"""
    # get arguments from docopt
    item_id = args['<item_id>']             # IA item to upload to
    meta_file = args['--metadata']          # metadata file containing item metadata, perhaps in YAML. Later, have first timers create it themselves.
    
    # default metadata filename is <item_id>.yml
    if args['--metadata'] == None:
        meta_file = "%s.yml" % item_id
    metadata = {}
    
    """Upload all files in given directory"""
    iaup = Uploader(item_id, "/", metadata)     # create Uploader object
    iaup.upload('item.txt')
        
if __name__ == "__main__":
    args = docopt(__doc__, version='0.0.1')
    main()