ar=($(cat))
echo ${ar[@]/*[a|A]*/}

