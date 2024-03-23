class F25:
    def light(self):
        print("switching on the lights")
    def fan(self,speed):
        print("fan is on and the speed is",speed)
        self.s=speed
    def cpu(self):
        print("powering on the system")
        print(self.s)
chandu=F25()
chandu.light()
chandu.fan(8)
chandu.cpu()
        

