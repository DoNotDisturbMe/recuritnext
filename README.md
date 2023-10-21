# recuritnext
#assignment

These lines import the required modules for working with CSV files and the LinkedIn API.

    import csv
    from linkedin_api import Linkedin

These lines store your LinkedIn username and password in variables.

    username = "___Linkedin_Username__"
    password = "___linkedin_Pass__"

This line initializes the LinkedIn API using the provided credentials.

    api = Linkedin(username, password)
    
This list contains the LinkedIn user IDs that you want to scrape data from.

      urls = [
    'neetu-rawat',
    'abdullah1shahid',
    'vishakha-patel-895412221',
    'nanda-soni-a03749210',
    'kirti-verma-b210a4246',
    'priya-agarwal-3657a5200',
]

This initializes an empty list to store the scraped data.

      scraped_data = []

This loop iterates through each URL and attempts to retrieve the LinkedIn profile data using the LinkedIn API.

      for url in urls:
    try:
        profile_data = api.get_profile(url)

This conditional statement checks if the 'firstName' key is not present in the profile data. If it is not found, it prints an error message and continues to the next profile.

      if 'firstName' not in profile_data:
    print(f"Could not retrieve data for profile: {url}")
    continue

    
These lines extract various information such as the first name, last name, headline, location, current company, summary, and skills from the LinkedIn profile data.

    fname = profile_data.get('firstName', 'Not available')
    lname = profile_data.get('lastName', 'Not available')
    headline = profile_data.get('headline', 'Not available')
    location = profile_data.get('geoLocationName', 'Not available')
    current_company = profile_data["experience"][0]["companyName"]
    summary = profile_data.get('summary', 'Not available')
    skills = profile_data.get('skills', 'Not available')


These lines extract education data from the LinkedIn profile, including the school name, degree, field of study, and time period.

      education_data = profile_data.get('education', [])
      education_text = ""
      for education in education_data:
          education_text += f"School Name: {education.get('schoolName', 'Not available')}\n"
          education_text += f"Degree: {education.get('degreeName', 'Not available')}\n"
          education_text += f"Field of Study: {education.get('fieldOfStudy', 'Not available')}\n"
          time_period = education.get('timePeriod', {})
          start_date = time_period.get('startDate', {}).get('year', 'Not available')
          end_date = time_period.get('endDate', {}).get('year', 'Not available')
          education_text += f"Time Period: {start_date} - {end_date}\n\n"


This appends all the extracted data to the scraped_data list.

      scraped_data.append({
    'Name': f"{fname} {lname}",
    'Headline': headline,
    'Location': location,
    'Current Company': current_company,
    'Summary': summary,
    'Skills': skills,
    'Education': education_text
})

These lines define the CSV file name and the headers for the columns.

      csv_file = 'scraped_data.csv'
    headers = ['Name', 'Headline', 'Location', 'Current Company', 'Summary', 'Skills', 'Education']


This code block opens the CSV file and writes the scraped data into it.

      with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(scraped_data)

These lines print the scraped data and a success message after the data has been written to the CSV file

    print("Scraped Data: ", scraped_data)
    print(f"Data has been scraped successfully and stored in {csv_file}.")
