read n
a=$n
sum=0
count=1
while [ $count -le $a ]
do
    read n
    x=$n
    count=$(($count + 1))
    sum=$(($sum + $x))
done
echo $sum $a | awk '{printf "%.3f", $1/$2 }'
