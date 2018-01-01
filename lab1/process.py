class Process:
    def __init__(self, executive_time, appear_time, name):

        self.name = name;
        self.executive_time = executive_time
        self.wait_time = 0
        self.time_to_finish = executive_time
        self.appear_time = appear_time
        self.start_time = -1
        self.finish_time = -1

    def wait(self):
        self.wait_time += 1

    def execute(self):
        self.time_to_finish -= 1