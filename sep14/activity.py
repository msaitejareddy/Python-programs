message='the recommended activity is:'
print('enter temperature')
temp=int(input())

if temp>85:
	message=message +'swimming'
elif temp>70:
	message=message +'play cricket'
elif temp>65:
	message=message +'do chicken BBQ'
else:
        message=message +'put chali manta'
print(message)
