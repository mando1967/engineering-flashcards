# Problem #5 — Moments of **F** in 3D (Trig/D.C. method)

We’ll use right-handed axes with unit vectors $\mathbf i,\mathbf j,\mathbf k$ along $x,y,z$. Distances are in **m**, forces in **N**, moments in **N·m**.  

Given force at **B**:  

$$
\mathbf F=\langle 80,-40,-120\rangle\ \text{N} = 80\,\mathbf i-40\,\mathbf j-120\,\mathbf k.
$$

## Geometry (from the figure)

$$

$$
\begin{aligned}
O&=(0,0,0),\\
C&=(0,0,0.6),\\
A&=(0.8,0,0.6),\\
B&=(0.8,0.3,0.6).
\end{aligned}
$$

$$

---

## 1) Moment of $\mathbf F$ about **point C** (Cartesian vector)

Use $\mathbf M_C=\mathbf r_{CB}\times \mathbf F$, where $\mathbf r_{CB}=\overrightarrow{CB}=B-C$.

$$
\mathbf r_{CB}=\langle 0.8,\,0.3,\,0\rangle.
$$

Cross product (determinant form):

$$

$$
\begin{aligned}
\mathbf M_C
&=\begin{vmatrix}
\mathbf i & \mathbf j & \mathbf k\\
0.8&0.3&0\\
80&-40&-120
\end{vmatrix}\\[2mm]
&=(-36)\,\mathbf i + (96)\,\mathbf j + (-56)\,\mathbf k.
\end{aligned}
$$

$$

$$
\boxed{\;\mathbf M_C=\langle -36,\ 96,\ -56\rangle\ \text{N·m}\;}
$$

---

## 2) Moment of $\mathbf F$ about the **x-axis**

Moment about an axis = projection of the moment vector about some point on that axis onto the axis’ unit vector.  
Take point $O$ (on the $x$-axis). First get $\mathbf M_O=\mathbf r_{OB}\times \mathbf F$ with $\mathbf r_{OB}=B-O=\langle 0.8,0.3,0.6\rangle$.

$$

$$
\begin{aligned}
\mathbf M_O
&=\begin{vmatrix}
\mathbf i & \mathbf j & \mathbf k\\
0.8&0.3&0.6\\
80&-40&-120
\end{vmatrix}
=(-12)\,\mathbf i + (144)\,\mathbf j + (-56)\,\mathbf k.
\end{aligned}
$$

$$

Unit vector of the $x$-axis is $\mathbf e_x=\mathbf i$. Hence

$$
\boxed{\;M_{x}=\mathbf M_O\cdot \mathbf e_x = -12\ \text{N·m}\;}
$$

(negative sign = clockwise about +$x$ by the right-hand rule).

---

## 3) Moment of $\mathbf F$ about the axis from **O** to **A**

Axis direction $\overrightarrow{OA}=A-O=\langle 0.8,0,0.6\rangle$.  
Use **direction cosines** (a trig idea) to form the unit vector:

$$
\|\overrightarrow{OA}\|=\sqrt{0.8^2+0^2+0.6^2}=1
\ \Rightarrow\ 
\mathbf e_{OA}=\langle \cos\alpha_x,\cos\alpha_y,\cos\alpha_z\rangle
=\left\langle \frac{0.8}{1},\,0,\,\frac{0.6}{1}\right\rangle
=\langle 0.8,0,0.6\rangle.
$$

Moment about the $OA$ axis is the scalar projection of $\mathbf M_O$ onto $\mathbf e_{OA}$:

$$
M_{OA} = \mathbf M_O\cdot \mathbf e_{OA}
= \langle -12,144,-56\rangle\cdot \langle 0.8,0,0.6\rangle
= (-12)(0.8) + (144)(0) + (-56)(0.6)
= \boxed{-43.2\ \text{N·m}}.
$$

(Negative means the sense is opposite the right‑hand rule about the axis directed from $O$ to $A$.)

---

## Final results
- $\displaystyle \mathbf M_C=\boxed{\langle -36,\ 96,\ -56\rangle\ \text{N·m}}$ (Cartesian vector).  
- $\displaystyle M_x=\boxed{-12\ \text{N·m}}$.  
- $\displaystyle M_{OA}=\boxed{-43.2\ \text{N·m}}$ about the axis $O\to A$.
