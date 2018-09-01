for (( ; ; ))
do
	date | nc -uw 1 192.168.15.80 5021
done
