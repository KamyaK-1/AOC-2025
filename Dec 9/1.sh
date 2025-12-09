declare -a xCoordinates
declare -a yCoordinates
largest_area=0

abs(){
    if [ $1 -lt 0 ]; then
        echo $(( -1 * $1 ))
    else
        echo $1
    fi
}
while read -r line;
do
    x=$(echo "$line" | cut -d',' -f1)
    y=$(echo "$line" | cut -d',' -f2)
    for ((i = 0; i < ${#xCoordinates[@]}; i++)); do
        length=$(abs $((x - ${xCoordinates[i]})))
        width=$(abs $((y - ${yCoordinates[i]})))
        current_area=$(( (1 + $length) * (1 + $width) ))
        if [ $current_area -gt $largest_area ]; then
            largest_area=$current_area
        fi
    done
    xCoordinates+=($x)
    yCoordinates+=($y)
done < input.txt

echo $largest_area

