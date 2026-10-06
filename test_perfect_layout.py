import os
import pymupdf
import subprocess
import shutil

work_dir = r"C:\Users\SURFACE LAPTOP\.gemini\antigravity\scratch\regan_costa_nursing_cv"
downloads_dir = r"C:\Users\SURFACE LAPTOP\Downloads"

# Let's design the Western ATS HTML so:
# Page 1 contains Header, Summary, Competencies, AND Square Hospitals Ltd. (the 10-year experience)
# Page 2 contains Green Life (Senior Staff Nurse), Green Life (Internship), Education, Licenses/Certifications, and Proficiencies

html_content = """<!DOCTYPE html>
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
    line-height: 1.35;
    font-size: 9.3pt;
  }
  
  /* Header */
  .header {
    border-bottom: 2px solid #0f4c81;
    padding-bottom: 6px;
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

  /* Section Styling */
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
    font-size: 8.9pt;
    color: #2d3748;
    line-height: 1.42;
    text-align: justify;
  }

  /* Skills Table */
  .skills-table {
    width: 100%;
    border-collapse: collapse;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    font-size: 8.3pt;
  }
  .skills-table td {
    padding: 3.5px 6px;
    vertical-align: top;
    border: 1px solid #e2e8f0;
    line-height: 1.32;
  }
  .skills-table td strong {
    color: #0f4c81;
    display: inline-block;
    width: 115px;
  }

  /* Job Blocks */
  .job-block {
    margin-bottom: 6px;
  }
  .job-head {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    break-after: avoid;
    page-break-after: avoid;
  }
  .job-role {
    font-size: 9.6pt;
    font-weight: 800;
    color: #1a202c;
  }
  .job-hospital {
    font-size: 9pt;
    font-weight: 700;
    color: #2b6cb0;
  }
  .job-dates {
    font-size: 8.5pt;
    font-weight: 700;
    color: #4a5568;
  }
  .job-bullets {
    margin-top: 3px;
    padding-left: 14px;
    font-size: 8.6pt;
    color: #2d3748;
    line-height: 1.38;
  }
  .job-bullets li {
    margin-bottom: 2px;
    page-break-inside: avoid;
  }

  /* Grid Layouts */
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
    font-size: 8.4pt;
    page-break-inside: avoid;
  }
  .card strong {
    color: #0f4c81;
    font-size: 8.9pt;
    display: block;
    margin-bottom: 1px;
  }
  .card p {
    color: #4a5568;
    line-height: 1.28;
  }

  /* Force Clean Page Break */
  .page-break {
    page-break-before: always;
    break-before: page;
  }
</style>
</head>
<body>

<!-- ================= PAGE 1 ================= -->
<div class="header">
  <div class="name">Regan Peter Costa, RN</div>
  <div class="title">Registered Nurse &ndash; Hemodialysis &amp; Nephrology Specialist</div>
  <div class="contact-row">
    <div class="contact-item"><strong>Location:</strong> Dhaka, Bangladesh</div>
    <div class="contact-item"><strong>Phone:</strong> +880 1936 621888 / +880 1772 684986</div>
    <div class="contact-item"><strong>Email:</strong> <a href="mailto:regancosta1010@gmail.com">regancosta1010@gmail.com</a></div>
    <div class="contact-item"><strong>LinkedIn:</strong> linkedin.com/in/regan-peter-costa</div>
    <div class="contact-item"><strong>Portfolio:</strong> freeimage.host/i/n1g9P9e</div>
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

<!-- ================= PAGE 2 ================= -->
<div class="page-break"></div>

<div class="section" style="margin-top: 4px;">
  <div class="section-title">Prior Clinical Work Experience</div>

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
  <div class="section-title">Languages, IT Skills &amp; Declaration</div>
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

test_html = os.path.join(work_dir, "test_ats.html")
test_pdf = os.path.join(work_dir, "test_ats.pdf")

with open(test_html, "w", encoding="utf-8") as f:
    f.write(html_content)

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={test_pdf}",
    test_html
]
subprocess.run(cmd, check=True)

# Render pages to PNG
doc = pymupdf.open(test_pdf)
print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=150)
    img_path = os.path.join(work_dir, f"test_ats_p{i+1}.png")
    pix.save(img_path)
    print(f"Saved: {img_path}")
"""

with open(r"C:\Users\SURFACE LAPTOP\.gemini\antigravity\scratch\regan_costa_nursing_cv\test_perfect_layout.py", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Wrote test script")
