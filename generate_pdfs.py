import os
import subprocess
import base64
import shutil

work_dir = r"C:\Users\SURFACE LAPTOP\.gemini\antigravity\scratch\regan_costa_nursing_cv"
downloads_dir = r"C:\Users\SURFACE LAPTOP\Downloads"
photo_path = os.path.join(work_dir, "assets", "regan_peter_costa_photo.jpg")

with open(photo_path, "rb") as f:
    photo_b64 = base64.b64encode(f.read()).decode("utf-8")

# 1. Western ATS HTML Template
html_western = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Regan Peter Costa - Registered Hemodialysis Nurse CV</title>
<style>
  @page {{
    size: A4;
    margin: 12mm 14mm 12mm 14mm;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    color: #1a202c;
    background: #fff;
    line-height: 1.42;
    font-size: 9.8pt;
  }}
  .header {{
    border-bottom: 2.5px solid #0f4c81;
    padding-bottom: 8px;
    margin-bottom: 10px;
  }}
  .name {{
    font-size: 19pt;
    font-weight: 700;
    color: #0f4c81;
    letter-spacing: -0.3px;
    text-transform: uppercase;
  }}
  .title {{
    font-size: 11.5pt;
    font-weight: 600;
    color: #2b6cb0;
    margin-top: 2px;
  }}
  .contact-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    font-size: 8.8pt;
    color: #4a5568;
    margin-top: 5px;
  }}
  .contact-item strong {{ color: #2d3748; }}
  .contact-item a {{ color: #2b6cb0; text-decoration: none; }}
  
  .badge-row {{
    margin-top: 6px;
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }}
  .badge {{
    background: #ebf8ff;
    color: #2b6cb0;
    border: 1px solid #bee3f8;
    font-size: 7.8pt;
    font-weight: 600;
    padding: 2px 7px;
    border-radius: 4px;
  }}
  .badge-gold {{
    background: #fefcbf;
    color: #975a16;
    border: 1px solid #faf089;
  }}

  .section {{
    margin-bottom: 10px;
  }}
  .section-title {{
    font-size: 10.2pt;
    font-weight: 700;
    color: #0f4c81;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #cbd5e0;
    padding-bottom: 2px;
    margin-bottom: 6px;
  }}
  .summary-text {{
    font-size: 9.2pt;
    color: #2d3748;
    line-height: 1.48;
    text-align: justify;
  }}

  .skills-table {{
    width: 100%;
    border-collapse: collapse;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    font-size: 8.5pt;
  }}
  .skills-table td {{
    padding: 4px 8px;
    vertical-align: top;
    border: 1px solid #e2e8f0;
    line-height: 1.35;
  }}
  .skills-table td strong {{
    color: #0f4c81;
    display: inline-block;
    width: 125px;
  }}

  .job-block {{
    margin-bottom: 9px;
    page-break-inside: avoid;
  }}
  .job-head {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }}
  .job-role {{
    font-size: 10pt;
    font-weight: 700;
    color: #1a202c;
  }}
  .job-hospital {{
    font-size: 9.2pt;
    font-weight: 600;
    color: #2b6cb0;
  }}
  .job-dates {{
    font-size: 8.8pt;
    font-weight: 600;
    color: #4a5568;
  }}
  .job-bullets {{
    margin-top: 3px;
    padding-left: 15px;
    font-size: 8.8pt;
    color: #2d3748;
    line-height: 1.42;
  }}
  .job-bullets li {{
    margin-bottom: 2.5px;
  }}

  .grid-2col {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
  }}
  .card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 8.5pt;
    page-break-inside: avoid;
  }}
  .card strong {{
    color: #0f4c81;
    font-size: 9pt;
    display: block;
    margin-bottom: 2px;
  }}
  .card p {{
    color: #4a5568;
    line-height: 1.3;
  }}
</style>
</head>
<body>

