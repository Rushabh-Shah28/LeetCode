class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        phones = {"1":"" , "2":"abc" , "3":"def" , "4":"ghi" , "5":"jkl" , "6":"mno" , "7":"pqrs" , "8":"tuv" , "9":"wxyz"}
        solution  = []
        solution.append("")
        
        for digit in digits:
            if digit == "1":
                continue
            word = phones[digit]
            temp = []
            for alphabet in word:
                for s in solution:
                    temp.append(s+alphabet)
            solution = temp
        
        return solution
        """
        :type digits: str
        :rtype: List[str]
        """
        