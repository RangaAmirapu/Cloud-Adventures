read X
read Y
read Z

if [ $X -eq $Y ] && [ $Y -eq $Z ]
then
 echo EQUILATERAL
fi

if [ $X -ne $Y ] && [ $X -ne $Z ] && [ $Y -ne $Z ]
then
 echo SCALENE
fi

if [ $X -eq $Y ] || [ $X -eq $Z ] || [ $Y -eq $Z ]
then
  if  [ $X -ne $Y ] || [ $X -ne $Z ]
  then
    echo ISOSCELES
  fi 
fi

