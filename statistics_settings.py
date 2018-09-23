class Settings():
    """initiate settings"""
    def __init__(self):
        self.sample_num = 100
        self.cycle_num = 5000
        self.file_path_1 = "399300_cov.xlsx"
        self.file_path_2 = "net_value.xlsx"
        self.hist_bins = int(self.cycle_num / 50)
        self.draw_out = True