#!/bin/bash
# Curl reupload script for IA's S3 like API
# use this if uploading to an existing bucket
# Created by Antonizoon for the Bibliotheca Anonoma
# Based on info from here: https://gist.github.com/Asparagirl/6206247

# require first argument
if [ $# -eq 0 ]; then
	echo "Note: You must edit this script and add the IA S3 Access/Secret Keys."
	echo "Usage: $0 <ia-s3-bucket> <path>/<filename>";
	echo "Example: $0 ibm-pccbbs ~/downloads/item.7z"
	exit 1;-
fi

# add IA S3 Access/Secret API Keys
export IA_S3_ACCESS_KEY=""
export IA_S3_SECRET_KEY=""

# local file location
#export FILE_LOCAL_PATH="/home/user/downloads/pccbbs/warc"
#export FILE_LOCAL_NAME="file.7z"
#export FILE_LOCAL_FULL="$FILE_LOCAL_PATH/$FILE_LOCAL_NAME"
export FILE_LOCAL_NAME=`basename $2`
export FILE_LOCAL_FULL=$2

# find file size to warn internet archive about it
export FILESIZE=`stat --printf="%s" $FILE_LOCAL_FULL`

# IA Directory
export FILE_IA_DIRECTORY=$1
export FILE_IA="http://s3.us.archive.org/$FILE_IA_DIRECTORY/$FILE_LOCAL_NAME"

# curl upload
curl --location \
	--header "authorization: LOW $IA_S3_ACCESS_KEY:$IA_S3_SECRET_KEY" \
	--header "x-archive-size-hint: $FILESIZE" \
	--upload-file $FILE_LOCAL_FULL \
	"http://s3.us.archive.org/$FILE_IA_DIRECTORY/$FILE_LOCAL_NAME"