class Proposition():
    def __init__(self, name: str, t: bool) -> None:
        self.name = name
        self.t = t
        
    @staticmethod
    def compare(prop_1: 'Proposition', prop_2: 'Proposition') -> int:
        val = 0
        if (prop_1.name == prop_2.name):
            val += 1
            if (prop_1.t == prop_2.t):
                val += 1
        return val

    def negate(self) -> 'Proposition':
        return Proposition(self.name, not self.t)

    def __eq__(self, other: 'Proposition') -> bool:
        return (self.name == other.name and self.t == other.t)

    def __hash__(self) -> int:
        return hash((self.name, self.t))
