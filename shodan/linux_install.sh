#!/bin/bash

if [ `/bin/id -u` -eq 0 ]; then

	rm -vR /etc/shlookup
	mkdir -v /etc/shlookup

	echo "======"

	cp -vf `pwd`/script/shlkup.py /etc/shlookup/
	cp -vf `pwd`/cmd/shlookup /bin/
	chmod 755 /bin/shlookup

else

	echo "Script must be run as root"

fi
