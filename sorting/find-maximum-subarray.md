# Maximum Subarray

## Algorithm for Maximum Subarray
---
```
find-maximum-subarray(A, low, high)
 1|if low == high
 2|    return (low, high, A[low]) // base-case:only one element
 3|else
 4|    mid = floor((low + high) / 2)
 5|    (left-low, left-high, left-sum) =
 6|        find-maximum-subarray(A, low, mid)
 7|    (right-low, right-high, right-sum) =
 8|        find-maximum-subarray(A, mid + 1, high)
 9|    (cross-low, cross-high, cross-sum) =
10|        find-max-crossing-subarray(A, low, mid, high)
11|    if left-sum >= right-sum and left-sum >= cross-sum)
12|        return(left-low, left-high, left-sum)
13|    
14|    if right-sum >= left-sum and right-sum >= cross-sum
15|        return(right-low, right-high, right-sum)
16|    
17|    else
18|        return(cross-low, cross-high, cross-sum)
```

## Dry run

```
A = [1, 2, 5, 8, -1, 5, 4, -1, 6, 9, -13]

max-subar(A, 0, 10)
    low = 0
    high = 10

    mid = floor((0 + 10)/2) = 5

    ---># 5: max-subar(A, 0, 5)
        low = 0
        high = 5

        mid = floor((0 + 5)/2) = 2

        ---># 5: max-subar(A, 0, 2)
            low = 0
            high = 2

            mid = floor((0 + 2)/2) = 1

            ---># 5: max-subar(A, 0, 1)
                low = 0
                high = 1

                mid = floor((0 + 1)/2) = 0
                
                ---># 5: max-subar(A, 0, 0)
                    low = 0
                    high = 0
                <--- (0, 0, 1)
                left-low = 0
                left-high = 0
                left-sum = 1
                ---># 7: max-subar(A, 1, 1)
                    low = 1
                    high = 1 
                <--- (1, 1, 2)
                right-low = 1
                right-high = 1
                right-sum = 2
                ---># 9: max-cross-subar(A, 0, 0, 1)
                    left-sum = 1
                    sum = 0

                    i = 0
                    sum = 1
                    max-left = 0

                    right-sum = 2
                    sum = 0

                    j = 1
                    sum = 2
                    max-right = 1
                <--- (0, 1, 3)
                cross-low = 0
                cross-high = 1
                cross-sum = 3
                
            <--- (0, 1, 3)
            left-low = 0
            left-high = 1
            left-sum = 3
            ---># 7: max-subar(A, 2, 2)
                low = 2
                high = 2

            <--- (2, 2, 5)
            right-low = 2
            right-high = 2
            right-sum = 5
            ---># 9: max-cross-subar(A, 0, 1, 2)
                left-sum = 3

                i = 0
                sum = 3
                max-left = 0

                right-sum = 5

                j = 2
                sum = 5
                max-right = 2

            <--- (0, 2, 8)
            cross-low = 0
            cross-high = 2
            cross-sum = 8
        <--- (0, 2, 8)
        left-low = 0
        left-high = 2
        left-sum = 8
        ---># 7: max-subar(A, 3, 5)
            low = 3
            high = 5

            mid = floor((3 + 5) / 2) = 4
            ---># 5: max-subar(A, 3, 4)
                low = 3
                high = 4

                mid = floor((3 + 4)/ 2) = 3
                ---># 5: max-subar(A, 3, 3)
                    low = 3
                    high = 3
                <--- (3, 3, 8)
                left-low = 3
                left-high = 3
                left-sum = 8
                ---># 7: max-subar(A, 4, 4)
                    low = 4
                    high = 4
                <--- (4, 4, -1)
                right-low = 4
                right-high = 4
                right-sum = -1
                ---># 9: max-cross-subar(A, 3, 3, 4)
                    left-sum = 8

                    i = 3
                    sum = 8
                    max-left = 3

                    right-sum = -1

                    j = 4
                    sum = -1
                    max-right = 4

                <--- (3, 4, 7)
                cross-low = 3
                cross-high = 4
                cross-sum = 7
            <--- (3, 3, 8)
            left-low = 3
            left-high = 3
            left-sum = 8
            ---># 7: max-subar(A, 5, 5)
                low = 5
                high = 5
            <--- (5, 5, 5)
            right-low = 5
            right-high = 5
            right-sum = 5
            ---># 9: max-cross-subar(A, 3, 4, 5)
                left-sum = 7

                i = 3
                sum = 7
                max-left = 3

                right-sum = 5

                j = 5
                sum = 5
                max-right = 5
            <--- (3, 5, 12)
            cross-left = 3
            cross-right = 5
            cross-sum = 12
        <--- (3, 5, 12)
        right-low = 3
        right-high = 5
        right-sum = 12
        ---># 9: max-cross-subar(A, 0, 2, 5)
            left-sum = 8
            
            i = 0
            sum = 8
            max-left = 0

            right-sum = 12

            j = 5
            sum = 12
            max-right = 5
        <--- (0, 5, 20)
        cross-low = 0
        cross-high = 5
        cross-sum = 20
    <--- (0, 5, 20)
    left-low = 0
    left-high = 5
    left-sum = 20

    ---># 7: max-subar(A, 6, 10)
        low = 6
        high = 10

        mid = floor((6 + 10)/2) = 8
        ---># 5: max-subar(A, 6, 8)
            low = 6
            high = 8

            mid = floor((6 + 8)/2) = 7
            ---># 5: max-subar(A, 6, 7)
                low = 6
                high = 7
                
                mid = 6
                ---># 5: max-subar(A, 6, 6)
                    low = 6
                    high = 6
                <--- (6, 6, 4)
                left-low = 6
                left-high = 6
                left-sum = 4
                ---># 7: max-subar(A, 7, 7)
                    low = 7
                    high = 7
                <--- (7, 7, -1)
                right-low = 7
                right-high = 7
                right-sum = -1
                ---># 9: max-cross-subar(A, 6, 7, 8)
                    left-sum = 3

                    i = 6
                    sum = 3
                    max-left = 6

                    right-sum = 6

                    j = 8
                    sum = 6
                    max-right = 8
                <---(6, 8, 9)
                cross-left = 6
                cross-right = 8
                cross-sum = 9
            <--- (6, 8, 9)
            left-low = 6
            left-high = 8
            left-sum = 9
            ---># 7: max-subar(A, 8, 8)
                left = 8
                high = 8
            <--- (8, 8, 6)
            right-low = 8
            right-high = 8
            right-sum = 6
            ---># 9: max-cross-subar(A, 6, 7, 8)
                left-sum = 3

                i = 6
                sum = 3
                max-left = 7

                right-sum = 6

                j = 8
                sum = 6
                max-right = 8
            <--- (7, 8, 9)
            cross-low = 7
            cross-high = 8
            cross-sum = 9
        <--- (6, 8, 9)
        left-low = 6
        left-high = 8
        left-sum = 9
        ---># 7: max-subar(A, 9, 10)
            low = 9
            high = 10

            mid = 9
            ---># 5: max-subar(A, 9, 9)
                low = high = 9
            <--- (9, 9, 9)
            left-low = 9
            left-high = 9
            left-sum = 9
            ---># 7: max-subar(A, 10, 10)
                low = high = 10
            <--- (10, 10, -13)
            right-low = 10
            right-high = 10
            right-sum = -13
            ---># 9: max-cross-subar(A, 9, 9, 10)
                left-sum = 9

                i = 9
                sum = 9
                max-left = 9

                right-sum = -13

                j = 10
                sum = -13
                max-right = 10
            <--- (9, 10, -4)
            cross-low = 9
            cross-high = 10
            cross-sum = -4
        <--- (9, 9, 9)
        right-low = 9
        right-high = 9
        right-sum = 9
        ---># 9: max-cross-subar(A, 6, 8, 10)
            left-sum = 9

            i = 6
            sum = 9
            max-left = 6

            right-sum = 9

            j = 10
            sum = -4
            max-right = 9
        <--- (6, 9, 18)
        cross-low = 6
        cross-high = 9
        cross-sum = 18
    <--- (6, 9, 18)
    right-low = 6
    right-high = 9
    right-sum = 18
    ---># 9: max-cross-subar(A, 0, 5, 10)
        left-sum = 20

        i = 0
        sum = 20
        max-left = 0

        right-sum = 18

        j = 10
        sum = 5
        max-right = 9
    <--- (0, 9, 38)
    cross-low = 0
    cross-high = 9
    cross-sum = 38
<--- (0, 9, 38)

```