class WindowsCommands:
    @staticmethod
    def ipconfig():
        return "ipconfig"

    def search(self, filename):
        return "dir /s /b | findstr /i " + filename
