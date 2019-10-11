T(n) = 2 * T(n/2) + n
T(n/2) = 2*T(n/4) + n / 2

T(n) = 2 * (2*T(n/4) + n / 2) + n
T(n) = 4 * T(n/4) + 2n
T(n) = 4 * (2 * T(n/8) + n / 4) + 2n
T(n) = 8 * T(n/8) + 3n
T(n) = 2^3 * T(n/(2^3)) + 3n

T(n) = 2<sup>k</sup> T(n/2<sup>k</sup>) + kn



T(1) = 1

n/2<sup>k</sup> = 1

n = 2<sup>k</sup>

k = log<sub>2</sub>(n)

T(n) = 2<sup>log<sub>2</sub>(n)</sup> T(1) + log<sub>2</sub>(n) n

T(n) = 2<sup>log<sub>2</sub>(n)</sup> + log<sub>2</sub>(n) n

---
y = 2<sup>log<sub>2</sub>(n)</sup>

log<sub>2</sub>(y) = log<sub>2</sub>(2<sup>log<sub>2</sub>(n)</sup>)

log<sub>2</sub>(y) = log<sub>2</sub>(n)  log<sub>2</sub>(2)


log<sub>2</sub>(y) = log<sub>2</sub>(n)

y = 2<sup>log<sub>2</sub>(n)</sup> = n

---
T(n) = n + n log<sub>2</sub>(n)

T(n) = O(n log<sub>2</sub>(n))