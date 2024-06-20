class LinuxCommands:
    @staticmethod
    def ipconfig():
        return "ip a"

    def search(self, filename):
        return "cd / | find " + filename
