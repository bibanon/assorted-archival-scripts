#!/usr/bin/python3
# Append more subjects to an existing Internet Archive item.
# Created by Antonizoon for the Bibliotheca Anonoma Field Research Team.

# Dependencies: pip install internetarchive
from docopt import docopt
from internetarchive import get_item
from internetarchive import search_items

__doc__ = """ ia-subject-mod.py. Append more subjects to all Internet Archive items uploaded by the current user.

Usage:
  ia-subject-mod.py <identifier> (<subject>...)

Arguments:
  <identifier>            Internet Archive Item URL Identifier.
  <subject>               All the subject tags to be appended. Add multiple.
"""

def append_meta(identifier, add_subject):
	# obtain existing metadata for given item
	item = get_item(identifier)
	subject = item.metadata['subject']

	# if subjects are given as a list, convert to semicolon-separated list
	if isinstance(subject, list):
		l = ""
		for element in subject:
			l += "%s;" % element
		subject = l

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

def append_acct_meta(uploader_email, add_subject):
	# get a list of all items made by the uploader
	print("Searching for all items...")
	search = search_items('uploader:%s' % uploader_email)
	
	# add subjects to each item in search results
	for result in search:
		append_meta(result['identifier'], add_subject)

def main():
	args = docopt(__doc__)
	
	# parameters
	identifier = args['<identifier>']
	
	# populate subjects to add
	add_subject = ""
	for subject in args['<subject>']:
		add_subject += "%s;" % subject
	
	# append additional tags to item
	append_meta(identifier, add_subject)

if __name__ == "__main__":
	main()