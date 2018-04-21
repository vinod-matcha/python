class Memoize_fact(object):
    '''
    Encapsulating the factorial recursion function with Memoization.
    
    Attributes:
    num : number for which factorial value is to be returned. 
          required as the 'var' used in recursion funciton will have its value changed to base value at end of recursion
    memo : dictionary to store factorial values after they are calculated for first time
    '''
    
    def __init__(self, num = 0):
        self.num = num
        self.memo = {}
    
    def fact(self, var):
        """
        function to check&return or calculate if necessary the factorial value
        
        Attributes:
        var : var for which factorial is to be calculated
        """
        #assign var to class attribute
        self.num = var
        
        #check and return pre calculated factorial value
        if var in self.memo:
            print ('pre-calculated')
            return self.memo[var]
        else:
            #call private factorial function and store result in dictionay
            print ('store to memo', var, self.num)
            #self.num used, as var value will change to 1, at end of recursion
            self.memo[self.num] = self._fact_calc(var)
            
            #print result
            return self.memo[self.num]
    
    #define private function
    def _fact_calc(self, var):
        if var < 2:
            #base condition to return 1 and exit the recursion loop
            print ('Test Base condition', var, self.num)
            return 1
        else:
            #calculate factorial through recursion
            print ('calculate factorial', var, self.num)
            return var * self._fact_calc(var - 1)
