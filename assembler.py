class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Register(metaclass=Singleton):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

    def __repr__(self):
        return "<Register()>"

    def __str__(self):
        return f"[RAX: {self.a}] [RBX: {self.b}] [RCX: {self.c}] [RDX: {self.d}]"


class Assembler():
    def __init__(self):
        self.filepath = None

    def load(self, filepath):
        self.filepath = filepath

    def run(self):
        if self.filepath is None:
            print("ERROR: No file loaded.")
            return

        with open(self.filepath) as fp:
            lines = fp.read().split("\n")

        print("--- START --".ljust(12), Register())


        for line in lines:
            op = line[0:3]
            dst = line[4:7]
            src = line[9:] if not line[9:].isnumeric() else int(line[9])
            
            if op == "MOV":
                self.mov(dst, src)
            elif op == "ADD":
                self.add(dst, src)

            print(line.ljust(12), Register())

        print("--- END ----".ljust(12), Register())

    def mov(self, dst, src):
        src = self._convert(src)
        if dst == "RAX":
            Register().a = src
        elif dst == "RBX":
            Register().b = src
        elif dst == "RCX":
            Register().c = src
        elif dst == "RDX":
            Register().d = src

    def add(self, dst, src):
        src = self._convert(src)
        if dst == "RAX":
            Register().a += src
        elif dst == "RBX":
            Register().b += src
        elif dst == "RCX":
            Register().c += src
        elif dst == "RDX":
            Register().d += src

    def sub(self, dst, src):
        src = self._convert(src)
        if dst == "RAX":
            Register().a -= src
        elif dst == "RBX":
            Register().b -= src
        elif dst == "RCX":
            Register().c -= src
        elif dst == "RDX":
            Register().d -= src

    def _convert(self, src):
        if isinstance(src, int):
            return src
        elif isinstance(src, str):
            if src == "RAX":
                return Register().a
            elif src == "RBX":
                return Register().b
            elif src == "RCX":
                return Register().c
            elif src == "RDX":
                return Register().d
            else:
                raise Exception(f"Failed to convert register {src}")

    def __repr__(self):
        return "<Assembler()>"

    def __str__(self):
        if self.filepath is None:
            return "Assembler: EMPTY"
        else:
            return f"Assembler: {self.filepath}"
            


def main():
    a = Assembler()
    a.load("./asm/jump.asm")
    a.run()
    print(Register())

    print(a)


if __name__ == "__main__":
    main()
