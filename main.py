import csv
from linkedin_api import Linkedin

# Replace with your LinkedIn credentials
username = "___Linkedin_Username__"
password = "___linkedin_Pass__"

# Initialize the LinkedIn API with your credentials
api = Linkedin(username, password)

# list of userID of Linkedin
urls = [
    'neetu-rawat',
    'abdullah1shahid',
    'vishakha-patel-895412221',
    'nanda-soni-a03749210',
    'kirti-verma-b210a4246',
    'priya-agarwal-3657a5200',
]

# Initialize an empty list to store the scraped data
scraped_data = []

# Iterate through each profile URL
for url in urls:
    try:
        profile_data = api.get_profile(url)

        if 'firstName' not in profile_data:
            print(f"Could not retrieve data for profile: {url}")
            continue

        fname = profile_data.get('firstName', 'Not available')
        lname = profile_data.get('lastName', 'Not available')
        headline = profile_data.get('headline', 'Not available')
        location = profile_data.get('geoLocationName', 'Not available')
        current_company = profile_data["experience"][0]["companyName"]
        summary = profile_data.get('summary', 'Not available')
        skills = profile_data.get('skills', 'Not available')

        if not skills:
            skills = 'Skills data not available'

        # Extracted education data
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

        # Append the scraped data to the list
        scraped_data.append({
            'Name': f"{fname} {lname}",
            'Headline': headline,
            'Location': location,
            'Current Company': current_company,
            'Summary': summary,
            'Skills': skills,
            'Education': education_text
        })

    except Exception as e:
        print(f"Failed to retrieve the data for profile {url}. Error: {e}")

# Store the scraped data in a CSV file
csv_file = 'scraped_data.csv'
headers = ['Name', 'Headline', 'Location', 'Current Company', 'Summary', 'Skills', 'Education']

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(scraped_data)

print("Scraped Data: ", scraped_data)
print(f"Data has been scraped successfully and stored in {csv_file}.")
