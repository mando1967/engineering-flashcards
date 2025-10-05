# Problem #3 — Find $\mathbf{F}_2$ (Using Trig Notation)

**Given:**  
Two forces $\mathbf{F}_1$ and $\mathbf{F}_2$ act at point A. Their resultant is

$$
\mathbf{F}_R = -100\,\mathbf{k}\ \text{lb}.
$$

We are given: $|\mathbf{F}_1| = 60\ \text{lb}$. From the figure, $\mathbf{F}_1$ is inclined **50° below the horizontal**, and its horizontal projection makes **30°** with the +y axis (measured toward the +x axis). Use the usual right-handed coordinate system with +x to the right, +y forward (to the right in the figure), and +z upward.

**Goal:** Determine the **magnitude** and **coordinate direction angles** (angles between $\mathbf{F}_2$ and the +x, +y, +z axes) of $\mathbf{F}_2$.

---

## Step 1: Resolve $\mathbf{F}_1$ into components using trig

Let the angle below horizontal be $\alpha=50^\circ$ and the azimuth in the horizontal plane from +y toward +x be $\phi=30^\circ$.

- Horizontal magnitude of $\mathbf{F}_1$:
  
$$
F_{1h} = F_1\cos\alpha = 60\cos50^\circ.
$$

- Components of $\mathbf{F}_1$:
  
$$
F_{1x} = F_{1h}\sin\phi = 60\cos50^\circ\sin30^\circ,\\
  F_{1y} = F_{1h}\cos\phi = 60\cos50^\circ\cos30^\circ,\\
  F_{1z} = -F_1\sin\alpha = -60\sin50^\circ.
$$

(Subscript signs: negative $z$ means downward.)

Compute numerically:

- $F_{1h}=60\cos50^\circ\approx 38.5673\ \text{lb}$.
- $F_{1x}\approx 38.5673\sin30^\circ\approx 19.2836\ \text{lb}$.
- $F_{1y}\approx 38.5673\cos30^\circ\approx 33.4002\ \text{lb}$.
- $F_{1z}\approx -60\sin50^\circ\approx -45.9627\ \text{lb}$.

So

$$
\mathbf{F}_1\approx \langle 19.2836,\; 33.4002,\; -45.9627\rangle\ \text{lb}.
$$

---

## Step 2: Use resultant to find $\mathbf{F}_2$

By equilibrium of vectors:

$$
\mathbf{F}_1 + \mathbf{F}_2 = \mathbf{F}_R \,\Rightarrow\, \mathbf{F}_2 = \mathbf{F}_R - \mathbf{F}_1.
$$

Given $\mathbf{F}_R=\langle 0,0,-100\rangle$ lb, we get component-wise:

$$
F_{2x} = 0 - F_{1x} = -19.2836\ \text{lb},\\
F_{2y} = 0 - F_{1y} = -33.4002\ \text{lb},\\
F_{2z} = -100 - F_{1z} = -100 - (-45.9627) = -54.0373\ \text{lb}.
$$

Thus

$$
\mathbf{F}_2\approx \langle -19.2836,\; -33.4002,\; -54.0373\rangle\ \text{lb}.
$$

---

## Step 3: Magnitude of $\mathbf{F}_2$

$$
|\mathbf{F}_2| = \sqrt{F_{2x}^2 + F_{2y}^2 + F_{2z}^2}
\approx \sqrt{(-19.2836)^2 + (-33.4002)^2 + (-54.0373)^2}
\approx 66.39\ \text{lb}.
$$

(Keep a few more digits if needed: **66.389** lb.)

---

## Step 4: Coordinate direction angles of $\mathbf{F}_2$

Coordinate direction angles are the angles between $\mathbf{F}_2$ and the +x, +y, +z axes, denoted $\alpha_x,\alpha_y,\alpha_z$. They satisfy

$$
\cos\alpha_x = \frac{F_{2x}}{|\mathbf{F}_2|},\quad
\cos\alpha_y = \frac{F_{2y}}{|\mathbf{F}_2|},\quad
\cos\alpha_z = \frac{F_{2z}}{|\mathbf{F}_2|}.
$$

Compute the angles (in degrees):

- $\alpha_x = \cos^{-1}\left(\dfrac{-19.2836}{66.389}\right) \approx 106.89^\circ.$
- $\alpha_y = \cos^{-1}\left(\dfrac{-33.4002}{66.389}\right) \approx 120.21^\circ.$
- $\alpha_z = \cos^{-1}\left(\dfrac{-54.0373}{66.389}\right) \approx 144.48^\circ.$

(Angles > 90° indicate the vector points having negative components relative to the positive axes.)

---

## ✅ Final Answers

- $\mathbf{F}_2\approx \langle -19.28,\; -33.40,\; -54.04\rangle\ \text{lb}.$
- Magnitude: $|\mathbf{F}_2|\approx 66.39\ \text{lb}.$
- Coordinate direction angles:
  - $\alpha_x\approx 106.89^\circ$  
  - $\alpha_y\approx 120.21^\circ$  
  - $\alpha_z\approx 144.48^\circ$

If you want, I can append this solution into your main canvas document (so Problems #1–#3 appear in a single file) or export any document as a `.md` or `.pdf` file.
