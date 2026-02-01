# MD_ET_Sample
Meta Data Driven ETL Python JSON sample
Metadata-Driven ETL (MD-ETL) framework follows a modular flow where the transformation logic is decoupled from the data itself. Instead of writing unique hard code for every new file ETL, you create a generic "engine" that follows instructions metadata provided by a configuration file.



Here is the step-by-step breakdown of a quick sample to illustrate this:

1. The Configuration Phase (The "Brain")
The process begins with the Metadata Markup (config.json). This file acts as the instruction manual recepie for the engine. 
It defines:
 Source Fields: Which columns to look for in the raw data.
 Aliases: What to rename those columns for the final output (standardization).
 Transformations: A list of specific functions to apply to that column (e.g., trim, uppercase, fix_date).

2. The Initialization Phase
When the main script (meatada_transform_etl.py) is executed, it performs the following:
Loading: reads the JSON configuration and loads the raw data (the test_input.csv) into a memory-efficient structure called a DataFrame.

3. The Transformation Engine (The "Assembly Line")
The DataIngestor class iterates through the mappings defined in your metadata. For every column specified in the JSON:
Validation: It checks if the column exists in the source file. If it doesn't, it is ignored (preventing crashes).
Sequential Logic: It loops through the "transform" list for that column. If it sees trim, it removes whitespace; if it sees fix_date, it re-formats the string.
Null Handling: It identifies "dirty" null values (like NaN or the string 'None') and converts them to clean, empty strings.

4. The Mapping and Filtering Phase
Once transformations are complete, the engine performs a "Selection and Rename" operation:
Filtering: It drops any columns from the raw file that were not mentioned in the JSON (removing "garbage" data).
Aliasing: It renames the remaining columns to their professional aliases (e.g., first_name becomes FirstName).

5. The Output Phase
Finally, the processed data is returned to the main script, which:
Previews the Data: Displays the first few rows in the console for verification.
Persists the Data: Saves the cleaned, standardized result into a new file (final_output.csv).

Summary of Benefits
By following this process, onboarding a new data source no longer requires writing new Python code. You simply create a new config.json for the new vendor, and the existing engine handles the rest, significantly speeding up data integration.

See sample input file, config, output and code in the comment.

hashtag#Python hashtag#Pandas hashtag#JSON hashtag#ETL hashtag#DataEngineering hashtag#MDETL hashtag#MetadataDriven 
hashtag#DataAutomation hashtag#DataAgility hashtag#ScalablePipelines hashtag#DataOnboarding 
hashtag#SoftwareArchitecture hashtag#CleanCode hashtag#DataStandardization hashtag#Automation 
hashtag#LowCode hashtag#DataOps hashtag#ModernDataStack hashtag#DataIngestion
