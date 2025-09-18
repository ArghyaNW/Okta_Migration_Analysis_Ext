The algorithm follows a linear additive model with multipliers for complexity. It breaks down effort into fixed base costs and variable components, ensuring estimates scale with organization size and configuration complexity. Here's the breakdown:

1. Initialize Base Effort:
        Start with base_hours = 160 hours. This covers standard project overhead (e.g., planning, meetings, basic setup) regardless of scale.
2. Calculate Component-Specific Effort (Additive Breakdown):
        Applications Migration (app_hours):
            SAML apps: 8 hours each (moderate effort due to standard federation).
            OIDC apps: 6 hours each (simpler protocol mapping).
            SWA (Secure Web Authentication) apps: 16 hours each (higher effort for legacy/manual auth reconfiguration).
            Bookmark apps: 2 hours each (low effort; mostly reconfiguration).
            Total: Sum of (count × hours_per_type).
        Policies and Configuration (policy_hours, agent_hours, etc.):
            OKTA Policies: 12 hours each (recreating rules, MFA, access controls).
            Agents (AD + RADIUS): 24 hours each (decommissioning/installing Entra equivalents, testing connectivity).
            Workflow Automations: 32 hours each (high effort; mapping to Entra Logic Apps or Power Automate).
            Provisioning-Enabled Apps: 16 hours each (sync setup, attribute mapping, testing user/group provisioning).
        Groups Migration (group_hours):
            Groups to Recreate: 2 hours each (simple recreation in Entra ID, but accounts for membership validation).
        Intermediate Total: Sum all components + base_hours. This gives a raw effort estimate.
3. Apply Complexity Multipliers:
        Start with complexity_multiplier = 1.0.
        If num_employees > 5000: Add 0.3 (30% increase for enterprise-scale testing/coordination).
        If federated_domains_count > 5: Add 0.2 (20% increase for multi-domain federation challenges).
        Final Effort: int(total_hours * complexity_multiplier).
        This ensures the estimate adjusts for non-linear risks like large user bases or distributed identity setups.
4. Output and Usage:
        Returns total hours as an integer.
        In the broader calculator, this feeds into:
            Days: effort_hours / 8.
            Timeline: Influences weeks calculation (e.g., effort_days / 5 for working weeks).
            Complexity Score: Cross-references for risk assessment.
        Assumptions: Effort is consultant-led; internal IT effort is separate (e.g., via num_it_staff in cost calcs). All rates are estimates based on industry benchmarks (e.g., 8-32 hours per item from migration guides).
Example Calculation
        Using the "medium" predefined scenario data:
        saml_apps_count=25 → 25 × 8 = 200 hours
        oidc_apps_count=12 → 12 × 6 = 72 hours
        swa_apps_count=18 → 18 × 16 = 288 hours
        bookmark_apps_count=35 → 35 × 2 = 70 hours
        okta_policies_count=8 → 8 × 12 = 96 hours
        okta_ad_agents_count=3 + okta_radius_agents_count=2 → 5 × 24 = 120 hours
        workflow_automations_count=8 → 8 × 32 = 256 hours
        provisioning_enabled_apps=15 → 15 × 16 = 240 hours
        groups_recreate_count=25 → 25 × 2 = 50 hours
        Base: 160 hours
        Raw Total: 160 + 200 + 72 + 288 + 70 + 96 + 120 + 256 + 240 + 50 = 1,552 hours
        Multipliers: num_employees=1200 (no +0.3), federated_domains_count=3 (no +0.2) → Multiplier = 1.0
        Final Effort: 1,552 hours (~194 days).



5. Detailed Breakdown 


> Currency: USD.  
> Example shown: **Medium Enterprise** scenario from your model.

---

### 0) QUICK SUMMARY

```
+---------------------------+-------------------------+
| Metric                    | Value                   |
+---------------------------+-------------------------+
| Final Effort (hours/days) | 1,552 h / 194.0 days    |
| Total Cost (excl. support)| $546,300                |
| Total Cost (incl. support)| $577,700                |
| Timeline                  | 23 weeks                |
| Complexity Score / Level  | 79 / High               |
+---------------------------+-------------------------+
```

