for dir in *;
do
for file in $dir/*;
do;if [[ $file == *.txt ]]
then
cat $file >> "$dir".txt
fi
done
done
