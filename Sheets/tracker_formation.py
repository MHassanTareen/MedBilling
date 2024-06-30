import pandas as pd
import re
import glob

class MedicalDataProcessor:
    def __init__(self, facility_list, provider_list, surgeon_list):
        self.facility_list = facility_list
        self.provider_list = provider_list
        self.surgeon_list = surgeon_list
        self.errors = []
        self.name_counts = None
        self.total_entries = 0

    def correct_time_format(self, time_str):
        corrected_time = re.sub(r'[,.;\']', ':', time_str)
        if re.match(r'^\d{2}:\d{2}$', corrected_time):
            return corrected_time
        return None

    def load_and_merge_csv_files(self, file_pattern):
        all_files = glob.glob(file_pattern)
        df_list = [pd.read_csv(file) for file in all_files]
        self.merged_df = pd.concat(df_list, ignore_index=True)
        self.log_errors()

    def log_errors(self):
        self.merged_df['Facility_Match'] = self.merged_df['Facility'].isin(self.facility_list)
        self.merged_df['Provider_Match'] = self.merged_df['Provider'].isin(self.provider_list)
        self.merged_df['Surgeon_Match'] = self.merged_df['Surgeon'].isin(self.surgeon_list)

        for col in ['Facility', 'Provider', 'Surgeon']:
            mismatch_col = f'{col}_Match'
            mismatched_values = self.merged_df[~self.merged_df[mismatch_col]][col].unique()
            if mismatched_values.any():
                self.errors.append(f'Mismatched {col}: {", ".join(mismatched_values)}')

        self.merged_df['Start Time'] = self.merged_df['Start Time'].apply(self.correct_time_format)
        self.merged_df['End Time'] = self.merged_df['End Time'].apply(self.correct_time_format)

        time_errors = self.merged_df[
            self.merged_df[['Start Time', 'End Time']].isnull().any(axis=1)
        ][['Start Time', 'End Time']]
        if not time_errors.empty:
            self.errors.append('Time format errors in Start Time and End Time columns')

    def count_entries_by_name(self):
        self.name_counts = self.merged_df['Name'].value_counts()
        self.total_entries = len(self.merged_df)

    def save_corrected_data(self, output_file):
        self.merged_df.to_csv(output_file, index=False)

    def save_report(self, report_file):
        report_data = {
            'Name': self.name_counts.index,
            'Total Records': self.name_counts.values
        }
        report_df = pd.DataFrame(report_data)
        report_df['Errors'] = pd.Series([', '.join(self.errors)] * len(report_df), index=report_df.index)
        report_df.to_csv(report_file, index=False)

    def report(self):
        print("Name Counts:\n", self.name_counts)
        print("\nTotal Entries: ", self.total_entries)
        if self.errors:
            print("\nErrors Found:")
            for error in self.errors:
                print(error)

# Usage
facility_list = ['Facility A', 'Facility B', 'Facility C']
provider_list = ['Provider X', 'Provider Y', 'Provider Z']
surgeon_list = ['Surgeon 1', 'Surgeon 2', 'Surgeon 3']

processor = MedicalDataProcessor(facility_list, provider_list, surgeon_list)
processor.load_and_merge_csv_files("*.csv")
processor.count_entries_by_name()
processor.save_corrected_data('merged_corrected.csv')
processor.save_report('report.csv')
processor.report()
