# Architecture

## Design Principles

- Minimal file count
- Explicit data boundaries
- Deterministic transformations
- Clear isolation of SAM execution
- Repository is the source of truth

---

## High-Level Flow

CSV  
↓  
Parse Sites  
↓  
Climate Assembly  
- NSRDB (GHI, DNI, albedo)  
- ERA5 / ERA5-Land (primary weather)  
- METAR (gap fill / fallback)  
↓  
Loss Parameter Generation  
- Monthly soiling losses  
- Snow losses via SAM  
↓  
SAM Execution  
- PySAM (primary)  
- Direct SAM API fallback (JSON)  
↓  
Post-Processing  
- 8760 extraction  
- Annual metrics  
↓  
Outputs  
- CSV  
- PNG visuals  
- PDF summary  

---

## Module Layout (Minimal)

```text
solar_production/
├── run.py              # CLI entrypoint
├── climate.py          # ERA5, NSRDB, METAR assembly
├── losses.py           # Soiling logic (pure functions)
├── sam_runner.py       # PySAM + API fallback abstraction
├── outputs.py          # CSV, plots, PDF generation
├── utils.py            # Shared helpers (time, units, I/O)
└── scripts/
    └── verify.sh       # Canonical verification command
