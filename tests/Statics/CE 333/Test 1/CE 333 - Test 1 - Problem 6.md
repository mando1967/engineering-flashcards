
# Problem #6 — Three Cables on Eyebolt (MathJax, fixed delimiters)

**Task.** Find two values of $P$ such that the magnitude of the resultant is $800$.  
(Use one unit system consistently; here all forces are treated as pounds.)

## Resolve the known cable forces
- $1000$ acting along a $3:4:5$ direction (up-left).  
  Components: $F_{1000,x}=-1000\,(3/5)=-600$, $\;F_{1000,y}=+1000\,(4/5)=+800$.
- $400$ at $30^\circ$ below the $-x$ axis (i.e., at $210^\circ$ from $+x$).  
  Components: $F_{400,x}=-400\cos 30^\circ=-346.410$, $\;F_{400,y}=-400\sin 30^\circ=-200$.
- $P$ acts along $+x$: $F_{P,x}=P$, $F_{P,y}=0$.

Vertical sum (independent of $P$):

$$
\sum F_y = 800 - 200 = 600.
$$

## Enforce the resultant magnitude
The resultant must satisfy

$$
(\sum F_x)^2 + (\sum F_y)^2 = 800^2.
$$

Since $\sum F_y=600$, the required horizontal component magnitude is

$$
\big\lvert \sum F_x \big\rvert
= \sqrt{800^2-600^2}
= 529.150.
$$

But

$$
\sum F_x = P + (-600) + (-346.410) = P - 946.410.
$$

Therefore

$$
P - 946.410 = \pm 529.150.
$$

## Solutions for $P$

$$
\boxed{P_1 = 946.410 + 529.150 = 1475.560 \approx 1475}
\qquad
\boxed{P_2 = 946.410 - 529.150 = 417.260 \approx 417}
$$

**Check:** For either $P$, $\sqrt{(\sum F_x)^2 + 600^2}=800$.
