class Proposition():
    def __init__(self, name: str, negation: bool) -> None:
        self.name = name
        self.negation = negation
        
    @staticmethod
    def compare(prop_1: 'Proposition', prop_2: 'Proposition') -> int:
        val = 0
        if (prop_1.name == prop_2.name):
            val += 1
            if (prop_1.negation == prop_2.negation):
                val += 1
        return val

    def __not__(self) -> 'Proposition':
        return Proposition(self.name, not self.negation)
