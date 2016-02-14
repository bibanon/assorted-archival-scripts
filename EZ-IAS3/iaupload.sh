#!/bin/bash
# Curl upload script for IA's S3 like API
# Created by Antonizoon for the Bibliotheca Anonoma
# Based on info from here: https://gist.github.com/Asparagirl/6206247

# require first argument
if [ $# -eq 0 ]; then
	echo "Note: You must edit this script, set the item metadata, and add the IA S3 Access/Secret Keys."
	echo "Usage: $0 <path>/<filename>";
	echo "Example: $0 ~/downloads/item.7z"
	exit 1;
fi

# add IA S3 Access/Secret API Keys
export IA_S3_ACCESS_KEY=""
export IA_S3_SECRET_KEY=""

# item information
export ITEM_TITLE="The Do/k/ument"
export ITEM_DESCRIPTION="The Do/k/ument is a collection of military training manuals, 4chan screencaps, and survival guides for the 4chan /k/ enthusiast. The Murdercube maintains a modern version. https://murdercube.com <\br>Magnet Link: magnet:?xt=urn:btih:f4294ed6278a78be6200131044a7e058017c2dbf&dn=The+Do%2Fk%2Fument&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337"
export ITEM_KEYWORDS="Bibliotheca Anonoma;4chan;4chan /k/;/k/;Weapons;Survival;Defense"

# IA Directory
export FILE_IA_DIRECTORY="the-dokument"
export FILE_IA="http://s3.us.archive.org/$FILE_IA_DIRECTORY/$FILE_LOCAL_NAME"

# local file location
#export FILE_LOCAL_PATH="/home/user/downloads/pccbbs/warc"
#export FILE_LOCAL_NAME="file.7z"
#export FILE_LOCAL_FULL="$FILE_LOCAL_PATH/$FILE_LOCAL_NAME"
export FILE_LOCAL_FULL=$1		# first argument

# curl upload
curl --location \
	--header "x-amz-auto-make-bucket:1" \
	--header "x-archive-meta01-collection:opensource" \
	--header "x-archive-meta-mediatype:web" \
	--header "x-archive-meta-title:$ITEM_TITLE" \
	--header "x-archive-meta-description:$ITEM_DESCRIPTION" \
	--header "x-archive-meta-subject:$ITEM_KEYWORDS" \
	--header "authorization: LOW $IA_S3_ACCESS_KEY:$IA_S3_SECRET_KEY" \
	--upload-file "$FILE_LOCAL_FULL" "$FILE_IA"