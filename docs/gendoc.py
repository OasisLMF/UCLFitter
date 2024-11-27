import json
import os
import pandas as pd
import pycountry

from md_utils import MarkdownGenerator

# Load the JSON file
with open('doc-rdl.json', 'r') as json_file:
    data = json.load(json_file)

# Initialize the Markdown generator
md = MarkdownGenerator()


# Extract the dataset information (assuming the first dataset in the list)
dataset = data.get('datasets', [])[0]  # Taking the first dataset as an example
dataset_id = dataset.get('id', 'N/A')
dataset_title = dataset.get('title', 'N/A')
dataset_description = dataset.get('description', 'N/A')
dataset_project = dataset.get('project', 'N/A')
dataset_details = dataset.get('details', 'N/A')
dataset_license = dataset.get('license', 'N/A')
dataset_version = dataset.get('version','N/A')
publisher = dataset.get('publisher',{})
publisher_name = publisher.get('name','N/A')
publisher_email = publisher.get('email','N/A')
publisher_url = publisher.get('url','N/A')
contact_point = dataset.get('contact_point', {})
contact_name = contact_point.get('name', 'N/A')
contact_email = contact_point.get('email', 'N/A')

# Add sections using the Markdown generator
# Header
md.add_text('<img src="https://oasislmf.org/packages/oasis_theme_package/themes/oasis_theme/assets/src/oasis-lmf-colour.png" alt="Oasis LMF logo" width="250"/>')
md.add_header(dataset_project,level=1)
md.add_header("Model Key Facts", level=2)

# Overview
#md.add_definition("Name", dataset_project)
#md.add_definition("Description", dataset_details)
#md.add_definition("License", dataset_license)
#md.add_definition("Contact", f"{contact_name} {contact_email}")
md.add_text(dataset_details)

md.add_header("Peril Region", level=3)
md.add_text('TO DO')

md.add_header("Publisher", level=3)
md.add_definition("Name", publisher_name)
md.add_definition("Email", publisher_email)
md.add_definition("URL", publisher_url)

md.add_header("Contact", level=3)
md.add_definition("Name", contact_name)
md.add_definition("Email", contact_email)

md.add_header("Version and Licence", level=3)
md.add_definition("Version", dataset_version)
md.add_definition("License", dataset_license)

# Hazard module heading
md.add_header("Hazard module", level=2)
#md.add_definition("ID", dataset_id)
md.add_definition("Title", dataset_title)
#md.add_definition("Description", dataset_description)
md.add_text(dataset_description)

# Event set information table
md.add_header("Event set information", level=3)
headers = ["Event Set", "Type", "Calculation Method", "Countries", "Number of events"]
rows = []

# Loop through event_sets and add rows to the Markdown table
event_sets = dataset.get('hazard', {}).get('event_sets', [])
for event_set in event_sets:
    event_set_name = event_set.get('id', 'N/A')
    analysis_type = event_set.get('analysis_type', 'N/A')
    calculation_method = event_set.get('calculation_method', 'N/A')
    spatial = event_set.get('spatial', {})
    countries = spatial.get('countries', 'N/A')
    countries_str = ", ".join(countries)
    event_count = event_set.get('event_count', 'N/A')
    row = [event_set_name, analysis_type, calculation_method, countries_str, event_count]
    rows.append([str(r) for r in row])

md.add_table(headers, rows)
md.add_text("TO DO: add occurrence set information ")
# Hazard information table
md.add_header("Hazard information", level=3)
headers = ["Peril Code", "Hazard Process", "Intensity measure", "Trigger Event", "Trigger Process"]
rows = []

# Loop through event_sets and hazards and add rows to the Markdown table
for event_set in event_sets:
    hazards = event_set.get('hazards', [])
    for hazards_obj in hazards:
        hazards_type = hazards_obj.get('id', 'N/A')
        hazards_processes = hazards_obj.get('processes', 'N/A')
        hazards_processes_str = ", ".join(hazards_processes)
        intensity_measure = hazards_obj.get('intensity_measure', 'N/A')
        trigger = hazards_obj.get('trigger', {})
        trigger_type = trigger.get('type', 'N/A')
        trigger_processes = trigger.get('processes', 'N/A')
        trigger_processes_str = ", ".join(trigger_processes)

        row = [hazards_type, hazards_processes_str, intensity_measure, trigger_type, trigger_processes_str]
        rows.append([str(r) for r in row])

md.add_table(headers, rows)
md.add_text("")
# Vulnerability module heading
md.add_header("Vulnerability module", level=2)

datasetv = data.get('datasets', [])[2]  # Vulnerability

# Get the root attributes
dataset_id = datasetv.get('id', 'N/A')
dataset_title = datasetv.get('title', 'N/A')
dataset_description = datasetv.get('description', 'N/A')
# Extract the vulnerability object from within the dataset
vulnerability = datasetv.get('vulnerability', {})
# Vuln attributes
hazard_primary = vulnerability.get('hazard_primary', 'N/A')
hazard_process_primary = vulnerability.get('hazard_process_primary', 'N/A') 
intensity = vulnerability.get('intensity', 'N/A') 
category = vulnerability.get('category', 'N/A') 
analysis_details = vulnerability.get('analysis_details', 'N/A')

impact = vulnerability.get('impact', {})
impact_type = impact.get('type', 'N/A')
impact_metric = impact.get('metric', 'N/A')
impact_unit = impact.get('unit', 'N/A')
impact_base_data_type = impact.get('base_data_type', 'N/A')

