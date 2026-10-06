import os
import pymupdf
import subprocess
import shutil
import base64

work_dir = r"C:\Users\SURFACE LAPTOP\.gemini\antigravity\scratch\regan_costa_nursing_cv"
downloads_dir = r"C:\Users\SURFACE LAPTOP\Downloads"
photo_path = os.path.join(work_dir, "assets", "regan_peter_costa_photo.jpg")

with open(photo_path, "rb") as f:
    photo_b64 = base64.b64encode(f.read()).decode("utf-8")

# 1. Western ATS HTML
html_western = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Regan Peter Costa - Registered Hemodialysis Nurse CV</title>
<style>
  @page {
    size: A4;
    margin: 10mm 13mm 10mm 13mm;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    color: #1a202c;
    background: #fff;
    line-height: 1.34;
    font-size: 9.2pt;
  }
  
  .header {
    border-bottom: 2px solid #0f4c81;
    padding-bottom: 5px;
    margin-bottom: 7px;
  }
  .name {
    font-size: 19pt;
    font-weight: 800;
    color: #0f4c81;
    letter-spacing: -0.3px;
    text-transform: uppercase;
  }
  .title {
    font-size: 11pt;
    font-weight: 700;
    color: #2b6cb0;
    margin-top: 1px;
  }
  .contact-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    font-size: 8.5pt;
    color: #4a5568;
    margin-top: 4px;
  }
  .contact-item strong { color: #1a202c; }
  .contact-item a { color: #2b6cb0; text-decoration: none; }
  
  .badge-row {
    margin-top: 5px;
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
  }
  .badge {
    background: #ebf8ff;
    color: #2b6cb0;
    border: 1px solid #bee3f8;
    font-size: 7.8pt;
    font-weight: 700;
    padding: 1.5px 6px;
    border-radius: 3px;
  }
  .badge-gold {
    background: #fefcbf;
    color: #975a16;
    border: 1px solid #faf089;
  }

  .section {
    margin-bottom: 7px;
  }
  .section-title {
    font-size: 9.8pt;
    font-weight: 800;
    color: #0f4c81;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    border-bottom: 1.2px solid #cbd5e0;
    padding-bottom: 1.5px;
    margin-bottom: 4px;
    break-after: avoid;
    page-break-after: avoid;
  }
  .summary-text {
    font-size: 8.8pt;
    color: #2d3748;
    line-height: 1.40;
    text-align: justify;
  }

  .skills-table {
    width: 100%;
    border-collapse: collapse;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    font-size: 8.2pt;
  }
  .skills-table td {
    padding: 3px 6px;
    vertical-align: top;
    border: 1px solid #e2e8f0;
    line-height: 1.30;
  }
  .skills-table td strong {
    color: #0f4c81;
    display: inline-block;
    width: 115px;
  }

  .job-block {
    margin-bottom: 5px;
  }
  .job-head {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    break-after: avoid;
    page-break-after: avoid;
  }
  .job-role {
    font-size: 9.5pt;
    font-weight: 800;
    color: #1a202c;
  }
  .job-hospital {
    font-size: 8.9pt;
    font-weight: 700;
    color: #2b6cb0;
  }
  .job-dates {
    font-size: 8.5pt;
    font-weight: 700;
    color: #4a5568;
  }
  .job-bullets {
    margin-top: 2.5px;
    padding-left: 14px;
    font-size: 8.5pt;
    color: #2d3748;
    line-height: 1.36;
  }
  .job-bullets li {
    margin-bottom: 2px;
    page-break-inside: avoid;
  }

  .grid-2col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
  }
  .card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 8.3pt;
    page-break-inside: avoid;
  }
  .card strong {
    color: #0f4c81;
    font-size: 8.8pt;
    display: block;
    margin-bottom: 1px;
  }
  .card p {
    color: #4a5568;
    line-height: 1.25;
  }

  .page-break {
    page-break-before: always;
    break-before: page;
  }
</style>
</head>
<body>

