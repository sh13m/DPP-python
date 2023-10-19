from proposition import *
from typing import Set, FrozenSet, Union
from itertools import combinations

class DPP():
    """
    Davis-Putnam Procedure in python
    
    ...
    
    Parameters
    ----------
    clauses : Set[FrozenSet[Proposition]]
        Set of clauses to perform DPP on, clauses are assumed to be disjunctive
        
    Attributes
    ----------
    _clauses : Set[FrozenSet[Proposition]]
        Data field for the set of clauses
    _props : Set[Proposition]
        Set of unique propositions that appear in _clauses

    
    Methods
    -------
    prove()
        Performs DPP
    _get_props()
        Gets unique propositions for _props
    
    """
    
    def __init__(self, clauses: Set[FrozenSet[Proposition]]) -> None:
        self._clauses = clauses 
        self._props = self._get_props() 
    
    def prove(self) -> None:
        """Runs DPP"""
        
        S = self._clauses
        T = None
        U = None
        for p in self._props:
            S = _rm_pnp(S, p)
            T = _parent_set(S, p)
            U = _resolvent_set(T, p)
            S = (set(S) - set(T)) | set(U)
        print(S)
    
    def _get_props(self) -> Set[Proposition]:
        """Gets all unqiue propostions"""
        prop_names = set()
        for clause in self._clauses:
            for prop in clause:
                prop_names.add(prop.name)
        props = [Proposition(name, True) for name in prop_names]
        return props


def _has_pnp(clause: FrozenSet[Proposition], p: Proposition) -> bool:
    """Determins whether a clauses has both p and its complement (not p)"""
    val = 0
    for prop in clause:
        if (prop.name == p.name and prop.t == p.t):
            val += 1
            break
    for prop in clause:
        if (prop.name == p.name and prop.t != p.t):
            val += 1
            break
    return (val == 2)

def _rm_pnp(S: Set[FrozenSet[Proposition]], p: Proposition) -> Set[FrozenSet[Proposition]]:
    """Removes clauses that contain p and its complement from S"""
    S_prime = set()
    for clause in S:
         if not _has_pnp(clause, p):
            S_prime.add(clause)
    return S_prime

def _contains(clause: FrozenSet[Proposition], p: Proposition) -> bool:
    """Checks if p in is clause"""
    for prop in clause:
        if (Proposition.compare(prop, p) == 2):
            return True
    return False


def _resolution(C: FrozenSet[Proposition], D: FrozenSet[Proposition], p: Proposition) -> Union[FrozenSet[Proposition], None]:
    """Performs resolution deduction on C and D over p"""
    if (_contains(C, p) and _contains(D, p.negate())) or (_contains(C, p.negate()) and _contains(D, p)):
        resolvent = set(C | D)
        resolvent.remove(p)
        resolvent.remove(p.negate())
        return frozenset(resolvent)
    return None
    
def _parent_set(S: Set[FrozenSet[Proposition]], p: Proposition) -> Set[FrozenSet[Proposition]]:
    """Obtains the parent set (T) of S"""
    T = set()
    for clause in S:
        for prop in clause:
            if (prop.name == p.name):
                T.add(clause)
                break
    return T

def _resolvent_set(T: Set[FrozenSet[Proposition]], p: Proposition) -> Set[FrozenSet[Proposition]]:
    """Obtains the resolvent set (U) of T"""
    U = set()
    for pair in combinations(T, 2):
        C, D = pair
        resolvent = _resolution(C, D, p)
        if resolvent is not None:
           U.add(resolvent)
    return U
