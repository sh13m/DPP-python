class Proposition():
    """
    A logical proposition
    
    ...
    
    Parameters
    ----------
    name : str
        Set of clauses to perform DPP on, clauses are assumed to be disjunctive
    t : bool
        Negation state (True = p, False = not p)
        
    
    Methods
    -------
    compate()
        Compares how similar two propositions are
    negate()
        Gets negation of a proposition
    string()
        Gets string representation of proposition
    
    """
    
    def __init__(self, name: str, t: bool) -> None:
        self.name = name
        self.t = t
        
    @staticmethod
    def compare(prop_1: 'Proposition', prop_2: 'Proposition') -> int:
        """Compares two propositions
        
        Parameters
        ----------
        prop_1 : Proposition
            First proposition to compare
        prop_2 : Proposition
            Second proposition to compare
        
        Returns
        -------
        val : int
            The comparison value of the two propositions
            0 means propositions have different symbols
            1 means propositions have same symbols but different negation state
            2 means propositions have both same symbols and negation states
            
        """
        val = 0
        if (prop_1.name == prop_2.name):
            val += 1
            if (prop_1.t == prop_2.t):
                val += 1
        return val

    def negate(self) -> 'Proposition':
        """Gets the negation of the itself"""
        return Proposition(self.name, not self.t)
    
    def string(self) -> str:
        """Gets string representation of proposition"""
        if self.t:
            return self.name
        else:
            return "not " + self.name

    def __eq__(self, other: 'Proposition') -> bool:
        return (self.name == other.name and self.t == other.t)

    def __hash__(self) -> int:
        return hash((self.name, self.t))
