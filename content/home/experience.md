---
# An instance of the Experience widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: experience


##### order
# 1) About
# 2) Skills_1
# 3) Experience
# 4) Projects
# 5) Courses Taken
# 6) Recent Posts
# 7) Tags
# 8) Contact

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 3

title: Experience
subtitle:

# Date format for experience
#   Refer to https://wowchemy.com/docs/customization/#date-format
date_format: Jan 2006

# Experiences.
#   Add/remove as many `experience` items below as you like.
#   Required fields are `title`, `company`, and `date_start`.
#   Leave `date_end` empty if it's your current employer.
#   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
experience:
  - title: Research Student
    company: Bio-Inspired Robotics Lab (BIRL)
    company_url: 'https://birlab.org/'
    company_logo: birl
    location: Cambridge
    date_start: '2023-07-03'
    date_end: '2023-09-08'
    description: |2-
        * Investigated the use of hydrogel-based e-skin for multi-touch sensors via electrical impedance tomography (EIT) and published a paper to ICRA
        * 3D printed and assembled a tensile testing machine for characterising the hydrogel's mechanical and viscoelastic properties
        * Designed the EIT apparatus in CAD and fabricated from PLA using a laser cutter for the frame, and a gelatin-glycerol-carbon black sensorised e-skin.
        * Programmed a UR5 industrial robot to gather a real dataset for pressing of the e-skin, and trained/tested neural nets to predict touch position based on the EIT data.

  - title: Data Analyst
    company: Oodle Car Finance
    company_url: 'https://www.oodlecarfinance.com/'
    company_logo: oodle-car-finance
    location: London, UK & Remote
    date_start: '2021-07-06'
    date_end: '2021-09-30'
    description: |2-
        * Developed a new benchmark for comparing delinquency rates, fit to a variety of customer risk indicators
        * Worked closely with the analytics team to create new metrics for predicting arrears deterioration from live Salesforce databases with Looker, SQL and Excel, including use of VBA and Python for utility scripting and automation
        * Verified a 30% increase in customer call-to-payment rates due to the adoption of a new IVR telephony system

  - title: Work Experience (Automotive Engineering and CAD)
    company: Cummins Turbo Technologies
    company_url: 'https://www.cummins.com/'
    company_logo: cummins-turbo-technologies
    location: Huddersfield, UK
    date_start: '2019-04-15'
    date_end: '2019-04-19'
    description:  |2-
        * Designed diesel engine components to engineering drawing specifications with Creo
        * Stripped down a turbocharger in Lab Ops and examined it for surface defects using an X-ray diffractometer
        * Simulated component response to mechanical and thermal loads
        * Presented to an audience of 20+ coworkers, including teams via conference call in India and China

  - title: Work Experience (Semiconductor QA)
    company: Arm
    company_url: 'https://www.arm.com/'
    company_logo: arm
    location: Sheffield, UK
    date_start: '2018-10-29'
    date_end: '2018-11-02'
    description:  |2-
        * Analysed a large JSON dataset on transistor characteristics using Python in the Spyder IDE to identify trends in performance
        * Presented a method to identify pairwise correlation using Seaborn, NumPy and
        Pandas to an audience of 10+ coworkers

design:
  columns: '1'
---
