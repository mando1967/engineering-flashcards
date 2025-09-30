# Quiz Wizard - Educational Resource Guide

This guide provides curated learning resources and explanations for common physics/engineering topics covered in the quizzes.

## How to Add Resources to Flashcards

Add these lines after the answer in your flashcard files:

```
[RESOURCE:Type] URL
```

---

## Capacitors & Capacitance

**Key Concepts:**
- Capacitors store energy in electric fields between conductors
- Capacitance C = ε₀A/d (parallel plates)
- Energy stored: U = ½CV² = ½Q²/C
- Q = CV relationship

**Resources:**
- [RESOURCE:Khan Academy - Capacitors] https://www.khanacademy.org/science/physics/circuits-topic/circuits-with-capacitors/v/capacitors-and-capacitance
- [RESOURCE:Video - How Capacitors Work] https://www.youtube.com/watch?v=X4EUwTwZ110
- [RESOURCE:Article - Capacitor Basics] https://www.electronics-tutorials.ws/capacitor/cap_1.html

---

## Batteries & Electrochemistry

**Key Concepts:**
- Chemical energy → electrical energy
- Two different metals (electrodes) + electrolyte
- Voltage depends on electrode materials
- Internal resistance causes voltage drop under load

**Resources:**
- [RESOURCE:Video - How Batteries Work] https://www.youtube.com/watch?v=9OVtk6G2TnQ
- [RESOURCE:Article - Battery Basics] https://www.electronics-tutorials.ws/battery/battery_1.html
- [RESOURCE:Khan Academy - Batteries] https://www.khanacademy.org/science/chemistry/oxidation-reduction/galvanic-voltaic-cells/v/electrochemistry-galvanic-cells

---

## Electric Potential & Voltage

**Key Concepts:**
- Voltage V = W/q (work per unit charge)
- Potential difference is path-independent
- 1 Volt = 1 Joule/Coulomb
- Equipotential surfaces: no work to move charge along them

**Resources:**
- [RESOURCE:Khan Academy - Electric Potential] https://www.khanacademy.org/science/physics/electric-charge-electric-force-and-voltage/electric-potential-voltage/v/electric-potential-at-a-point-in-space
- [RESOURCE:Video - Voltage Explained] https://www.youtube.com/watch?v=z8qfhFXjsrw
- [RESOURCE:Article - Potential Difference] https://www.physicsclassroom.com/class/circuits/Lesson-1/Electric-Potential-Difference

---

## Electric Current & Charge

**Key Concepts:**
- Current I = Q/t (charge flow rate)
- 1 Ampere = 1 Coulomb/second
- Conventional current: positive charge flow direction
- Current density J = I/A

**Resources:**
- [RESOURCE:Khan Academy - Electric Current] https://www.khanacademy.org/science/physics/circuits-topic/circuits-resistance/v/circuits-part-1
- [RESOURCE:Video - Current and Charge] https://www.youtube.com/watch?v=8jB6hDUqN0Y
- [RESOURCE:Article - Current Flow] https://www.electronics-tutorials.ws/dccircuits/dcp_2.html

---

## Kirchhoff's Laws

**Key Concepts:**
- **KCL (Current Law):** Sum of currents into junction = sum out
- **KVL (Voltage Law):** Sum of voltages around loop = 0
- Based on conservation of charge and energy
- Essential for circuit analysis