<!-- PAGE 1: Core Profile + Competencies + Square Hospitals Ltd. (10 Years) -->
<div class="header">
  <div class="name">Regan Peter Costa, RN</div>
  <div class="title">Registered Nurse &ndash; Hemodialysis &amp; Nephrology Specialist</div>
  <div class="contact-row">
    <div class="contact-item"><strong>Location:</strong> Dhaka, Bangladesh</div>
    <div class="contact-item"><strong>Phone:</strong> +880 1936 621888 / +880 1772 684986</div>
    <div class="contact-item"><strong>Email:</strong> <a href="mailto:regancosta1010@gmail.com">regancosta1010@gmail.com</a></div>
    <div class="contact-item"><strong>Portfolio &amp; Verified Credentials:</strong> <a href="https://zion369369.github.io/regan-peter-costa-portfolio/" target="_blank">zion369369.github.io/regan-peter-costa-portfolio</a></div>
  </div>
  <div class="badge-row">
    <span class="badge badge-gold">10+ Years Continuous Dialysis Service (Square Hospitals Ltd.)</span>
    <span class="badge">BNMC License: 32750 (Valid to July 2029)</span>
    <span class="badge">BLS Provider (Jan 2025)</span>
    <span class="badge">Fresenius / B. Braun / SLED Expert</span>
  </div>
</div>

