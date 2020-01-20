for f in *.zst
do
name=$(echo "$f" | cut -f 1 -d '.')
echo $name
unzstd -d $f -o ./raw/$name
done

