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

    def negate(self) -> 'Proposition':
        return Proposition(self.name, not self.negation)

    def __eq__(self, other: 'Proposition') -> bool:
        return (self.name == other.name and self.negation == other.negation)

    def __hash__(self) -> int:
        return hash((self.name, self.negation))
