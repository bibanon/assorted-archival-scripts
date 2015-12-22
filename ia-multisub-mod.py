#!/usr/bin/python3
# Append more subjects to all Internet Archive items uploaded by the current user.
# Created by Antonizoon for the Bibliotheca Anonoma Field Research Team.

# Dependencies: pip install internetarchive
import sys
import json
from internetarchive import get_item
from internetarchive import search_items

def append_meta(identifier, add_subject):
	# obtain existing metadata for given item
	item = get_item(identifier)
	subject = item.metadata['subject']

	# append new subject to existing subject
	if str(subject).endswith(';'):
		new_subject = str(subject) + add_subject
	else:
		new_subject = str(subject) + ';' + add_subject

	# upload new metadata
	r = item.modify_metadata(dict(subject=new_subject))

	# check if metadata successfully modified
	if (r.status_code == 200):
		print(":: [Identifier] Item: [%s] %s" % (identifier, item.metadata['title']))
		print("Subjects '%s' successfully appended." % add_subject)
		print("Result: %s" % new_subject)
	else:
		print("Failed to add new subjects.")

def main():
	# usage statement
	if(len(sys.argv) < 3):
		print("Append new subjects to all Internet Archive items uploaded by the current user.")
		print("Usage: %s 'uploaders.emailaccount@gmail.com' 'subject1;subject2;'" % (sys.argv[0]))
		sys.exit(1)
	else:
		# parameters
		uploader_email = sys.argv[1]
		add_subject = sys.argv[2]
		
	# get a list of all items made by the uploader
	print("Searching for all items...")
	search = search_items('uploader:%s' % uploader_email)
	
	# add subjects to each item in search results
	for result in search:
		append_meta(result['identifier'], add_subject)

if __name__ == "__main__":
	main()
