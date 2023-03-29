class mypwd(object):
    def __init__(self, file=r"daytime.txt") -> None:
        self.outFile = file

    def save_data(self, data) -> None:
        if not data:
            return
        file = open(file=self.outFile, mode="a+")
        for item in data:
            if isinstance(item,list):
                file.write("+".join(item))
                file.write(" ")
            elif isinstance(item,str) :
                file.write("\n" + item + ">>>>>> ")
            else :
                pass
        file.close()


if __name__ == "__main__":

    TEST = [['a'], ['b'], 'another window', ['a', 'b']]
    TEST2 = [['a'],['b'],['s'],['ctrl','shift'],['a'],['a', 'b']]

    pw = mypwd()
    pw.save_data(TEST)
    pass
