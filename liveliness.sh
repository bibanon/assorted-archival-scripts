#!/bin/bash
# liveliness.sh: Check the HTTP status code of all urls in a given url-list.
# curl command by stackexchange, scripted by Antonizoon for the Bibliotheca Anonoma.

display_usage() { 
	echo "$0 : Checks the HTTP status code of all urls in a given url-list." 
	echo -e "\nUsage:\n$0 url-list.txt \n" 
	echo ""
	echo "To continue where you left off before, first find the last URL scraped:"
	echo "    cat results-2014-01-03.txt | tail"
	echo "Then search for the URL given in url-list.txt:"
	echo "    grep -n \"example.com\" url-list.txt"
	echo "Then cut a slice of the url-list.txt starting only from that line number."
	echo "    sed '1,/example.com/d' url-list.txt > url-list-slice.txt"
	echo "Finally, run the script again on the slice:"
	echo "    $0 url-list-slice.txt"
} 

# if less than two arguments supplied, display usage 
if [ "$#" -ne 1 ]
then 
	display_usage
	exit 1
fi 

# url-file is first argument
url_file=$1

# name the results file by datetime
now=$(date +%Y%m%d_%H%M%S)

xargs -n1 -P 10 curl -o /dev/null --silent --head --write-out '%{url_effective}: %{http_code}\n' < "$url_file" | tee "results-$now.txt"