<div class="header">
  <div class="name">Regan Peter Costa, RN</div>
  <div class="title">Registered Nurse &ndash; Hemodialysis &amp; Nephrology Specialist</div>
  <div class="contact-row">
    <div class="contact-item"><strong>Location:</strong> Dhaka, Bangladesh</div>
    <div class="contact-item"><strong>Phone:</strong> +880 1936 621888 / +880 1772 684986</div>
    <div class="contact-item"><strong>Email:</strong> regancosta1010@gmail.com</div>
    <div class="contact-item"><strong>LinkedIn:</strong> linkedin.com/in/regan-peter-costa</div>
    <div class="contact-item"><strong>Portfolio:</strong> freeimage.host/i/n1g9P9e</div>
  </div>
  <div class="badge-row">
    <span class="badge badge-gold">10+ Years Square Hospitals Ltd. (Hemodialysis Unit)</span>
    <span class="badge">BNMC Registration: 32750 (Valid to July 2029)</span>
    <span class="badge">Basic Life Support (BLS) Provider (Jan 2025)</span>
    <span class="badge">Fresenius / B. Braun / SLED Expert</span>
  </div>
</div>

<div class="section">
  <div class="section-title">Professional Summary</div>
  <p class="summary-text">
    Dedicated, patient-focused <strong>Registered Hemodialysis Nurse</strong> with <strong>over 10 consecutive years of high-volume clinical practice</strong> in the Hemodialysis &amp; Nephrology Department of <strong>Square Hospitals Ltd.</strong> (Dhaka's leading 400+ bed JCI-standard tertiary private hospital). Possesses proven expertise in the independent setup, priming, programming, and troubleshooting of advanced hemodialysis platforms including <strong>Fresenius 4008S, 5008 CorDiax, B. Braun Dialog+, Gambro AK 96</strong>, and bedside <strong>Sustained Low-Efficiency Dialysis (SLED)</strong> for ICU critical renal care. Accomplished in advanced vascular access cannulation (native Arteriovenous Fistulas and Grafts) using rope-ladder and buttonhole techniques, sterile Central Venous Catheter (<strong>Permcath</strong>) maintenance under strict Aseptic Non-Touch Technique (ANTT), and protocolized emergency intradialytic stabilization. BLS certified with active BNMC registration valid through July 2029. Fully prepared for international direct-hire transition into the UK (NHS direct application), Ireland (HSE), Middle East, or US (EB-3).
  </p>
</div>

<div class="section">
  <div class="section-title">Core Clinical Competencies &amp; Technical Skills</div>
  <table class="skills-table">
    <tr>
      <td><strong>Dialysis Modalities:</strong> Intermittent Hemodialysis (IHD), Sustained Low-Efficiency Dialysis (SLED), Online HDF, High-Flux Hemodialysis, Isolated Ultrafiltration (SCUF).</td>
      <td><strong>Machinery:</strong> Fresenius Medical Care (4008S, 5008 CorDiax), B. Braun Dialog+, Gambro AK 96, Artis Physio, ICU Bedside Dialysis.</td>
    </tr>
    <tr>
      <td><strong>Vascular Access:</strong> Native AV Fistula (AVF) &amp; Graft (AVG) cannulation (14G–17G), Rope-ladder/Buttonhole, Bruit/Thrill surveillance, Steal syndrome detection.</td>
      <td><strong>CVC &amp; Permcath:</strong> Tunneled &amp; Non-tunneled CVC sterile access, Heparin (1000/5000 IU/mL) &amp; Citrate locks, ANTT dressings, Clot clearance protocols.</td>
    </tr>
    <tr>
      <td><strong>Emergency Response:</strong> Intradialytic hypotension resuscitation, Dialysis Disequilibrium Syndrome (DDS), First-use reaction, Air embolism protocol, BLS CPR.</td>
      <td><strong>Water Plant &amp; Adequacy:</strong> Reverse Osmosis (RO) monitoring, Total Chlorine/Chloramine testing (&lt; 0.1 ppm, AAMI/ISO 23500), Urea Kinetic Modeling (Kt/V &ge; 1.3, URR &gt; 68%).</td>
    </tr>
    <tr>
      <td><strong>Pharmacotherapy:</strong> Blood &amp; blood products transfusion, Erythropoietin (EPO), Darbepoetin, IV Iron sucrose, IV Calcium, Heparinization &amp; Heparin-free saline flush.</td>
      <td><strong>Infection Control:</strong> Universal precautions, Bloodborne pathogen isolation bays (Hepatitis B/C, HIV), Dialyzer reprocessing safety, Sharps safety.</td>
    </tr>
  </table>
</div>

<div class="section">
  <div class="section-title">Professional Clinical Experience</div>

  <div class="job-block">
    <div class="job-head">
      <div>
        <span class="job-role">Senior Staff Nurse &ndash; Hemodialysis &amp; Nephrology Unit</span> | 
        <span class="job-hospital">Square Hospitals Ltd., Dhaka</span>
      </div>
      <span class="job-dates">July 2015 &ndash; Present (10+ Years)</span>
    </div>
    <ul class="job-bullets">
      <li>Manage comprehensive specialized hemodialysis care for a high volume of acute and chronic End-Stage Renal Disease (ESRD) and Acute Kidney Injury (AKI) patients in a modern multi-station dialysis department.</li>
      <li>Independently prime, program, calibrate, and troubleshoot <strong>Fresenius 4008S, 5008 CorDiax, B. Braun Dialog+, and Gambro</strong> systems with zero equipment-related treatment delays.</li>
      <li>Administer bedside <strong>Sustained Low-Efficiency Dialysis (SLED)</strong> for critically ill, hemodynamically fragile renal patients admitted to Medical ICU, Surgical ICU, and CCU.</li>
      <li>Perform high-precision cannulation of complex native Arteriovenous Fistulas and Grafts, achieving a &gt;98% first-attempt success rate while minimizing vessel trauma.</li>
      <li>Execute sterile access, flushing, heparin/citrate locking, and dressing changes for temporary and tunneled Central Venous Catheters (<strong>Permcath</strong>) under strict ANTT protocols, maintaining zero CRBSI incidence under direct shift care.</li>
      <li>Swiftly detect and stabilize intradialytic complications, including severe acute hypotension (fluid bolus, UF suspension, Trendelenburg positioning), muscle cramps, and vascular access clotting.</li>
      <li>Administer renal pharmacotherapy including IV Iron sucrose, Erythropoietin (EPO), Darbepoetin, IV multivitamins, and individualized systemic heparinization protocols.</li>
      <li>Perform clinical calculations for dry weight assessment, ultrafiltration (UF) modeling, and adequacy monitoring (Kt/V &ge; 1.3, URR &gt; 68%).</li>
      <li>Conduct daily morning chemical and total chlorine/chloramine tests on the Reverse Osmosis (RO) water purification plant, strictly verifying adherence to AAMI / ISO 23500 water quality standards before initiating patient sessions.</li>
      <li><em>Verified &amp; Endorsed by Consultant Nephrologist Dr. Mosaddeque Ahmed, MBBS, MRCP (UK), Square Hospitals Ltd.</em></li>
    </ul>
  </div>

  <div class="job-block">
    <div class="job-head">
      <div>
        <span class="job-role">Senior Staff Nurse &ndash; Multi-Specialty Inpatient Wards</span> | 
        <span class="job-hospital">Green Life Medical College Hospital</span>
      </div>
      <span class="job-dates">January 2014 &ndash; June 2015 (1.5 Years)</span>
    </div>
    <ul class="job-bullets">
      <li>Delivered clinical nursing care across adult medical and surgical wards, coordinating admissions, preoperative prep, postoperative wound care, and medication administration.</li>
      <li>Collaborated within multidisciplinary clinical teams to implement tailored patient recovery plans and responded to hospital ward emergency codes.</li>
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
      <li>Completed rotational clinical internship across Internal Medicine, Surgery, Pediatrics, Emergency, and Nephrology units.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Qualifications &amp; Professional Credentials</div>
  <div class="grid-2col">
    <div class="card">
      <strong>Diploma in Nursing Science and Midwifery (3 Years)</strong>
      <p>Green Life Hospital Nursing Institute | Session: 2010&ndash;2011</p>
      <p>Comprehensive Council Exam Passed: April 2014</p>
    </div>
    <div class="card">
      <strong>Registered Nurse &amp; Midwife Practitioner (BNMC)</strong>
      <p>Registration No: <strong>32750</strong> | Reg Date: 07-07-2014</p>
      <p>Renewed Date: 06-07-2024 | <strong>Valid Upto: 05-07-2029</strong></p>
    </div>
    <div class="card">
      <strong>Basic Life Support (BLS) Provider Certification</strong>
      <p>Approved by Bangladesh Society of Emergency Medicine (BSEM)</p>
      <p>Dr. Nizam Medical Centre | Certified: <strong>28 January 2025</strong></p>
    </div>
    <div class="card">
      <strong>Secondary &amp; Higher Secondary Education</strong>
      <p>H.S.C: Tejgaon College, Dhaka Board (2010)</p>
      <p>S.S.C: Tumilia Boys High School, Dhaka Board (2008)</p>
    </div>
  </div>
</div>

<div class="section" style="margin-top: 6px;">
  <div class="section-title">Languages &amp; Digital Proficiencies</div>
  <p style="font-size: 8.5pt; color: #4a5568;">
    <strong>Languages:</strong> English (Full Professional Working Proficiency in clinical documentation, handover, and patient communication), Bengali (Native).<br>
    <strong>Digital Systems:</strong> Hospital Information Systems (HIS), Electronic Medical Records (EMR), Microsoft Office Suite (Word, Excel, PowerPoint).
  </p>
</div>

</body>
</html>
"""

# 2. Gulf Executive HTML Template (with photo and GCC details)
html_gulf = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Regan Peter Costa - Middle East Executive Nursing CV</title>
<style>
  @page {{
    size: A4;
    margin: 12mm 14mm 12mm 14mm;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    color: #1a202c;
    background: #fff;
    line-height: 1.40;
    font-size: 9.6pt;
  }}
  .header-container {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2.5px solid #0f4c81;
    padding-bottom: 8px;
    margin-bottom: 10px;
  }}
  .header-text {{
    flex: 1;
  }}
  .photo-box {{
    width: 100px;
    height: 125px;
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
    font-size: 18.5pt;
    font-weight: 700;
    color: #0f4c81;
    text-transform: uppercase;
  }}
  .title {{
    font-size: 11pt;
    font-weight: 600;
    color: #2b6cb0;
    margin-top: 2px;
  }}
  .contact-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    font-size: 8.5pt;
    color: #4a5568;
    margin-top: 5px;
  }}
  .contact-item strong {{ color: #2d3748; }}
  .contact-item a {{ color: #2b6cb0; text-decoration: none; }}

  .badge-row {{
    margin-top: 6px;
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
  }}
  .badge {{
    background: #ebf8ff;
    color: #2b6cb0;
    border: 1px solid #bee3f8;
    font-size: 7.5pt;
    font-weight: 600;
    padding: 1.5px 6px;
    border-radius: 3px;
  }}
  .badge-gold {{
    background: #fefcbf;
    color: #975a16;
    border: 1px solid #faf089;
  }}

  .section {{
    margin-bottom: 9px;
  }}
  .section-title {{
    font-size: 9.8pt;
    font-weight: 700;
    color: #0f4c81;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #cbd5e0;
    padding-bottom: 2px;
    margin-bottom: 5px;
  }}
  .summary-text {{
    font-size: 9pt;
    color: #2d3748;
    line-height: 1.45;
    text-align: justify;
  }}

  .info-table {{
    width: 100%;
    border-collapse: collapse;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    font-size: 8.2pt;
    margin-bottom: 8px;
  }}
  .info-table td {{
    padding: 3.5px 6px;
    border: 1px solid #e2e8f0;
  }}
  .info-table td.label {{
    font-weight: 600;
    color: #4a5568;
    background: #edf2f7;
    width: 18%;
  }}
  .info-table td.val {{
    color: #1a202c;
    font-weight: 500;
    width: 32%;
  }}

  .skills-table {{
    width: 100%;
    border-collapse: collapse;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    font-size: 8.3pt;
  }}
  .skills-table td {{
    padding: 4px 6px;
    vertical-align: top;
    border: 1px solid #e2e8f0;
    line-height: 1.32;
  }}
  .skills-table td strong {{
    color: #0f4c81;
    display: inline-block;
    width: 120px;
  }}

  .job-block {{
    margin-bottom: 8px;
    page-break-inside: avoid;
  }}
  .job-head {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }}
  .job-role {{
    font-size: 9.8pt;
    font-weight: 700;
    color: #1a202c;
  }}
  .job-hospital {{
    font-size: 9pt;
    font-weight: 600;
    color: #2b6cb0;
  }}
  .job-dates {{
    font-size: 8.5pt;
    font-weight: 600;
    color: #4a5568;
  }}
  .job-bullets {{
    margin-top: 3px;
    padding-left: 14px;
    font-size: 8.6pt;
    color: #2d3748;
    line-height: 1.40;
  }}
  .job-bullets li {{
    margin-bottom: 2px;
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
    font-size: 8.3pt;
    page-break-inside: avoid;
  }}
  .card strong {{
    color: #0f4c81;
    font-size: 8.8pt;
    display: block;
    margin-bottom: 2px;
  }}
  .card p {{
    color: #4a5568;
    line-height: 1.3;
  }}
</style>
</head>
<body>

<div class="header-container">
  <div class="header-text">
    <div class="name">Regan Peter Costa, RN</div>
    <div class="title">Senior Hemodialysis Nurse Specialist &ndash; Square Hospitals Ltd.</div>
    <div class="contact-row">
      <div class="contact-item"><strong>Location:</strong> Dhaka, Bangladesh</div>
      <div class="contact-item"><strong>Phone:</strong> +880 1936 621888 / +880 1772 684986</div>
      <div class="contact-item"><strong>Email:</strong> regancosta1010@gmail.com</div>
      <div class="contact-item"><strong>Credentials:</strong> freeimage.host/i/n1g9P9e</div>
    </div>
    <div class="badge-row">
      <span class="badge badge-gold">10+ Years Square Hospitals Ltd.</span>
      <span class="badge">BNMC Active (Valid to 2029)</span>
      <span class="badge">BLS Certified (2025)</span>
      <span class="badge">Fresenius / B. Braun / SLED Expert</span>
      <span class="badge">GCC / DataFlow Ready</span>
    </div>
  </div>
  <div class="photo-box">
    <img src="data:image/jpeg;base64,{photo_b64}" alt="Regan Peter Costa">
  </div>
</div>

<div class="section">
  <div class="section-title">Personal &amp; Regulatory Credentials (GCC / Middle East Authorities)</div>
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
      <td class="label">DataFlow / Prometric:</td>
      <td class="val">Document Verification Ready (SCFHS, DHA, DOH, QCHP)</td>
    </tr>
  </table>
</div>

<div class="section">
  <div class="section-title">Professional Summary</div>
  <p class="summary-text">
    Highly skilled <strong>Senior Hemodialysis Nurse</strong> with <strong>over 10 consecutive years of clinical practice</strong> in the Hemodialysis &amp; Nephrology Department of <strong>Square Hospitals Ltd.</strong> (leading JCI-standard tertiary private hospital in Dhaka). Expert in independently operating, calibrating, and troubleshooting major dialysis platforms: <strong>Fresenius 4008S, 5008 CorDiax, B. Braun Dialog+, Gambro AK 96</strong>, and ICU bedside <strong>Sustained Low-Efficiency Dialysis (SLED)</strong>. Master of native Arteriovenous Fistula (AVF) and Graft (AVG) cannulation, sterile Central Venous Catheter (<strong>Permcath</strong>) maintenance under strict Aseptic Non-Touch Technique (ANTT), and emergency intradialytic stabilization. Certified BLS provider with active BNMC registration valid through July 2029. Actively seeking senior nursing opportunities across premier hospitals in <strong>Saudi Arabia, UAE, Qatar, and Kuwait</strong>.
  </p>
</div>

<div class="section">
  <div class="section-title">Core Clinical Competencies</div>
  <table class="skills-table">
    <tr>
      <td><strong>Dialysis Modalities:</strong> Intermittent Hemodialysis (IHD), SLED (ICU bedside), Online HDF, High-Flux Hemodialysis, Isolated Ultrafiltration (SCUF).</td>
      <td><strong>Machinery:</strong> Fresenius 4008S, 5008 CorDiax, B. Braun Dialog+, Gambro AK 96, SLED critical care hemodialysis.</td>
    </tr>
    <tr>
      <td><strong>Vascular Access:</strong> Native AV Fistula &amp; Graft cannulation (Rope-ladder/Buttonhole), Bruit/Thrill surveillance, Steal syndrome detection.</td>
      <td><strong>CVC &amp; Permcath:</strong> Tunneled Permcath sterile access, Heparin (1000/5000 IU/mL) &amp; Citrate locks, ANTT dressings, Clot clearance.</td>
    </tr>
    <tr>
      <td><strong>Emergency Stabilization:</strong> Intradialytic hypotension management, DDS response, dialyzer reaction intervention, air embolism protocol, BLS CPR.</td>
      <td><strong>Water Plant &amp; Adequacy:</strong> Reverse Osmosis (RO) monitoring, Total Chlorine/Chloramine testing (&lt; 0.1 ppm, AAMI/ISO 23500), Kt/V &ge; 1.3, URR &gt; 68%.</td>
    </tr>
  </table>
</div>

<div class="section">
  <div class="section-title">Professional Clinical Experience</div>

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
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Education &amp; Professional Certifications</div>
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

<div class="section" style="margin-top: 5px;">
  <div class="section-title">Languages &amp; IT Skills</div>
  <p style="font-size: 8.3pt; color: #4a5568;">
    <strong>Languages:</strong> English (Professional Working Proficiency), Bengali (Native).<br>
    <strong>Computer Systems:</strong> Hospital Information Systems (HIS), EMR, Microsoft Office (Word, Excel, PowerPoint).
  </p>
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

print("Created HTML templates successfully.")

# Compile to PDF using Edge / Chrome
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

print(f"Using browser for PDF compilation: {edge_path}")

pdf_western = os.path.join(work_dir, "Regan_Peter_Costa_CV_Western_ATS.pdf")
pdf_gulf = os.path.join(work_dir, "Regan_Peter_Costa_CV_Gulf_Executive.pdf")

# Generate Western PDF
cmd1 = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_western}",
    file_western_html
]
subprocess.run(cmd1, check=True)
print("Generated:", pdf_western)

# Generate Gulf PDF
cmd2 = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_gulf}",
    file_gulf_html
]
subprocess.run(cmd2, check=True)
print("Generated:", pdf_gulf)

# Also copy to Downloads folder for instant 1-click user access
dl_western = os.path.join(downloads_dir, "Regan_Peter_Costa_CV_Western_ATS.pdf")
dl_gulf = os.path.join(downloads_dir, "Regan_Peter_Costa_CV_Gulf_Executive.pdf")

shutil.copy2(pdf_western, dl_western)
shutil.copy2(pdf_gulf, dl_gulf)

print("Copied both PDFs to Downloads folder successfully!")
