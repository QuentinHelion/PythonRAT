class WindowsCommands:
    @staticmethod
    def ipconfig():
        return "ipconfig"

    def search(self, filename):
        return "cd / | dir /s /b | findstr /i " + filename
