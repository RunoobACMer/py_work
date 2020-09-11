import math

n = (int)(input())

a = list(map(int, input().split()))
a.insert(0,0)
v = (n + 5) * [0]
ans = 1

for i in range(1, n + 1):
	t = i; cnt = 0
	while v[a[t]] != 1:
		v[a[t]] = 1
		t = a[t]
		cnt += 1
	if (cnt > 0):
		ans = ans * cnt // math.gcd(ans, cnt)
print(ans)

