<p align="center"><img src="images/banner/banner.jpg" width="100%"></p>

<p align="center">
<img src="https://img.shields.io/badge/Siemens%20STAR--CCM%2B-1c2434?style=for-the-badge" alt="Siemens STAR-CCM+">
<img src="https://img.shields.io/badge/ANSYS%20Fluent-1c2434?style=for-the-badge" alt="ANSYS Fluent">
<img src="https://img.shields.io/badge/SOLIDWORKS-1c2434?style=for-the-badge&logo=dassaultsystemes&logoColor=white" alt="SOLIDWORKS">
<img src="https://img.shields.io/badge/Python-1c2434?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/CFRP%20composites-1c2434?style=for-the-badge" alt="CFRP composites">
</p>

# Formula Student Aerodynamic Package — TUFF-XVIII (2026)

**Team Fateh Racing, Thapar Institute of Engineering & Technology**
Aerodynamics Lead (Jul 2025 – present) · Aerodynamicist (Oct 2023 – Jul 2025)
Formula Bharat & Supra SAE 2026 · **Supra SAE 2026: P3 overall, P2 Engineering Design Report**

I led a 4-person aerodynamics sub-team that delivered Team Fateh's **first complete aerodynamic package**: front wing, rear wing, side wings, whiskers and nosecone. It took the car from essentially no downforce to **397 N at 10 m/s at a downforce-to-drag ratio of 3.6**, and in lap-time simulation it moved the car from podium to first in skidpad, autocross and endurance.

<p align="center"><img src="images/car/complete_aero_package_fitted_formula_bharat_2026.jpg" width="31%"> <img src="images/car/side_wings_and_bodywork.jpg" width="66%"></p>

### My role
- Led the 4-person aero sub-team: set the targets, chose the concept (wings over an undertray), and owned the CFD process and sign-off.
- Designed the rear wing, side wings, front wing, whiskers and nosecone in SOLIDWORKS; ran 45+ full-car and component CFD iterations.
- Built the team's first aeromaps and handed aero coefficients to the vehicle-dynamics group for lap-time simulation.
- Wrote the Python tool that rebuilds the Benzing rear-wing profiles, and took the parts through mould design and composite manufacture.

| Area | Tools |
|---|---|
| CAD | SOLIDWORKS |
| CFD | Siemens STAR-CCM+, ANSYS Fluent (RANS, k-ω SST) |
| Profiles & scripting | Python (NumPy, SciPy, Matplotlib) |
| Manufacturing | CFRP resin infusion, vacuum bagging, wet layup, aluminium honeycomb, 3D printing |

