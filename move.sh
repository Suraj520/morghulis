srce="/mnt/f084d510-e9ee-4344-ab0a-6811dadadb19/DL/Temp/morghulis/datasets/widerface/darknet/images/"
trgt="/mnt/f084d510-e9ee-4344-ab0a-6811dadadb19/DL/Temp/morghulis/datasets/widerface/darknet/Images/"

shopt -s nullglob dotglob

mkdir -p -- "$trgt" || exit 1

# in case trgt is relative
cd -- "$trgt" || exit 1
trgt="$PWD"
cd -- "$OLDPWD" || exit 2

cd -- "$srce" || exit 2

find . -maxdepth 3 ! -type d -exec cp -t "$trgt" -- {} +

for d in ./*; do
   [ -d "$d" ] && mkdir -p -- "$trgt/$d" \
   && find "$d" ! -type d -exec cp -t "$trgt/$d" -- {} +
done
