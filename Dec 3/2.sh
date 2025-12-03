total_joltage=0

get_highest_joltage() {
    local bank=$1
    local n=${#bank}
    declare -a max_joltage
    for ((j = 0 ; j <= 12 ; j++)); do
        max_joltage[j]=0
    done

    for ((i = 0; i < n; i++)); do
        local digit=${bank:i:1}
        for ((j = 12 ; j > 0 ; j--)); do
            local max_with_given_end=$(( 10 * ${max_joltage[j-1]} + digit ))
            if [ ${max_with_given_end} -gt ${max_joltage[j]} ]; then
                max_joltage[j]=${max_with_given_end}
            fi
        done
    done
    total_joltage=$(( total_joltage + ${max_joltage[12]} ))
}

while read line
do
    get_highest_joltage "${line}"
done < input.txt

echo ${total_joltage}