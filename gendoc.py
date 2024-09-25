import json

# Load the JSON file
with open('doc-rdl.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the dataset information (assuming the first dataset in the list)
dataset = data.get('datasets', [])[0]  # Taking the first dataset as an example
dataset_id = dataset.get('id', 'N/A')
dataset_title = dataset.get('title', 'N/A')
dataset_description = dataset.get('description', 'N/A')
dataset_project = dataset.get('project', 'N/A')
dataset_details = dataset.get('details', 'N/A')
dataset_license = dataset.get('license', 'N/A')
contact_point = dataset.get('contact_point', {})
contact_name = contact_point.get('name', 'N/A')
contact_email = contact_point.get('email', 'N/A')

# Extract the hazard object from within the first dataset
hazard = dataset.get('hazard', {})
event_sets = hazard.get('event_sets', [])

# Create the Markdown content
markdown = f"# Model Information\n\n"

markdown += f"**Name**: {dataset_project}\n\n"
markdown += f"**Description**: {dataset_details}\n\n"
markdown += f"**License**: {dataset_license}\n\n"
markdown += f"**Contact**: {contact_name} {contact_email}  \n\n"

# Create a hazard module heading
markdown+= "# Hazard module \n\n"

markdown += f"**ID**: {dataset_id}\n\n"
markdown += f"**Title**: {dataset_title}\n\n"
markdown += f"**Description**: {dataset_description}\n\n"


# Create a Markdown table
markdown += "## Event set information \n\n"
markdown += "| Event Set | Type        | Calculation Method | Countries  | Number of events |\n"
markdown += "|-----------|-------------|--------------------|------------|------------------|\n"

# Loop through event_sets and add rows to the Markdown table
for event_set in event_sets:
    event_set_name = event_set.get('id', 'N/A')
    analysis_type = event_set.get('analysis_type', 'N/A')
    calculation_method = event_set.get('calculation_method', 'N/A')
    spatial = event_set.get('spatial', 'N/A')
    countries = spatial.get('countries','N/A')
    event_count = event_set.get('event_count', 'N/A')
    
    markdown += f"| {event_set_name} | {analysis_type} | {calculation_method} | {countries} | {event_count} |\n"

markdown += "\n"
markdown += "## Hazard information \n\n"
markdown += "| Event Set | Process types | Intensity measure | Trigger type  | Trigger process types |\n"
markdown += "|-----------|---------------|-------------------|---------------|-----------------------|\n"

# Loop through event_sets and hazards and add rows to the Markdown table
for event_set in event_sets:
    hazards = event_set.get('hazards', [])
    for hazards_obj in hazards:
        hazards_type = hazards_obj.get('id','N/A')
        hazards_processes = hazards_obj.get('processes','N/A')
        intensity_measure = hazards_obj.get('intensity_measure','N/A')
        trigger = hazards_obj.get('trigger','N/A')
        trigger_type = trigger.get('type','N/A')
        trigger_processes = trigger.get('processes','N/A')

        markdown += f"| {hazards_type} | {hazards_processes} | {intensity_measure} | {trigger_type} | {trigger_processes} |\n"

markdown += "\nThis document has been generated using Risk Data Library Standard schema version 0.2. For more information about the RDLS please visit [RDLS](https://docs.riskdatalibrary.org/en/latest/)"

# Write the output to a markdown file
with open('doc.md', 'w') as md_file:
    md_file.write(markdown)

print("Markdown file generated successfully!")
