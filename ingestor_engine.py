import pandas as pd
import numpy as np

class DataIngestor:
    def __init__(self, config):
        self.config = config
        
    def _transform_logic(self, df, source_col, transforms):
        """Applies business logic based on metadata tags."""
        for action in transforms:
            if action == "trim":
                df[source_col] = df[source_col].astype(str).str.strip()
            elif action == "uppercase":
                df[source_col] = df[source_col].astype(str).str.upper()
            elif action == "null_to_blank":
                # Replaces technical nulls with an empty string
                df[source_col] = df[source_col].replace(['nan', 'None', 'NaN', np.nan], '')
            elif action == "fix_date":
                # Converts yyyy/mm/dd to mm/dd/yy
                df[source_col] = pd.to_datetime(df[source_col]).dt.strftime('%m/%d/%y')
        return df

    def process(self, input_df):
        """Maps columns to aliases and triggers transformations."""
        final_cols = {}
        working_df = input_df.copy()
        
        for item in self.config['mappings']:
            src = item['source']
            alias = item['alias']
            actions = item.get('transform', [])
            
            if src in working_df.columns:
                working_df = self._transform_logic(working_df, src, actions)
                final_cols[src] = alias
        
        # Filter to only the columns defined in mapping and rename them
        return working_df[list(final_cols.keys())].rename(columns=final_cols)
