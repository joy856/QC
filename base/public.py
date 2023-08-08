import os


class publicmethod():

    def __init__(self):
        pass

    def get_path(self,*filename):
        realpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(realpath,*filename)
        return path






if __name__ == "__main__":
    pm = publicmethod()
    print(pm.get_path())

