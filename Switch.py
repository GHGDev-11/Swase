class Switch:
    def __init__(self):
        self.switchList = {}
        self.inputCMD = ''
    
    def AddToSwitch(self, Input, Outcome):
        self.switchList[Input] = Outcome
        self.inputCMD += f'\n{Input}'
    
    def PrintSwitch(self):
        print(self.switchList)
    
    def LastSwitch(self, Input, Outcome, Else, Bind):
        self.switchList[Input] = Outcome
        self.inputCMD += f'\n{Input}'
        self.switchList.get(Bind)
        if Bind in self.switchList:
            exec(Outcome)
        else:
            exec(Else)
