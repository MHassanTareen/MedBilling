class TimeCalculator:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def convert_to_24h_format(self, time_str):
        if 'AM' in time_str or 'PM' in time_str:
            period = time_str[-2:]
            time_str = time_str[:-3]
            hours, minutes = map(int, time_str.split(":"))
            if period == "PM" and hours != 12:
                hours += 12
            elif period == "AM" and hours == 12:
                hours = 0
        else:
            hours, minutes = map(int, time_str.split(":"))
        return hours, minutes

    def calculate_difference(self):
        st_hours, st_minutes = self.convert_to_24h_format(self.start_time)
        ed_hours, ed_minutes = self.convert_to_24h_format(self.end_time)

        start_total_minutes = st_hours * 60 + st_minutes
        end_total_minutes = ed_hours * 60 + ed_minutes

        if end_total_minutes < start_total_minutes:
            end_total_minutes += 24 * 60  # Handle crossing midnight

        total_minutes = end_total_minutes - start_total_minutes
        diff_hours = total_minutes // 60
        diff_minutes = total_minutes % 60

        return diff_hours, diff_minutes


# Example usage
enter_time1 = input('Start Time (e.g., "02:34 AM"): ')
enter_time2 = input('End Time (e.g., "03:45 PM"): ')

calculator = TimeCalculator(enter_time1, enter_time2)
diff_hours, diff_minutes = calculator.calculate_difference()

print(f"Time difference is {diff_hours} hours and {diff_minutes} minutes.")
