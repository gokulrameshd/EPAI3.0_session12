import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self._area = None
        self._interior_angle = None
        self._apothem = None
        self._side_length = None
        self._perimeter = None
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        if self._interior_angle == None :
            print("interior angle calculated!!")
            self._interior_angle = (self._n - 2) * 180 / self._n
            return self._interior_angle
        else :
            return _interior_angle
    @property
    def side_length(self):
        if self._side_length == None :
            print("side length calculated!!")
            self._side_length = 2 * self._R * math.sin(math.pi / self._n)
            return self._side_length
        else:
            return self._side_length
    
    @property
    def apothem(self):
        if self._apothem == None : 
            print("apothem calculated!!")
            self._apothem = self._R * math.cos(math.pi / self._n)
            return self._apothem
        else : 
            return self._apothem
    
    @property
    def area(self):
        if self._area == None:
            print("area calculated!!")
            self._area = self._n / 2 * self.side_length * self.apothem
            return self._area
        else :
            return self._area
    
    @property
    def perimeter(self):
        if self._perimeter == None:
            print("perimeter calculated!!")
            self._perimeter = self._n * self.side_length
            return self._perimeter
        else:
            return self._perimeter
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented