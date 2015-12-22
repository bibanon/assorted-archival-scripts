#!/usr/bin/python3
# Append more subjects to an existing Internet Archive item.
# Created by Antonizoon for the Bibliotheca Anonoma Field Research Team.

# Dependencies: pip install internetarchive
import sys
from internetarchive import get_item

# usage statement
if(len(sys.argv) < 3):
	print("Append more subjects to an existing item.")
	print("Usage: %s <identifier> 'subject1;subject2;'" % (sys.argv[0]))
	sys.exit(1)
else:
	# parameters
	identifier = sys.argv[1]
	add_subject = sys.argv[2]

# obtain existing metadata for given item
item = get_item(identifier)
subject = item.metadata['subject']

# append new subject to existing subject
new_subject = str(subject) + add_subject

# upload new metadata
r = item.modify_metadata(dict(subject=new_subject))

# check if metadata successfully modified
if (r.status_code == 200):
	print(":: [Identifier] Item: [%s] %s" % (identifier, item.metadata['title']))
	print("Subjects '%s' successfully appended." % add_subject)
	print("Result: %s" % new_subject)
else:
	print("Failed to add new subjects.")