**Contents:** [Headline results](#headline-results) · [Why aero](#1-why-aero-on-a-formula-student-car) · [Design targets](#2-design-targets) · [Concept selection](#3-concept-selection) · [Components](#4-components) · [CFD methodology](#5-cfd-methodology) · [Attitude sweeps & aeromaps](#6-attitude-sweeps--aeromaps) · [Lap-time simulation](#7-lap-time-simulation) · [Manufacturing](#8-manufacturing) · [CAD](#cad) · [Code](#code)

---

## Headline results

| Full car @ 10 m/s (Siemens STAR-CCM+, k-ω SST) | |
|---|---|
| Downforce | **397.3 N** |
| Drag | 110.9 N |
| Downforce / drag | **3.58** (target ≥ 3) |
| Centre of pressure | 46.7 % from the front, **3.3 % rearward of CG** (target: within 10 %) |
| Design iterations | 45+ |

| Component | Downforce @ 10 m/s | Efficiency |
|---|---|---|
| Rear wing | 160 N | C<sub>L</sub>/C<sub>D</sub> > 2.8 |
| Front wing + whiskers | 90 N | C<sub>L</sub>/C<sub>D</sub> > 2 |
| Side wings | 70 N | C<sub>L</sub>/C<sub>D</sub> > 2 |

<p align="center"><img src="images/cfd/full_car_system_simulated_in_starccm.jpg" width="95%"></p>

---

## 1. Why aero on a Formula Student car

Formula Bharat tracks are tight and corner-dominated: short straights, slaloms, hairpins and constant-radius turns. Lap time is set mostly by **cornering speed**, and cornering speed is limited by how much lateral force the tyres can make, which depends on the vertical load on them.

From MRF's load-sensitivity data for the ZTD-1 tyre, grip peaks at about **1800 N of vertical load per wheel**. Without aero the car produced only about 825 N of total downforce, leaving roughly **975 N of unused vertical load** at the tyres' optimum. Downforce closes that gap without adding the mass that extra load would otherwise cost.

The trade-off is drag, plus added mass, a higher CG and higher polar inertia from the wings. The package had to win back more in the corners than it lost on the straights.

## 2. Design targets

- **Downforce / drag ≥ 3.** In lap-time simulation, efficiencies near 3 met the team's lap-time goals.
- **Centre of pressure within 10 % rearward of CG.** A CoP slightly behind the CG gives a restoring yaw moment. Too far back and the rear gains load faster than the front with speed, causing understeer.
- **Reliable behaviour in yaw**, since the car spends most of a lap cornering.
- **Weight-to-performance:** the gains have to outweigh the added mass and inertia.
- **All CFD at 10 m/s.** That's representative of Formula Bharat speeds, and a package that works at 10 m/s only gets stronger with speed (forces scale with V²).

<p align="center"><img src="images/design_process.jpg" width="55%"></p>

## 3. Concept selection

**Undertray rejected.** In symmetric flow the undertray reached C<sub>L</sub> ≈ 4.6, but at 15° yaw that fell to about 1.9, a **58 % loss**. It was running close to separation and was very sensitive to ride height, pitch and yaw. The multi-element rear wing went from C<sub>L</sub> 4.20 at 0° yaw to 3.46 at 15° (under 18 %). So the package was built around **wings that hold their downforce over a whole lap** rather than an undertray with a higher peak.

**Drag-limit check** (McBeath's power-limited method):
- Available power is 35 kW. The clean body needs 6.48 kW at a capped top speed of 30 m/s, which leaves 28.5 kW for the aero devices.
- That puts the **allowable drag area at 1.72 m²**.
- The full package came out at **1.65 m²**, so the car is not power-limited at 30 m/s.

## 4. Components

### Nosecone
The nose sees the highest stagnation pressure on the car. The goal was to turn the incoming flow smoothly toward the front wing and whiskers instead of letting pressure build up.

Five iterations went from an initial convex profile to the final shape. Compared with the 2025 prototype:
- **frontal area −14.5 %**, by moving to aluminium honeycomb construction
- **nosecone downforce +35.5 %**
- **full-body drag −29 %**

Over 2023–25, sidepod, nosecone and undertray campaigns cut full-car drag by **more than 40 %**.

<p align="center"><img src="images/sweeps/nosecone_iterations.jpg" width="60%"></p>

### Front wing: FX-76 mainplane + FX-74 flaps
- **Role:** front-axle downforce for turn-in and mid-corner balance, targeted at 20–30 % of total downforce.
- **Airfoils:** I compared multi-element combinations by their pressure distributions.
  - **FX-76 / FX-74** gave smooth pressure recovery, low sensitivity to angle of attack, and flow that stayed attached at high incidence.
  - **CH10-based sets** destabilised the downstream elements.
  - **MSHD-based sets** recovered pressure too aggressively and separated early.
- **Slot gaps and overlaps** started from McBeath's ranges and were then refined in CFD:
  - gap about 3.5 % of mainplane chord, overlap about 5.2 %, convergent slots
  - flap chords 30–40 % of total chord
  - first flap at 25–30° to the mainplane
- **Endplates and footplates** limit spanwise leakage and contain the tip vortex. **Outwashing endplates with an S1223 suction side** push the wake away from the front tyres.

<p align="center"><img src="images/car/front_wing_cad.jpg" width="45%"> <img src="images/cfd/front_wing_slot_flow.jpg" width="25%"></p>

### Whiskers
The front wing's upwash steals flow from the rear wing. The whiskers are **CH10-derived profiles thinned by 70 % with no endplates**, so they turn flow rather than make lift. They redirect the upwash back toward the side and rear elements, **adding 27.5 % to full-car downforce** while costing less than 3 % of total downforce themselves.

### Rear wing: Be 122-185 mainplane + 2 × Be 153-105 flaps
- **Profiles:** I chose Benzing race-car profiles for their stable, low-Reynolds multi-element behaviour, which gave **12–15 % more downforce** than an S1223 + Goe 477 baseline.
  - The **Be 122-185** mainplane gave the most downforce in the 122 series.
  - The **Be 153-105** flaps were the best compromise. The 153-175 added too much drag and vortex strength; the 153-055 didn't add enough load.
  - Usable coordinates aren't published, so I **rebuilt the profiles with my own [Python tool](rear-wing-airfoils)**.
- **Dual cascade (biplane) elements: +22 % downforce.** They add circulation and delay separation across the assembly.
- **Leading-edge slat: +9.5 %.** It re-energises the boundary layer in the roll-hoop wake.
- **Endplate V-cuts, a trailing-edge C-cut and louvres** release the pressure difference and weaken the tip vortex. Drag dropped **60 N → 45.5 N (−24 %)**.
- **10° swept mainplane section.** Tight clearance to the HV/LV enclosures was choking the flow. Sweeping that section fixed it without relocating the wing, and let the wing mount lower.

<p align="center"><img src="images/sweeps/rear_wing_airfoil_combinations.jpg" width="38%"> <img src="images/cfd/rear_wing_wheel_wake.jpg" width="57%"></p>

### Side wings
An **inwashing multi-element assembly with integrated air-dams** sits ahead of the rear wheels and suppresses the rotating-wheel wake:
- rear-wheel drag **−65 %**
- rear-wing performance **+12.5 %**
- centre of pressure **5 % rearward**, toward the balance target

## 5. CFD methodology

| | |
|---|---|
| Solvers | Siemens STAR-CCM+ (primary), ANSYS Fluent |
| Model | Steady, incompressible RANS, **k-ω SST** |
| Geometry | Cleaned bluff body (no fasteners or small details) plus aero devices, checked against the Formula Bharat rule boxes |
| Domain | 3–5 L upstream, 8–10 L downstream, 3 L laterally and vertically; ground tangent to the tyres |
| Boundary conditions | 10 m/s inlet, **moving ground and rotating wheels** |
| Mesh | **Trimmed hex** mesher, chosen over polyhedral and tetrahedral meshes for gap filling and growth control. Local refinement at leading and trailing edges, slots and the wake |
| Near-wall | **y⁺ evaluated per surface**, not assumed globally. y⁺ ≈ 1–3; first prism layer **5.6 × 10⁻⁵ m** (Re ≈ 1.8 × 10⁶ on a 2.2 m car length at 13 m/s); prism stack sized to a 47 mm flat-plate turbulent boundary layer |
| Convergence | Residuals (continuity, momentum, k, ω) and force monitors, about 1000 iterations |
| Post-processing | Pressure and velocity fields, Q-criterion vortex structures, lift and drag along the car length |

<p align="center"><img src="images/cfd/domain_cross_section_with_refinement_regions.jpg" width="49%"> <img src="images/cfd/surface_mesh_and_refinement_full_car_front_view.jpg" width="37%"></p>
<p align="center"><img src="images/cfd/q_criterion.jpg" width="49%"> <img src="images/cfd/velocity_side_with_aero.jpg" width="49%"></p>
<p align="center"><img src="images/cfd/velocity_side_no_aero.jpg" width="60%"><br><sub>Baseline car without aero, for comparison</sub></p>

## 6. Attitude sweeps & aeromaps

A car never runs at its static ride height. Braking, acceleration and cornering pitch, heave, roll and yaw it all the time. I ran **pitch (±5°), roll, ride-height and yaw sweeps** on the wings and full car, which became the team's **first aeromaps** for the vehicle-dynamics group:

- **Ride height:** across front ride heights of 40–80 mm and rear of 20–60 mm, full-car downforce ranged from **270 to 351 N** and efficiency from **1.84 to 2.70**. The most efficient setups are at higher front and rear ride heights, which tells the vehicle-dynamics group which way to tune springs and ride height.
- **Front wing:** strongly sensitive to ride height (ground effect). No abrupt stall across the pitch range. A gradual, predictable loss of C<sub>L</sub> in yaw.
- **Rear wing:** peaks near small nose-up pitch and is mildly sensitive to ride height. **Smooth behaviour in yaw** with no sudden drop, which was the reason for choosing it over an undertray.

<p align="center"><img src="images/sweeps/aeromaps.jpg" width="95%"></p>

<p align="center">
<img src="images/sweeps/front_wing_cl_pitch.jpg" width="32%"> <img src="images/sweeps/front_wing_cl_yaw.jpg" width="32%"> <img src="images/sweeps/front_wing_cl_roll.jpg" width="32%">
<img src="images/sweeps/rear_wing_cl_pitch.jpg" width="32%"> <img src="images/sweeps/rear_wing_cd_pitch.jpg" width="32%"> <img src="images/sweeps/rear_wing_cl_yaw.jpg" width="32%">
</p>

## 7. Lap-time simulation

The package was scored with transient lap-time simulation across the dynamic events, with the aero coefficients from CFD as inputs:

| Event | Without aero | With aero | Change |
|---|---|---|---|
| Acceleration (75 m) | 5.224 s | 5.654 s | +0.43 s (drag penalty) |
| Skidpad | 5.774 s | **5.710 s** | podium → **1st** |
| Autocross | 122.6 s | **107.8 s** | **−12 %**, podium → **1st** |
| Endurance (22 laps) | | | **−17.3 s**, podium → **1st** |
| **Dynamic points (of 575)** | 448.2 | **522.2** | **+74** |

The package deliberately gives up a little straight-line acceleration to win the three cornering-limited events.

<p align="center"><img src="images/sweeps/lap_time_surface.jpg" width="55%"><br><sub>Lap time across downforce and drag coefficients, used to set the efficiency target</sub></p>

## 8. Manufacturing

| Part | Process |
|---|---|
| Front & rear wings | Female moulds designed by the team from the CAD. Wings made by **resin infusion** with a **corrugated core** for stiffness at low mass, then demoulded, trimmed and inspected |
| Nosecone | Fibreglass female mould; **in-house vacuum bagging**, 3-ply carbon layup with epoxy resin; then sanded and finished |
| Bodywork & sidepods | Foam blocks stacked and profiled to the CAD sections, filled and faired into moulds; CFRP **wet layup and vacuum bagging** over **aluminium-honeycomb** sandwich panels |
| Whiskers | 3D-printed with threaded inserts. **Infill and wall thickness chosen from shear tests** of insert pull-out specimens |
| Side wings | **Deflection-tested** before running |

<p align="center">
<img src="images/manufacturing/foam_blocks_stacked_and_profiled_for_sidepod_female_mould.jpg" width="19%"> <img src="images/manufacturing/filler_and_putty_to_smoothen_female_mould_1.jpg" width="19%"> <img src="images/manufacturing/wet_layup_onto_the_nosecone_2025.jpg" width="19%"> <img src="images/manufacturing/vacuum_bag_sealed_over_female_nosecone_mould.jpg" width="19%"> <img src="images/manufacturing/cured_cfrp_nosecone_fitted.jpg" width="19%">
<img src="images/manufacturing/corrugation_for_rear_wing_elements.jpg" width="32%"> <img src="images/manufacturing/3d_printed_whiskers.jpg" width="20%"> <img src="images/manufacturing/deflection_testing_for_side_wings.jpg" width="20%"> <img src="images/manufacturing/nosecone_after_sanding_and_wrapping.jpg" width="20%">
</p>

**Also on the team:** I built a COMSOL thermal model of the HV accumulator (heat generation, cell-array conduction, convective cooling) to keep the tractive system within regulatory limits at peak power (Formula Bharat Pi EV 2024).

---

## CAD

Exports of the 2026 package are in [`cad/`](cad). Each model comes as an STL (click it on GitHub to rotate it in 3D) and a Parasolid `.x_t` (opens in Fusion 360, Onshape, FreeCAD or SOLIDWORKS). The native SOLIDWORKS files are not published.

| Model | STL | Parasolid |
|---|---|---|
| **Full car** (bluff body with both side wings, front wing, final rear wing) | [`full_car.stl`](cad/full_car.stl) | [`full_car.x_t`](cad/full_car.x_t) |
| Rear wing (final) | [`rear_wing.stl`](cad/rear_wing.stl) | [`rear_wing.x_t`](cad/rear_wing.x_t) |
| Front wing | [`front_wing.stl`](cad/front_wing.stl) | [`front_wing.x_t`](cad/front_wing.x_t) |
| Side wing | [`side_wings.stl`](cad/side_wings.stl) | [`side_wings.x_t`](cad/side_wings.x_t) |
| Bluff body used for CFD | [`bluff_body.stl`](cad/bluff_body.stl) | [`bluff_body.x_t`](cad/bluff_body.x_t) |

<p align="center"><img src="images/car/full_car_system_designed_in_solidworks.jpg" width="70%"></p>

## Code

[`rear-wing-airfoils/`](rear-wing-airfoils) is the Python spline tool I used to rebuild the Benzing rear-wing profiles from sparse coordinates. It writes a densely sampled, curvature-adaptive profile for CAD and meshing.

---
*Akshay Malhan · B.E. Mechanical Engineering, Thapar Institute · [LinkedIn](https://linkedin.com/in/akshaymalhan) · [GitHub](https://github.com/TheMahaanOne)*
