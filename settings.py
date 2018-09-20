class Settings():
    """initiate settings"""
    def __init__(self):
        self.sample_num = 100
        self.cycle_num = 100000
        self.file_path = "399300.xlsx"
        self.hist_bins = int(self.cycle_num / 50)