#sample sets for testing
#subset
set_a = {1,2,3}
#superset
set_b = {1,2,3,4,5,6}

class CheckSubset:
    def __init__(self, superset, subset):
        self.superset = superset
        self.subset = subset
    
    #static method as this a method for the class it's self
    @staticmethod
    def isSubset(self):
        dict = {}
        count = 0
        #iterate through the subset and check if the set element is in the superset and record the results in a dictionary
        for element in self.subset:
            if element in self.superset:
                dict[element] = True
            else:
                dict[element] = False
        #iterate though the dictionary and assign a point for true values and zero for false
        for key in dict:
            if dict[key] == True:
                count += 1
            else:
                count += 0
        #check if the number of true values match the number of elements in the subset (+1 is because it starts at zero) return true if matches return false if doesn't
        if count == self.subset.count() + 1:
            return True
        else:
            return False