spatial = vulnerability.get('spatial', {})
spatial_scale = spatial.get('scale','N/A')
countries = spatial.get('countries', 'N/A')

functions = vulnerability.get('functions', {})
vuln_function = functions.get('vulnerability', {})
approach = vuln_function.get('approach', 'N/A')

#md.add_definition("ID", dataset_id)
md.add_definition("Title", dataset_title)
md.add_text(dataset_description)

md.add_header("Hazard information", level=3)
md.add_table(["Hazard type", "Hazard process", "Intensity"],
                          [[hazard_primary, hazard_process_primary, intensity]])
md.add_text("")
md.add_header("Vulnerability functions", level=3)
md.add_definition("Exposure category", category)
md.add_definition("Countries", countries)
md.add_definition("Impact type", impact_type)
md.add_definition("Impact metric", impact_metric)
md.add_definition("Impact unit", impact_unit)
md.add_definition("Base data type", impact_base_data_type)
md.add_definition("Approach", approach)

md.add_header("Further details", level=3)
md.sections.append(f"{analysis_details}\n\n")


#  new part

# Coverage types and modifiers
md.add_header("Coverage types and modifiers", level=2)

# Exposure class
md.add_header("Exposure category", level=3)
md.add_text("Buildings")

# Coverages
md.add_header("Coverages", level=3)

headers = ["Coverage Type", "Supported?"]
rows = []
rows.append(["Buildings", "Yes"]) # Get this from RDL vulnerability cost tab
rows.append(["Other", "No"]) # Get this from RDL vulnerability cost tab
rows.append(["Contents", "Yes"]) # Get this from RDL vulnerability cost tab
rows.append(["Business Interruption", "No"]) # Get this from RDL vulnerability cost tab
md.add_table(headers, rows)
md.add_text("")
# Primary modifiers
md.add_header("Primary modifiers", level=3)

headers = ["OED field", "Required?","Comments"]
rows = []
rows.append(["OccupancyCode", "No",""]) 
rows.append(["ConstructionCode", "No",""])
rows.append(["NumberOfStories", "No",""])
rows.append(["YearBuilt", "No",""])
rows.append(["FloorArea", "No",""])
md.add_table(headers, rows)
md.add_text("")
# Secondary modifiers
md.add_header("Secondary modifiers", level=3)

headers = ["OED field", "Comments"]
rows=[]
md.add_table(headers, rows)
md.add_text("")
md.add_text("For lists of supported values please see 'Reference Tables' section below")


# Geographical schemes
md.add_header("Geographical schemes", level=2)
md.add_header("Broad scope", level=3)
md.add_definition("Spatial scale", spatial_scale)

headers = ["Country Code", "Country name"]
rows=[]
# Lookup the full country name using pycountry
for code in countries:
    country_name = pycountry.countries.get(alpha_3=code)
    full_name = country_name.name if country_name else "Unknown"
    rows.append([code, full_name])
md.add_table(headers, rows)

md.add_header("Geographical schemes", level=3)
md.add_text("TO DO")
# Reference tables
md.add_header("Reference tables", level=2)

md.add_text("The following reference tables contain key model definitions and lists of supported values for exposure attributes.")
md.add_text("TO DO")


# Define the sub-directory containing the CSV files
sub_directory = "resources/haz"  # Replace with your path

# Loop through all files in the sub-directory
for filename in os.listdir(sub_directory):
    if filename.endswith(".csv"):
        # Full path to the CSV file
        file_path = os.path.join(sub_directory, filename)
        
        # Read the CSV file
        try:
            df = pd.read_csv(file_path)
            
            # Select the first 20 records
            first_20_records = df.head(20)
            
            # Extract headers and rows
            headers = list(first_20_records.columns)
            rows = first_20_records.values.tolist()
            
            # Add filename as a header (if needed)
            md.add_header([filename],level=3)  
            
            # Add the table to the MarkdownGenerator
            md.add_table(headers, rows)

            # Add a hyperlink to the file
            relative_path = os.path.relpath(file_path)
            md.add_text(f"[{filename}]({relative_path})")  # Creates a single-cell Markdown row
        except Exception as e:
            print(f"Error reading {filename}: {str(e)}")

# Define the sub-directory containing the CSV files
sub_directory = "resources/vln"  # Replace with your path

# Loop through all files in the sub-directory
for filename in os.listdir(sub_directory):
    if filename.endswith(".csv"):
        # Full path to the CSV file
        file_path = os.path.join(sub_directory, filename)
        
        # Read the CSV file
        try:
            df = pd.read_csv(file_path)
            
            # Select the first 20 records
            first_20_records = df.head(20)
            
            # Extract headers and rows
            headers = list(first_20_records.columns)
            rows = first_20_records.values.tolist()
            
            # Add filename as a header (if needed)
            md.add_header([filename],level=3)  
            
            # Add the table to the MarkdownGenerator
            md.add_table(headers, rows)

            # Add a hyperlink to the file
            relative_path = os.path.relpath(file_path)
            md.add_text(f"[{filename}]({relative_path})")  # Creates a single-cell Markdown row
        except Exception as e:
            print(f"Error reading {filename}: {str(e)}")
## End of content
# Add footer
md.add_text("This document has been generated using Risk Data Library Standard schema version 0.2.")
md.add_text("For more information about the RDLS please visit [RDLS](https://docs.riskdatalibrary.org/en/latest/)")


# Get the final markdown content
markdown_content = md.get_markdown()


# Write the output to a markdown file
with open('../doc.md', 'w') as md_file:
    md_file.write(markdown_content)

print("Markdown file generated successfully!")
