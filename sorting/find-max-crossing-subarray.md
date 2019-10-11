# Find Maximum Crossing Subarray

## Algorithm for find-max-crossing-subarray

```
maximum-crossing-subarray(A, low, mid, high)
left-sum = -infinity
sum = 0

for i = mid downto low # theta(n/2)
    sum = sum + A[i]
    if sum > left-sum
        left-sum = sum
        max-left = i

right-sum = -infinity
sum = 0
for j = mid + 1 to high # theta(n/2)
    sum = sum + A[j]
    if sum > right-sum
        right-sum = sum
        max-right = j

return(max-left, max-right, left-sum + right-sum)
```

## dry run
```
A = [1, 2, 5, 8, -1, 5, 4, -1, 6, 9, -13]

left-sum = 20
n = 11
mid = n // 2 = 11 // 2 = 5

i = 0
A[i] = 1
sum = 20
max-left = 0


right-sum = 18

j = 10
A[j] = -13
sum = 5
max-right = 9

return (0, 9, 38)
```