<div class="section">
  <div class="section-title">Professional Summary</div>
  <p class="summary-text">
    Dedicated, patient-focused <strong>Registered Hemodialysis Nurse</strong> with <strong>over 10 consecutive years of high-volume clinical practice</strong> in the Hemodialysis &amp; Nephrology Department of <strong>Square Hospitals Ltd.</strong> (Dhaka's leading 400+ bed JCI-standard tertiary private hospital). Possesses proven mastery in the independent setup, priming, programming, and troubleshooting of advanced hemodialysis platforms including <strong>Fresenius 4008S, 5008 CorDiax, B. Braun Dialog+, Gambro AK 96</strong>, and bedside <strong>Sustained Low-Efficiency Dialysis (SLED)</strong> for ICU critical renal care. Accomplished in advanced vascular access cannulation (native Arteriovenous Fistulas and Grafts) using rope-ladder and buttonhole techniques, sterile Central Venous Catheter (<strong>Permcath</strong>) maintenance under strict Aseptic Non-Touch Technique (ANTT), and emergency intradialytic stabilization. Certified BLS provider with active BNMC registration valid through July 2029. Fully prepared for international direct-hire relocation to the UK (NHS direct application), Ireland (HSE), Middle East, or US (EB-3).
  </p>
</div>

<div class="section">
  <div class="section-title">Core Clinical Competencies &amp; Technical Skills</div>
  <table class="skills-table">
    <tr>
      <td><strong>Dialysis Modalities:</strong> Intermittent Hemodialysis (IHD), Sustained Low-Efficiency Dialysis (SLED), Online HDF, High-Flux Hemodialysis, Isolated Ultrafiltration (SCUF).</td>
      <td><strong>Machinery:</strong> Fresenius Medical Care (4008S, 5008 CorDiax), B. Braun Dialog+, Gambro AK 96, Artis Physio, ICU Bedside Dialysis Systems.</td>
    </tr>
    <tr>
      <td><strong>Vascular Access:</strong> Native AV Fistula (AVF) &amp; Graft (AVG) cannulation (14G–17G), Rope-ladder/Buttonhole, Bruit/Thrill surveillance, Steal syndrome detection.</td>
      <td><strong>CVC &amp; Permcath:</strong> Tunneled Permcath &amp; Temporary CVC sterile access, Heparin (1000/5000 IU/mL) &amp; Citrate locks, ANTT dressings, Clot clearance protocols.</td>
    </tr>
    <tr>
      <td><strong>Emergency Response:</strong> Intradialytic hypotension resuscitation, Dialysis Disequilibrium Syndrome (DDS), First-use reaction, Air embolism Durant maneuver, BLS CPR.</td>
      <td><strong>Water Plant &amp; Adequacy:</strong> Reverse Osmosis (RO) monitoring, Total Chlorine/Chloramine testing (&lt; 0.1 ppm, AAMI/ISO 23500), Urea Kinetic Modeling (Kt/V &ge; 1.3, URR &gt; 68%).</td>
    </tr>
    <tr>
      <td><strong>Pharmacotherapy:</strong> Blood &amp; blood products transfusion, Erythropoietin (EPO), Darbepoetin, IV Iron sucrose, IV Calcium, Heparinization &amp; Heparin-free saline flush.</td>
      <td><strong>Infection Control:</strong> Universal precautions, Bloodborne pathogen isolation bays (Hepatitis B/C, HIV), Dialyzer reprocessing safety, Sharps safety.</td>
    </tr>
  </table>
</div>

<div class="section">
  <div class="section-title">Specialized Hemodialysis Experience</div>

  <div class="job-block">
    <div class="job-head">
      <div>
        <span class="job-role">Senior Staff Nurse &ndash; Hemodialysis &amp; Nephrology Unit</span> | 
        <span class="job-hospital">Square Hospitals Ltd., Dhaka</span>
      </div>
      <span class="job-dates">July 2015 &ndash; Present (10+ Years)</span>
    </div>
    <ul class="job-bullets">
      <li>Manage comprehensive specialized hemodialysis care for a high volume of acute and chronic End-Stage Renal Disease (ESRD) and Acute Kidney Injury (AKI) patients in a modern multi-station tertiary unit.</li>
      <li>Independently prime, program, calibrate, and troubleshoot <strong>Fresenius 4008S, 5008 CorDiax, B. Braun Dialog+, and Gambro</strong> systems with zero equipment-related treatment delays.</li>
      <li>Administer bedside <strong>Sustained Low-Efficiency Dialysis (SLED)</strong> for critically ill, hemodynamically fragile renal patients admitted to Medical ICU, Surgical ICU, and Coronary Care Units.</li>
      <li>Perform high-precision cannulation of complex native Arteriovenous Fistulas and Grafts, achieving a &gt;98% first-attempt success rate while minimizing vessel trauma.</li>
      <li>Execute sterile access, flushing, heparin/citrate locking, and dressing changes for temporary and tunneled Central Venous Catheters (<strong>Permcath</strong>) under strict ANTT protocols, maintaining zero CRBSI incidence.</li>
      <li>Swiftly detect and stabilize intradialytic complications, including severe acute hypotension (fluid bolus, UF suspension, Trendelenburg positioning), muscle cramps, and vascular access clotting.</li>
      <li>Administer renal pharmacotherapy including IV Iron sucrose, Erythropoietin (EPO), Darbepoetin, IV multivitamins, and individualized systemic heparinization protocols.</li>
      <li>Perform clinical calculations for dry weight assessment, ultrafiltration (UF) modeling, and adequacy monitoring (Kt/V &ge; 1.3, URR &gt; 68%).</li>
      <li>Conduct daily morning chemical and total chlorine/chloramine tests on the Reverse Osmosis (RO) water purification plant, strictly verifying adherence to AAMI / ISO 23500 water quality standards.</li>
      <li><em>Verified &amp; Endorsed by Consultant Nephrologist Dr. Mosaddeque Ahmed, MBBS, MRCP (UK), Square Hospitals Ltd.</em></li>
    </ul>
  </div>
</div>

<!-- PAGE 2: Prior Experience + Qualifications + Equipment Log + Languages -->
<div class="page-break"></div>

<div class="section" style="margin-top: 2px;">
  <div class="section-title">Prior Clinical Experience</div>

  <div class="job-block">
    <div class="job-head">
      <div>
        <span class="job-role">Senior Staff Nurse &ndash; Multi-Specialty Inpatient Wards</span> | 
        <span class="job-hospital">Green Life Medical College Hospital</span>
      </div>
      <span class="job-dates">January 2014 &ndash; June 2015 (1.5 Years)</span>
    </div>
    <ul class="job-bullets">
      <li>Delivered clinical bedside nursing care across adult medical and surgical wards, coordinating admissions, preoperative patient prep, postoperative complex wound care, and medication administration.</li>
      <li>Collaborated within multidisciplinary clinical teams consisting of attending physicians, surgeons, and pharmacists to implement tailored patient care and recovery plans.</li>
      <li>Responded rapidly to ward emergency calls, participating in emergency code resuscitations and stabilizing acute deteriorating patients.</li>
    </ul>
  </div>

  <div class="job-block">
    <div class="job-head">
      <div>
        <span class="job-role">Trainee Nurse (Clinical Rotational Internship)</span> | 
        <span class="job-hospital">Green Life Medical College Hospital</span>
      </div>
      <span class="job-dates">January 2011 &ndash; December 2013 (3 Years)</span>
    </div>
    <ul class="job-bullets">
      <li>Completed comprehensive supervised rotational internship across Internal Medicine, General Surgery, Pediatrics, Emergency, Obstetrics &amp; Gynecology, and Nephrology units.</li>
      <li>Maintained accurate, confidential electronic and physical patient records adhering to national clinical documentation standards.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Qualifications &amp; Professional Credentials</div>
  <div class="grid-2col">
    <div class="card">
      <strong>Diploma in Nursing Science and Midwifery (3 Years)</strong>
      <p>Green Life Hospital Nursing Institute | Bangladesh Nursing Council (BNC)</p>
      <p>Session: 2010&ndash;2011 | Comprehensive Council Exam Passed: April 2014</p>
    </div>
    <div class="card">
      <strong>Registered Nurse &amp; Midwife Practitioner (BNMC)</strong>
      <p>Bangladesh Nursing &amp; Midwifery Council | Registration No: <strong>32750</strong></p>
      <p>Original Reg: 07-07-2014 | Renewed: 06-07-2024 | <strong>Valid Upto: 05-07-2029</strong></p>
    </div>
    <div class="card">
      <strong>Basic Life Support (BLS) Provider Certification</strong>
      <p>Approved by Bangladesh Society of Emergency Medicine (BSEM)</p>
      <p>Training Center: Dr. Nizam Medical Centre | Certified: <strong>28 January 2025</strong></p>
    </div>
    <div class="card">
      <strong>Secondary &amp; Higher Secondary Education</strong>
      <p>H.S.C: Tejgaon College, Dhaka Board (Business Studies, 2010)</p>
      <p>S.S.C: Tumilia Boys High School, Dhaka Board (Business Studies, 2008)</p>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-title">Clinical Equipment &amp; Technical Proficiency Log</div>
  <table class="skills-table">
    <tr>
      <td style="width: 25%;"><strong>Fresenius 4008S / 5008:</strong></td>
      <td>Fully independent operation, dialyzer circuit priming, blood line setup, profiling (Na/UF), disinfection, pressure alarm troubleshooting.</td>
    </tr>
    <tr>
      <td><strong>B. Braun Dialog+:</strong></td>
      <td>Independent therapy setup, cartridge bloodline mounting, bio-filtration, bicarbonate preparation, and routine maintenance disinfection.</td>
    </tr>
    <tr>
      <td><strong>Gambro AK 96:</strong></td>
      <td>Setup, arterial/venous chamber level adjustment, isolated ultrafiltration (SCUF), treatment data logging, and machine descaling.</td>
    </tr>
    <tr>
      <td><strong>ICU Bedside SLED:</strong></td>
      <td>Bedside slow-flow dialysis in ICU/CCU, continuous heparinization, pre/post-filter monitoring, hemodynamic safety stabilization.</td>
    </tr>
    <tr>
      <td><strong>Vascular Cannulation:</strong></td>
      <td>Native radiocephalic &amp; brachiocephalic AV Fistulas, PTFE Arteriovenous Grafts, rope-ladder &amp; buttonhole puncture (14G–17G needles).</td>
    </tr>
    <tr>
      <td><strong>Permcath &amp; CVC Care:</strong></td>
      <td>Tunneled Internal Jugular Permcath access, exit-site ANTT dressing, 5000 IU/mL heparin locks, 4% citrate instillation, clot aspiration.</td>
    </tr>
  </table>
</div>

<div class="section">
  <div class="section-title">Languages, IT Systems &amp; Declaration</div>
  <table class="skills-table">
    <tr>
      <td style="width: 25%;"><strong>Languages:</strong></td>
      <td><strong>English:</strong> Full Professional Working Proficiency (clinical handovers, patient documentation, medical terminology).<br><strong>Bengali:</strong> Native / Mother Tongue.</td>
    </tr>
    <tr>
      <td><strong>Digital Systems:</strong></td>
      <td>Hospital Information Systems (HIS), Electronic Medical Records (EMR), Microsoft Office (Word, Excel, PowerPoint).</td>
    </tr>
    <tr>
      <td><strong>Declaration &amp; References:</strong></td>
      <td>I hereby declare that all clinical records, employment history, and credentials stated herein are authentic. Verified reference letters, original council certificates, and clinical competency logs available immediately upon request.</td>
    </tr>
  </table>
</div>

</body>
</html>
"""

# 2. Gulf Executive HTML (Photo + GCC personal table)
html_gulf = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Regan Peter Costa - Middle East Executive Nursing CV</title>
<style>
  @page {{
    size: A4;
    margin: 10mm 13mm 10mm 13mm;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    color: #1a202c;
    background: #fff;
    line-height: 1.34;
    font-size: 9.1pt;
  }}
  .header-container {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #0f4c81;
    padding-bottom: 5px;
    margin-bottom: 7px;
  }}
  .header-text {{
    flex: 1;
  }}
  .photo-box {{
    width: 95px;
    height: 118px;
    margin-left: 15px;
    border-radius: 4px;
    border: 2px solid #cbd5e0;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }}
  .photo-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .name {{
    font-size: 18pt;
    font-weight: 800;
    color: #0f4c81;
    text-transform: uppercase;
  }}
  .title {{
    font-size: 10.5pt;
    font-weight: 700;
    color: #2b6cb0;
    margin-top: 1px;
  }}
  .contact-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    font-size: 8.3pt;
    color: #4a5568;
    margin-top: 4px;
  }}
  .contact-item strong {{ color: #1a202c; }}
  .contact-item a {{ color: #2b6cb0; text-decoration: none; }}

  .badge-row {{
    margin-top: 5px;
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
  }}
  .badge {{
    background: #ebf8ff;
    color: #2b6cb0;
    border: 1px solid #bee3f8;
    font-size: 7.5pt;
    font-weight: 700;
    padding: 1.5px 5px;
    border-radius: 3px;
  }}
  .badge-gold {{
    background: #fefcbf;
    color: #975a16;
    border: 1px solid #faf089;
  }}

  .section {{
    margin-bottom: 6px;
  }}
  .section-title {{
    font-size: 9.6pt;
    font-weight: 800;
    color: #0f4c81;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    border-bottom: 1.2px solid #cbd5e0;
    padding-bottom: 1.5px;
    margin-bottom: 4px;
    break-after: avoid;
    page-break-after: avoid;
  }}
  .summary-text {{
    font-size: 8.8pt;
    color: #2d3748;
    line-height: 1.38;
    text-align: justify;
  }}

  .info-table {{
    width: 100%;
    border-collapse: collapse;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    font-size: 8.1pt;
    margin-bottom: 6px;
  }}
  .info-table td {{
    padding: 3px 5px;
    border: 1px solid #e2e8f0;
  }}
  .info-table td.label {{
    font-weight: 700;
    color: #4a5568;
    background: #edf2f7;
    width: 17%;
  }}
  .info-table td.val {{
    color: #1a202c;
    font-weight: 500;
    width: 33%;
  }}

  .skills-table {{
    width: 100%;
    border-collapse: collapse;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    font-size: 8.1pt;
  }}
  .skills-table td {{
    padding: 3px 5px;
    vertical-align: top;
    border: 1px solid #e2e8f0;
    line-height: 1.30;
  }}
  .skills-table td strong {{
    color: #0f4c81;
    display: inline-block;
    width: 110px;
  }}

  .job-block {{
    margin-bottom: 5px;
  }}
  .job-head {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    break-after: avoid;
    page-break-after: avoid;
  }}
  .job-role {{
    font-size: 9.5pt;
    font-weight: 800;
    color: #1a202c;
  }}
  .job-hospital {{
    font-size: 8.9pt;
    font-weight: 700;
    color: #2b6cb0;
  }}
  .job-dates {{
    font-size: 8.4pt;
    font-weight: 700;
    color: #4a5568;
  }}
  .job-bullets {{
    margin-top: 2.5px;
    padding-left: 14px;
    font-size: 8.4pt;
    color: #2d3748;
    line-height: 1.35;
  }}
  .job-bullets li {{
    margin-bottom: 2px;
    page-break-inside: avoid;
  }}

  .grid-2col {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
  }}
  .card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 8.2pt;
    page-break-inside: avoid;
  }}
  .card strong {{
    color: #0f4c81;
    font-size: 8.7pt;
    display: block;
    margin-bottom: 1px;
  }}
  .card p {{
    color: #4a5568;
    line-height: 1.25;
  }}

  .page-break {{
    page-break-before: always;
    break-before: page;
  }}
</style>
</head>
<body>

<!-- PAGE 1: Header + Photo + GCC Details + Summary + Competencies + Square Hospitals -->
<div class="header-container">
  <div class="header-text">
    <div class="name">Regan Peter Costa, RN</div>
    <div class="title">Senior Hemodialysis Specialist Nurse &ndash; Square Hospitals Ltd.</div>
    <div class="contact-row">
      <div class="contact-item"><strong>Location:</strong> Dhaka, Bangladesh</div>
      <div class="contact-item"><strong>Phone:</strong> +880 1936 621888 / +880 1772 684986</div>
      <div class="contact-item"><strong>Email:</strong> <a href="mailto:regancosta1010@gmail.com">regancosta1010@gmail.com</a></div>
      <div class="contact-item"><strong>Portfolio &amp; Verified Credentials:</strong> <a href="https://zion369369.github.io/regan-peter-costa-portfolio/" target="_blank">zion369369.github.io/regan-peter-costa-portfolio</a></div>
    </div>
    <div class="badge-row">
      <span class="badge badge-gold">10+ Years Square Hospitals Ltd.</span>
      <span class="badge">BNMC Active (Valid to 2029)</span>
      <span class="badge">BLS Certified (2025)</span>
      <span class="badge">DataFlow / GCC Ready</span>
    </div>
  </div>
  <div class="photo-box">
    <img src="data:image/jpeg;base64,{photo_b64}" alt="Regan Peter Costa">
  </div>
</div>

<div class="section">
  <div class="section-title">Personal &amp; Regulatory Credentials (GCC Authorities)</div>
  <table class="info-table">
    <tr>
      <td class="label">Date of Birth:</td>
      <td class="val">14 November 1992 (Age: 33)</td>
      <td class="label">Nationality:</td>
      <td class="val">Bangladeshi (By Birth)</td>
    </tr>
    <tr>
      <td class="label">Religion:</td>
      <td class="val">Christian (Roman Catholic)</td>
      <td class="label">Marital Status:</td>
      <td class="val">Married</td>
    </tr>
    <tr>
      <td class="label">National ID (NID):</td>
      <td class="val">8660039069</td>
      <td class="label">Passport:</td>
      <td class="val">Ready for Immediate Visa Processing</td>
    </tr>
    <tr>
      <td class="label">BNMC License:</td>
      <td class="val">Reg No: 32750 (Valid to 05-07-2029)</td>
      <td class="label">DataFlow / PSV:</td>
      <td class="val">Document Verification Ready (SCFHS, DHA, DOH, QCHP)</td>
    </tr>
  </table>
</div>

<div class="section">
  <div class="section-title">Professional Summary</div>
  <p class="summary-text">
    Highly experienced <strong>Senior Hemodialysis Nurse</strong> with <strong>over 10 consecutive years of clinical practice</strong> in the specialized Hemodialysis Department of <strong>Square Hospitals Ltd.</strong> (Dhaka's premier JCI-standard tertiary private hospital). Expert in independently operating, calibrating, and troubleshooting major dialysis platforms: <strong>Fresenius 4008S, 5008 CorDiax, B. Braun Dialog+, Gambro AK 96</strong>, and ICU bedside <strong>Sustained Low-Efficiency Dialysis (SLED)</strong>. Master of native Arteriovenous Fistula (AVF) and Graft (AVG) cannulation, sterile Central Venous Catheter (<strong>Permcath</strong>) maintenance under strict Aseptic Non-Touch Technique (ANTT), and emergency intradialytic stabilization. Certified BLS provider with active BNMC registration valid through July 2029. Actively seeking senior clinical opportunities across premier hospitals in <strong>Saudi Arabia, UAE, Qatar, and Kuwait</strong>.
  </p>
</div>

<div class="section">
  <div class="section-title">Specialized Hemodialysis Experience</div>

  <div class="job-block">
    <div class="job-head">
      <div>
        <span class="job-role">Senior Staff Nurse &ndash; Hemodialysis Department</span> | 
        <span class="job-hospital">Square Hospitals Ltd., Dhaka</span>
      </div>
      <span class="job-dates">July 2015 &ndash; Present (10+ Years)</span>
    </div>
    <ul class="job-bullets">
      <li>Deliver specialized hemodialysis nursing care for a high volume of ESRD and acute renal failure patients in a modern multi-bed tertiary hemodialysis unit.</li>
      <li>Independently prime, operate, and troubleshoot <strong>Fresenius 4008S, 5008 CorDiax, B. Braun Dialog+, and Gambro</strong> systems across rotating morning, evening, and emergency shifts.</li>
      <li>Conduct bedside <strong>Sustained Low-Efficiency Dialysis (SLED)</strong> for critically ill patients in Medical ICU, Surgical ICU, and Coronary Care Units.</li>
      <li>Perform high-precision cannulation of Arteriovenous (AV) Fistulas and Grafts, achieving a &gt;98% first-attempt success rate while preserving vascular integrity.</li>
      <li>Perform sterile access, heparin locking, and dressing changes for temporary and tunneled Central Venous Catheters (<strong>Permcath</strong>) under strict ANTT protocols, achieving zero CRBSI.</li>
      <li>Intervene rapidly during intradialytic complications (severe hypotension, muscle cramps, chest pain, dialyzer reactions) via UF rate adjustment, Trendelenburg positioning, and saline resuscitation.</li>
      <li>Administer prescribed renal medications: Erythropoietin (EPO), Darbepoetin, IV iron preparations, IV calcium, and individualized heparinization protocols.</li>
      <li>Conduct daily morning chemical testing of the Reverse Osmosis (RO) water purification plant, strictly verifying total chlorine/chloramine levels comply with AAMI/ISO 23500 standards.</li>
      <li><em>Formally Endorsed by Dr. Mosaddeque Ahmed, MBBS, MRCP (UK), Consultant Nephrology, Square Hospitals Ltd.</em></li>
    </ul>
  </div>
</div>

<!-- PAGE 2: Prior Experience + Qualifications + Equipment Log + Languages -->
<div class="page-break"></div>

<div class="section" style="margin-top: 2px;">
  <div class="section-title">Prior Clinical Experience</div>

  <div class="job-block">
    <div class="job-head">
      <div>
        <span class="job-role">Senior Staff Nurse &ndash; Inpatient Medical &amp; Surgical Wards</span> | 
        <span class="job-hospital">Green Life Medical College Hospital</span>
      </div>
      <span class="job-dates">January 2014 &ndash; June 2015 (1.5 Years)</span>
    </div>
    <ul class="job-bullets">
      <li>Delivered bedside clinical care across general medical and surgical wards, coordinating admissions, post-op wound dressings, and medication administration.</li>
      <li>Assisted attending consultants during bedside sterile procedures and managed pre/post-operative surgical recovery pathways.</li>
    </ul>
  </div>

  <div class="job-block">
    <div class="job-head">
      <div>
        <span class="job-role">Trainee Nurse (Clinical Rotational Internship)</span> | 
        <span class="job-hospital">Green Life Medical College Hospital</span>
      </div>
      <span class="job-dates">January 2011 &ndash; December 2013 (3 Years)</span>
    </div>
    <ul class="job-bullets">
      <li>Completed supervised rotations across Medicine, Surgery, Pediatrics, Emergency, and Nephrology departments.</li>
      <li>Maintained accurate, confidential electronic and physical patient records adhering to hospital documentation protocols.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Qualifications &amp; Professional Credentials</div>
  <div class="grid-2col">
    <div class="card">
      <strong>Diploma in Nursing Science and Midwifery (3 Years)</strong>
      <p>Green Life Hospital Nursing Institute | Session: 2010&ndash;2011 | Passed: April 2014</p>
    </div>
    <div class="card">
      <strong>Registered Nurse &amp; Midwife Practitioner (BNMC)</strong>
      <p>Reg No: <strong>32750</strong> | Reg Date: 07-07-2014 | <strong>Valid Upto: 05-07-2029</strong></p>
    </div>
    <div class="card">
      <strong>Basic Life Support (BLS) Provider Certification</strong>
      <p>Approved by Bangladesh Society of Emergency Medicine (BSEM) | Certified: <strong>28 Jan 2025</strong></p>
    </div>
    <div class="card">
      <strong>Secondary &amp; Higher Secondary Education</strong>
      <p>H.S.C: Tejgaon College, Dhaka (2010) | S.S.C: Tumilia Boys High School, Dhaka (2008)</p>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-title">Clinical Competencies &amp; Equipment Mastery</div>
  <table class="skills-table">
    <tr>
      <td style="width: 25%;"><strong>Dialysis Machines:</strong></td>
      <td>Fresenius 4008S, 5008 CorDiax, B. Braun Dialog+, Gambro AK 96, ICU Bedside SLED systems.</td>
    </tr>
    <tr>
      <td><strong>Vascular Cannulation:</strong></td>
      <td>Native AV Fistula &amp; Graft cannulation (Rope-ladder / Buttonhole), Bruit &amp; Thrill surveillance.</td>
    </tr>
    <tr>
      <td><strong>Central Venous Lines:</strong></td>
      <td>Tunneled Permcath sterile access, 5000 IU/mL Heparin &amp; Citrate locks, ANTT dressings, Clot aspiration.</td>
    </tr>
    <tr>
      <td><strong>Emergency Response:</strong></td>
      <td>Intradialytic hypotension protocol, DDS management, dialyzer reaction intervention, BLS CPR.</td>
    </tr>
    <tr>
      <td><strong>Water Plant Quality:</strong></td>
      <td>Daily RO total chlorine/chloramine testing (&lt;0.1 ppm, AAMI/ISO 23500), Kt/V &ge; 1.3, URR &gt; 68%.</td>
    </tr>
  </table>
</div>

<div class="section">
  <div class="section-title">Languages, IT Skills &amp; Declaration</div>
  <table class="skills-table">
    <tr>
      <td style="width: 25%;"><strong>Languages:</strong></td>
      <td><strong>English:</strong> Professional Working Proficiency.<br><strong>Bengali:</strong> Native / Mother Tongue.</td>
    </tr>
    <tr>
      <td><strong>Computer Systems:</strong></td>
      <td>Hospital Information Systems (HIS), Electronic Medical Records (EMR), Microsoft Office Suite.</td>
    </tr>
    <tr>
      <td><strong>Official Declaration:</strong></td>
      <td>I hereby solemnly declare that all statements presented are true and authentic. Verified credentials and consultant recommendation letters available immediately upon request.</td>
    </tr>
  </table>
</div>

</body>
</html>
"""

# Write HTML files
file_western_html = os.path.join(work_dir, "Regan_Peter_Costa_CV_Western_ATS.html")
file_gulf_html = os.path.join(work_dir, "Regan_Peter_Costa_CV_Gulf_Executive.html")

with open(file_western_html, "w", encoding="utf-8") as f:
    f.write(html_western)

with open(file_gulf_html, "w", encoding="utf-8") as f:
    f.write(html_gulf)

print("Saved HTML files.")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
pdf_western = os.path.join(work_dir, "Regan_Peter_Costa_CV_Western_ATS.pdf")
pdf_gulf = os.path.join(work_dir, "Regan_Peter_Costa_CV_Gulf_Executive.pdf")

# Generate Western PDF
subprocess.run([
    edge_path, "--headless", "--disable-gpu", "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_western}", file_western_html
], check=True)

# Generate Gulf PDF
subprocess.run([
    edge_path, "--headless", "--disable-gpu", "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_gulf}", file_gulf_html
], check=True)

# Copy to Downloads
shutil.copy2(pdf_western, os.path.join(downloads_dir, "Regan_Peter_Costa_CV_Western_ATS.pdf"))
shutil.copy2(pdf_gulf, os.path.join(downloads_dir, "Regan_Peter_Costa_CV_Gulf_Executive.pdf"))

# Copy to public/downloads for the website
public_dl = os.path.join(work_dir, "public", "downloads")
shutil.copy2(pdf_western, os.path.join(public_dl, "Regan_Peter_Costa_CV_Western_ATS.pdf"))
shutil.copy2(pdf_gulf, os.path.join(public_dl, "Regan_Peter_Costa_CV_Gulf_Executive.pdf"))

# Render page images with pymupdf to inspect
doc_w = pymupdf.open(pdf_western)
print(f"Western ATS total pages: {len(doc_w)}")
for i, p in enumerate(doc_w):
    pix = p.get_pixmap(dpi=150)
    pix.save(os.path.join(work_dir, f"fixed_ats_p{i+1}.png"))

doc_g = pymupdf.open(pdf_gulf)
print(f"Gulf Executive total pages: {len(doc_g)}")
for i, p in enumerate(doc_g):
    pix = p.get_pixmap(dpi=150)
    pix.save(os.path.join(work_dir, f"fixed_gulf_p{i+1}.png"))

print("All PDFs regenerated and rendered to images successfully!")
