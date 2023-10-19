from proposition import *
from typing import Set, FrozenSet, Union
from itertools import combinations

class DPP():
    def __init__(self, clauses: Set[FrozenSet[Proposition]]) -> None:
        self._clauses = clauses 
        self._props = self._get_props()
    
    @staticmethod
    def _has_pnp(clause: FrozenSet[Proposition], p: Proposition) -> bool:
        val = 0
        for prop in clause:
            if (prop.name == p.name and prop.negation == p.negation):
                val += 1
                break
        for prop in clause:
            if (prop.name == p.name and prop.negation != p.negation):
                val += 1
                break
        return (val == 2)
    
    @staticmethod
    def _rm_pnp(S: Set[FrozenSet[Proposition]], p: Proposition) -> Set[FrozenSet[Proposition]]:
        ans = set()
        for clause in S:
            if not DPP._has_pnp(clause, p):
                ans.add(clause)
        return ans
    
    @staticmethod
    def _parent_set(S: Set[FrozenSet[Proposition]], p: Proposition) -> Set[FrozenSet[Proposition]]:
        T = set()
        for clause in S:
            for prop in clause:
                if (prop.name == p.name):
                    T.add(clause)
                    break
        return frozenset(T)
    
    @staticmethod
    def _resolution(C: FrozenSet[Proposition], D: FrozenSet[Proposition], p: Proposition) -> Union[FrozenSet[Proposition], None]:
        if (p in C and (not p) in D) or ((not p) in C and p in D):
            resolvent = (set(C) | set(D)) - {p, not p}
            return frozenset(resolvent)
        return None

    @staticmethod
    def _resolvent_set(T: Set[FrozenSet[Proposition]], p: Proposition) -> Set[FrozenSet[Proposition]]:
        U = set()
        for pair in combinations(T, 2):
            C, D = pair
            resolvent = DPP._resolution(C, D, p)
            if resolvent is not None:
                U.add(resolvent)
        return frozenset(U)
    
    def _get_props(self) -> Set[Proposition]:
        prop_names = set()
        for clause in self._clauses:
            for prop in clause:
                prop_names.add(prop.name)
        props = [Proposition(name, True) for name in prop_names]
        return props

    def prove(self) -> Set[FrozenSet[Proposition]]:
        S = self._clauses
        T = None
        U = None
        for p in self._props:
            S = DPP._rm_pnp(S, p)
            T = DPP._parent_set(S, p)
            U = DPP._resolvent_set(T, p)
            S = (S - T) | U
        print(S)
