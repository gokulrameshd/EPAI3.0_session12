from math import *
from objective1 import *


class Polygons: 
    "Iterable Class"
    def __init__(self, m, R):
        self._m = m-2
        self._R = R
    def __len__(self):
        return self._m 

    def __getitem__(self, i):
        print(i)
        if i+3 >= self._m:
            raise StopIteration
        else:
#             [Polygon(i, R) for i in range(3, m+1)]
            print(self._m,Polygon(i+3 ,self._R))
            return Polygon(i+3 ,self._R)
            
class PolygonsIterator:
    "Iterator class"
    def __init__(self, m, R):
        self._polygons = Polygons(m ,R)
        print(len(self._polygons))
        self._i = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._i >= len(self._polygons):
            raise StopIteration
        else:
            result = self._polygons[self._i]
            self._i += 1
            return result
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]
    
