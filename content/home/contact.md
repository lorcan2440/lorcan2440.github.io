---
# An instance of the Contact widget.
widget: contact

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 10

title: Contact
subtitle: This goes to my email.

content:
  # Automatically link email and phone or display as text?
  autolink: true

  # Email form provider
  form:
    provider: netlify
    formspree:
      id:
    netlify:
      # Enable CAPTCHA challenge to reduce spam?
      captcha: true

  # Contact details (edit or remove options as required)
  email: lorcan.nicholls@cantab.net
  phone:
  address:
    street:
    city:
    country:
    country_code:
    postcode: 
 # coordinates:
 #   latitude: '37.4275'
 #   longitude: '-122.1697'
  #directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
  #office_hours:
  #  - 'Monday 10:00 to 13:00'
  #  - 'Wednesday 09:00 to 10:00'
#  appointment_url: https://calendly.com/lorcan2440
#  contact_links:
#    - icon: twitter
#      icon_pack: fab
#      name: Dm me
#      link: 'https://twitter.com/Nick_2440'
#    - icon: instagram
#      icon_pack: fab
#      name: See my insta
#      link: 'https://www.instagram.com/nxck2440/'

design:
  columns: '2'
---
