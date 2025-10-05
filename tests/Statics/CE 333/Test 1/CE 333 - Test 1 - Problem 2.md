# Problem #2 — Maximum Supported Weight (Trig/Statics)

**Given.** Two cords meet at point **B** and support a weight $W$.  
- Left cord $AB$ makes $45^\circ$ above the horizontal (up-left).  
- Right cord $CB$ has a 5–12–13 slope: from $B$ to $C$, the horizontal and vertical direction cosines are $\cos\theta=5/13$ and $\sin\theta=12/13$, respectively (up-right).  
- Each cord has an allowable tension of **15 lb** (maximum).

Let the cord tensions be $T_A$ (in $AB$) and $T_C$ (in $CB$). Take $+x$ right and $+y$ up.

## 1) Resolve forces with trigonometry
Unit directions:

$$
\hat u_{AB}=\langle -\cos45^\circ,\ +\sin45^\circ\rangle,\qquad
\hat u_{CB}=\langle \tfrac{5}{13},\ \tfrac{12}{13}\rangle.
$$

Equilibrium at the pin $B$:

$$
T_A\hat u_{AB}+T_C\hat u_{CB}-W\,\mathbf j=\mathbf 0
$$

Component equations:

$$
-\,T_A\cos45^\circ+T_C\tfrac{5}{13}=0
\quad\Rightarrow\quad
T_A=\frac{\tfrac{5}{13}}{\cos45^\circ}\,T_C
=\frac{10}{13\sqrt2}\,T_C,
$$

$$
T_A\sin45^\circ+T_C\tfrac{12}{13}-W=0.
$$

Substitute $T_A$ from the first equation into the second:

$$
W=T_A\sin45^\circ+T_C\frac{12}{13}
=\left(\frac{10}{13\sqrt2}\,T_C\right)\sin45^\circ+T_C\frac{12}{13}
=T_C\left(\frac{5}{13}+\frac{12}{13}\right)
=\boxed{\frac{17}{13}T_C}.
$$

Also, from the relation above,

$$
T_C=\frac{13\sqrt2}{10}\,T_A\approx 1.84\,T_A,
$$

so the **right** cord always carries more tension; it will reach its limit first.

## 2) Apply the allowable tension
With $T_C\le15\,\text{lb}$ governing,

$$
W_{\max}=\frac{17}{13}(15)=\boxed{\frac{255}{13}\ \text{lb}\approx 19.62\ \text{lb}}.
$$

(The corresponding $T_A=(10/(13\sqrt2))\,15\approx 8.16\,\text{lb}\le15\,\text{lb}$.)

## 3) Check against the provided answer
Computed: $W_{\max}\approx 19.62\,\text{lb}$.  
Provided: **19.6**.  
**Match?** $\boxed{Yes}$.

**Conclusion:** The **greatest weight** the cords can support without exceeding 15 lb in either cord is **$\approx 19.6\,\text{lb}$**.
