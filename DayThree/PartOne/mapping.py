class Mapper():
    _map_sum = 0
    _myMap = dict()

    def __init__(self):
        # Loop & create add to the map
        j = 0

        for i in range(97, 123):
            j += 1
            self._myMap[chr(i)] = j

        for i in range(65, 91):
            j += 1
            self._myMap[chr(i)] = j

    def get_map(self):
        return self._myMap

    def inc_total_priorities(self, char):
        if(char == '' or char == None or char == ' '):
            return
        val = self._myMap.get(char)

        self._map_sum += val

    def get_priority_total(self):
        return self._map_sum
