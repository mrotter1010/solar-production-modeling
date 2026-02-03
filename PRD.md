# Product Requirements Document (PRD)

## MVP Scope

### Inputs
- CSV file where each row represents an independent site
- Location data sufficient to resolve climate inputs
- System specifications required for SAM PV modeling
- Monthly loss parameters (albedo, soiling)

---

### Climate Data

**Primary source**
- ERA5 / ERA5-Land
  - Temperature
  - Precipitation
  - Snowfall / snow depth

**Fallback source**
- METAR
  - Used only to fill missing ERA data
  - Used as a trusted temperature fallback
  - Nearest-station lookup required

**Solar resource**
- NSRDB
  - GHI
  - DNI
  - Monthly albedo (12 values)

---

### Loss Modeling

**Soiling**
- Monthly losses
- Driven by cumulative monthly precipitation
- If multi-year climate data is pulled, precipitation is averaged by month
- Baseline soiling loss is 1%

| Monthly Precipitation (inches) | Soiling Loss |
|-------------------------------|--------------|
| ≥ 2.0                         | 1.0% |
| 1.5 – 2.0                     | 1.5% |
| 1.0 – 1.5                     | 2.0% |
| 0.5 – 1.0                     | 2.5% |
| < 0.5                         | 3.0% |

**Snow**
- Modeled exclusively using SAM’s native snow loss model
- No custom snow loss logic outside SAM

---

### Simulation Rules

- Hourly resolution (8760)
- Leap years ignored
- SAM-native expectations enforced
- Timezone (UTC vs local) validated empirically and documented

---

### Outputs (per site)

**Data**
- CSV containing full 8760 production profile
- Annual summary metrics:
  - Total generation
  - Yield
  - Net capacity factor
  - Loss breakdown

**Visuals**
- Monthly production bar chart (PNG)
- Waterfall loss diagram (PNG)

**Report**
- Simple, professional PDF
- Includes:
  - Site specifications
  - Climate summary
  - Key production metrics
  - Embedded visuals
- No branding or custom theming

---

### Execution

- CLI-only
- Single command processes all sites in the CSV
- Each site is executed independently
- Failure of one site must not halt batch execution

---

## Non-Goals

- Battery energy storage modeling
- Dispatch or optimization
- Financial modeling
- Web UI or API service
- Branding or advanced report styling
- Leap-year handling
- Sub-hourly resolution

---

## Acceptance Criteria

1. Running the CLI with a valid CSV produces outputs for each valid site row
2. ERA5 data is used as the primary climate source
3. METAR data fills missing ERA values where required
4. Monthly soiling losses are computed deterministically from precipitation
5. SAM snow loss model is enabled and configurable
6. Outputs include:
   - 8760 CSV
   - Two PNG plots
   - One PDF summary per site
7. `scripts/verify.sh` completes successfully
