
while IFS= read -r line; do
  printf 'scheduling for %s\n' "$line"
  at -f ../gpAutoTakePhoto.sh "$line"
done < <(python3 Timer.py)



