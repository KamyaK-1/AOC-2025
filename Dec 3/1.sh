total_joltage=0
while read line
do
    n=${#line}
    r=$(( n - 1 ))
    max_joltage=0
    max_digit=${line:r:1}

    for ((i = ((r-1)) ; i >=0 ; i--)); do
        digit=${line:i:1}
        max_with_given_start=$(( 10*digit + max_digit ))
        if [ ${digit} -gt ${max_digit} ]; then
            max_digit=${digit}
        fi
        if [ ${max_with_given_start} -gt ${max_joltage} ]; then
            max_joltage=${max_with_given_start}
        fi
    done

    total_joltage=$(( total_joltage + max_joltage ))
done < input.txt

echo ${total_joltage}