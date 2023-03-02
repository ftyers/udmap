for line in $(cat releases.tsv | grep -v "^#" | sed "s/\t/#/g"); do 
	url=$(echo "${line}" | cut -f2 -d'#');
	version=$(echo "${line}" | cut -f1 -d'#');
	echo "${version} ${url}" >> /dev/stderr;
	
	wget -q -O - "${url}?show=full" | xmllint --html --format - | grep 'DC.language' | cut -f4 -d'"'  | sort | sed "s/^/${version}\t/g"
done
