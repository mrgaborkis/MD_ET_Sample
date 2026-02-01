import pandas as pd
import json
import os
from ingestor_engine import DataIngestor

def run_pipeline():
    # --- DYNAMIC PATH HANDLING ---
    # This finds the folder where THIS script is saved
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    config_path = os.path.join(base_path, 'config.json')
    input_path = os.path.join(base_path, 'test_input.csv')
    output_path = os.path.join(base_path, 'final_output.csv')

    # 1. Load the Metadata Markup
    if not os.path.exists(config_path):
        print(f"Error: Could not find {config_path}")
        return

    with open(config_path, 'r') as f:
        metadata = json.load(f)

    # 2. Load the Raw Data
    if not os.path.exists(input_path):
        print(f"Error: Could not find {input_path}")
        return
        
    df_raw = pd.read_csv(input_path)

    # 3. Initialize and Execute Ingestion
    ingestor = DataIngestor(metadata)
    df_final = ingestor.process(df_raw)

    # 4. Output the Results
    print("--- INGESTION SUCCESSFUL ---")
    print(df_final.head())
    
    df_final.to_csv(output_path, index=False)
    print(f"\nSaved results to: {output_path}")

if __name__ == "__main__":
    run_pipeline()