**Resources:**
- [RESOURCE:Khan Academy - Kirchhoff's Laws] https://www.khanacademy.org/science/physics/circuits-topic/circuits-with-resistors/v/ee-kirchhoffs-current-law
- [RESOURCE:Video - KCL Explained] https://www.youtube.com/watch?v=9lZNB-8dHRk
- [RESOURCE:Video - KVL Explained] https://www.youtube.com/watch?v=3H6Rttqx0Yw
- [RESOURCE:Article - Circuit Analysis] https://www.electronics-tutorials.ws/dccircuits/dcp_4.html

---

## Resistance & Ohm's Law

**Key Concepts:**
- Ohm's Law: V = IR
- Resistance R = ρL/A (material, geometry)
- Power: P = VI = I²R = V²/R
- Resistors in series: R_total = R₁ + R₂ + ...
- Resistors in parallel: 1/R_total = 1/R₁ + 1/R₂ + ...

**Resources:**
- [RESOURCE:Khan Academy - Ohm's Law] https://www.khanacademy.org/science/physics/circuits-topic/circuits-resistance/v/circuits-part-2
- [RESOURCE:Video - Resistance] https://www.youtube.com/watch?v=VnnfDzGLY8g
- [RESOURCE:Article - Ohm's Law] https://www.electronics-tutorials.ws/dccircuits/dcp_2.html

---

## RC Circuits

**Key Concepts:**
- Time constant τ = RC
- Charging: Q(t) = Q_max(1 - e^(-t/τ))
- Discharging: Q(t) = Q_max·e^(-t/τ))
- Voltage and current follow similar exponential curves

**Resources:**
- [RESOURCE:Article - RC Circuits] https://www.electronics-tutorials.ws/rc/rc_1.html
- [RESOURCE:Video - Capacitor Discharge] https://www.youtube.com/watch?v=9g9LkgY_5Hs
- [RESOURCE:Khan Academy - RC Circuits] https://www.khanacademy.org/science/physics/circuits-topic/circuits-with-capacitors/v/ee-circuits-with-capacitors

---

## Circuit Protection (Fuses & Breakers)

**Key Concepts:**
- Fuses must be in series with protected circuit
- Melt when current exceeds rating
- One-time use (must be replaced)
- Circuit breakers are resettable

**Resources:**
- [RESOURCE:Article - Circuit Protection] https://www.electronics-tutorials.ws/io/io_6.html
- [RESOURCE:Video - Fuses and Breakers] https://www.youtube.com/watch?v=YZRjVnZJZGw

---

## Series vs Parallel Circuits

**Key Concepts:**
- **Series:** Same current, voltages add
- **Parallel:** Same voltage, currents add
- Series increases total resistance
- Parallel decreases total resistance

**Resources:**
- [RESOURCE:Khan Academy - Series and Parallel] https://www.khanacademy.org/science/physics/circuits-topic/circuits-with-resistors/v/ee-series-resistors
- [RESOURCE:Video - Series vs Parallel] https://www.youtube.com/watch?v=VV3dUKVcNPo
- [RESOURCE:Article - Circuit Configurations] https://www.electronics-tutorials.ws/resistor/res_4.html

---

## Power in Circuits

**Key Concepts:**
- Power P = VI = I²R = V²/R
- Energy = Power × Time
- 1 Watt = 1 Joule/second
- Power dissipated in resistors becomes heat

**Resources:**
- [RESOURCE:Khan Academy - Electric Power] https://www.khanacademy.org/science/physics/circuits-topic/circuits-resistance/v/circuits-part-3
- [RESOURCE:Video - Electrical Power] https://www.youtube.com/watch?v=FhwlfPMJgm4
- [RESOURCE:Article - Power Calculations] https://www.electronics-tutorials.ws/dccircuits/dcp_3.html

---

## Internal Resistance

**Key Concepts:**
- Real batteries have internal resistance r
- Terminal voltage: V = ε - Ir
- Power lost internally: P = I²r
- Affects battery performance under load

**Resources:**
- [RESOURCE:Article - Internal Resistance] https://www.electronics-tutorials.ws/battery/battery_4.html
- [RESOURCE:Video - Battery Internal Resistance] https://www.youtube.com/watch?v=YZRjVnZJZGw

---

## Measurement Instruments

**Key Concepts:**
- **Voltmeter:** Measures voltage, connected in parallel, high resistance
- **Ammeter:** Measures current, connected in series, low resistance
- Ideal meters don't affect circuit
- Real meters have finite resistance

**Resources:**
- [RESOURCE:Article - Meters] https://www.electronics-tutorials.ws/meter/meter_1.html
- [RESOURCE:Video - Using Multimeters] https://www.youtube.com/watch?v=TdUK6RPdIrA

---

## Tips for Adding Resources

1. **Copy the [RESOURCE:...] line** from this guide
2. **Paste after the Answer:** in your flashcard
3. **Add 1-3 resources** per question (don't overload)
4. **Mix formats:** Videos for visual learners, articles for detailed reading
5. **Use Khan Academy** for comprehensive explanations
6. **YouTube** for quick visual demonstrations

## Example Flashcard Format

```
1. (3 points) Question text here
(a) option a
(b) option b
(c) option c	Answer: (c) option c
Explanation: Brief explanation of the concept.
[RESOURCE:Khan Academy - Topic] https://khanacademy.org/...
[RESOURCE:Video - Topic Explained] https://youtube.com/...
```

---

*Last Updated: 2025-09-29*
*Quiz Wizard Educational Resources*