---

### 1) INPUTS (SCENARIO VALUES)

```
+---------------------------+-------------------------+
| Item                      | Value                   |
+---------------------------+-------------------------+
| Employees                 | 1,200                   |
| IT Staff                  | 15                      |
| Locations                 | 6                       |
| SAML Apps                 | 25                      |
| OIDC Apps                 | 12                      |
| SWA Apps                  | 18                      |
| Bookmark Apps             | 35                      |
| Total Apps                | 90                      |
| Policies                  | 8                       |
| AD Agents                 | 3                       |
| RADIUS Agents             | 2                       |
| Total Agents              | 5                       |
| Workflows                 | 8                       |
| Provisioning-enabled Apps | 15                      |
| Federated Domains         | 3                       |
| Groups to Recreate        | 25                      |
| Annual Okta Cost          | $85,000                 |
+---------------------------+-------------------------+
```

---

### 2) EFFORT BREAKDOWN

```
+--------------------------+------------+----------+-----------------+
| Component                | Unit (h)   | Quantity | Subtotal Hours  |
+--------------------------+------------+----------+-----------------+
| Base Project             | 160        |    —     | 160             |
| SAML Apps                | 8/app      |   25     | 200             |
| OIDC Apps                | 6/app      |   12     | 72              |
| SWA Apps                 | 16/app     |   18     | 288             |
| Bookmark Apps            | 2/app      |   35     | 70              |
| Policies                 | 12/policy  |    8     | 96              |
| Agents (AD + RADIUS)     | 24/agent   |    5     | 120             |
| Workflows                | 32/flow    |    8     | 256             |
| Provisioning             | 16/app     |   15     | 240             |
| Groups                   | 2/group    |   25     | 50              |
+--------------------------+------------+----------+-----------------+
| PRE-MULTIPLIER HOURS                               | 1,552          |
| Effort Multipliers: Emp>5k (+0.3)? No; Domains>5 (+0.2)? No        |
+----------------------------------------------------+----------------+
| FINAL EFFORT HOURS                                  | 1,552          |
| FINAL EFFORT DAYS (÷8)                              | 194.0          |
+----------------------------------------------------+----------------+
```

---

### 3) COST BREAKDOWN

```
+-----------------------------------------+---------------------------+------------+
| Bucket                                  | Computation               | Subtotal   |
+-----------------------------------------+---------------------------+------------+
| Licensing (base)                        | 1,200 × $22 × 12          | $316,800   |
| Licensing (premium add-on)              | Policies>10? No ⇒ $0      | $0         |
+-----------------------------------------+---------------------------+------------+
| INFRASTRUCTURE                                                                      |
+-----------------------------------------+---------------------------+------------+
| Base Setup                              | Fixed                     | $25,000    |
| Agents                                  | 5 × $5,000                | $25,000    |
| Domains                                 | 3 × $2,500                | $7,500     |
| Monitoring & Logging                    | Emp>1,000 ⇒ $15,000       | $15,000    |
| Infrastructure Total                    | Sum                       | $72,500    |
+-----------------------------------------+---------------------------+------------+
| PROFESSIONAL SERVICES                                                                |
+-----------------------------------------+---------------------------+------------+
| Base Services                           | Fixed                     | $50,000    |
| Apps Component                          | 90 × $750                 | $67,500    |
| Policies Component                      | 8 × $1,500                | $12,000    |
| Workflows Component                     | 8 × $2,500                | $20,000    |
| Training                                | 15 × $500                 | $7,500     |
| Services Subtotal (before multipliers)  | Sum                       | $157,000   |
| Services Multipliers                    | Wkfl>20? No; Prov>30? No  | ×1.0       |
| Professional Services Total             | 157,000 × 1.0             | $157,000   |
+-----------------------------------------+---------------------------+------------+
| SUPPORT (20% of services)               | 0.2 × 157,000             | $31,400    |
+-----------------------------------------+---------------------------+------------+
| TOTAL (excl. support)                   | 316,800 + 72,500 + 157,000| $546,300   |
| TOTAL (incl. support)                   | + 31,400                  | $577,700   |
+-----------------------------------------+---------------------------+------------+
```

