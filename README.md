# Fuzzy-logic-Implementation
This repo is associated with speed control of vehicle through fuzzy logic. It's a merely tutorial based repo in which fuzzy logic has been implemented. The code implements a classic Mamdani-type FLC pipeline, but with a closed-form (geometric) shortcut for defuzzification instead of numerical integration.

### Linguistic variable levels (used for SD = speed difference , A = Accelerator, and TC= Throttle Control):

```

Abbrev.	    Full form
NL	     Negative Large
NM	     Negative Medium
NS	     Negative Small
ZE	     Zero
PS	     Positive Small
PM	     Positive Medium
PL	     Positive Large

```

MF = Membership Function — the curve (triangular, open-left, or open-right in this case) that defines how strongly a crisp value belongs to one of the above fuzzy sets, with degree between 0 and 1.

So, for example, "SD is NL" means the speed difference falls into the "Negative Large" fuzzy region, and the degree to which it does is given by that set's membership function (here, the open-left shape with a=30, b=60).

<img width="1263" height="588" alt="image" src="https://github.com/user-attachments/assets/c607113a-a3f1-41ce-9b94-4b5f9c24adf8" />

### Rules: 
Translating the fuzzy labels into vehicle-control logic (SD = speed difference from target, A = acceleration, TC = throttle control)
<img width="1098" height="442" alt="image" src="https://github.com/user-attachments/assets/7a5c116b-5551-488a-8c6e-5f507419c0ee" />

### Pipeline
<img width="600" height="620" alt="image" src="https://github.com/user-attachments/assets/9c5456d9-1532-456e-93f6-5025a604cb8c" />

That's the full pipeline code implements. A quick recap of the key equation at each stage:

- Fuzzification — apply the shoulder/triangular formulas to SD and A.
- Rule evaluation — min for AND within a rule, max (via compare()) across rules sharing a consequent.
- Aggregation — each active output set gets clipped at its firing strength 𝜇
  and its exact area is computed geometrically (trapezoid formulas above) rather than by numerical integration.
- Defuzzification — weighted average of over all active output sets:

### Finidng x1 and x2 for triangular area :
<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/d5a5b461-d4a7-4032-b338-ca0487fb3284" />

### Finding Open left area :
<img width="650" height="500" alt="image" src="https://github.com/user-attachments/assets/5d69cd53-4974-4fd8-9ca0-0421b30b3f5c" />

### Finding Open right area: 
<img width="650" height="500" alt="image" src="https://github.com/user-attachments/assets/e5567f3e-340a-44ff-94a4-c0d9bbd20765" />



### Equation to find crisp value from fuzzy value (Defuzzification equation)
<img width="500" height="90" alt="image" src="https://github.com/user-attachments/assets/2331029f-61d5-4474-9b70-f75111ae29a9" />