---

### 4) TIMELINE CALCULATION

```
+---------------------------+------------------------------+-----------+
| Component                 | Rule/Computation             | Value     |
+---------------------------+------------------------------+-----------+
| Base Weeks                | Fixed                        | 12.00     |
| Effort Component          | 0.3 × (194.0 ÷ 5)            | 11.64     |
| Complexity Adders         | Wkfl>15 (+4)? No             | 0         |
|                           | Prov>25 (+3)? No             | 0         |
|                           | Domains>5 (+2)? No           | 0         |
+---------------------------+------------------------------+-----------+
| TOTAL WEEKS (int, min 8)                                  | 23        |
+-----------------------------------------------------------+-----------+
```

---

### 5) PHASE PLAN (FROM 23 WEEKS)

```
+---------------------------+--------+
| Phase                     | Weeks  |
+---------------------------+--------+
| Planning & Assessment     | 3      |
| Environment Setup         | 2      |
| User Migration            | 5      |
| Application Migration     | 8      |
| Testing & Validation      | 3      |
| Cutover & Support         | 1      |
+---------------------------+--------+
```

---

### 6) COMPLEXITY SCORE (0–100)

```
+---------------------------+----------------------------+---------+
| Dimension                 | Computation                | Points  |
+---------------------------+----------------------------+---------+
| Apps                      | min(90 × 0.5, 25)          | 25      |
| Policies                  | min(8 × 2, 20)             | 16      |
| Workflows                 | min(8 × 1.5, 15)           | 12      |
| Provisioning              | min(15 × 1, 15)            | 15      |
| Federated Domains         | min(3 × 2, 10)             | 6       |
| Organization Size         | +5 (1,200 > 1,000)         | 5       |
| Locations                 | +0 (6 ≤ 10)                | 0       |
+---------------------------+----------------------------+---------+
| TOTAL SCORE                                           | 79      |
| COMPLEXITY LEVEL                                      | High    |
+-------------------------------------------------------+---------+
```

---

### 7) RISKS & RECOMMENDATIONS

```
+-------------------+------------------------------+----------------------------------------------+
| Type              | Trigger                      | Output                                       |
+-------------------+------------------------------+----------------------------------------------+
| Risk              | Complexity > 75              | HIGH: Phased approach + extensive testing    |
| Risk              | Workflows > 20               | Not triggered                                |
| Risk              | Provisioning > 30            | Not triggered                                |
| Recommendation    | Complexity > 70              | Phased migration (High)                      |
| Recommendation    | Always                       | Monitoring & alerting (Medium)               |
| Recommendation    | Always                       | User training & communications (Medium)      |
+-------------------+------------------------------+----------------------------------------------+
```

---

### 8) ROI SNAPSHOT (ILLUSTRATIVE)

```
+---------------------------+------------------+
| Metric                    | Amount           |
+---------------------------+------------------+
| Year 1                    | $577,700         |
| Year 2                    | $348,200         |
| Year 3                    | $348,200         |
| 3-Year Entra Total        | $1,274,100       |
| Okta Avoided (3 years)    | $255,000         |
| Payback (months, approx.) | 81.6             |
+---------------------------+------------------+
```

---

### 9) CRITICAL PATH

```
+-----------------------------------+----------+
| Check                             | Result   |
+-----------------------------------+----------+
| Workflows > 10?                   | No       |
| SWA Apps > 20?                    | No       |
| Federated Domains > 3?            | No       |
| Provisioning > 20?                | No       |
+-----------------------------------+----------+
| CRITICAL PATH                     | Standard |
|                                   | Application Migration |
+-----------------------------------+----------------------+
```
