from itertools import combinations


class StringClass:
    def __init__(self):
        self.str = "12314532"
        self.str1 = "45211834"

    def lengthOfString(self):
        print(len(self.str))

    def stringToChar(self):
        print(list(self.str))


class PairsPossible(StringClass):
    def listOfPairs(self):
        res = list(combinations(self.str, 2))
        print(res)


class SearchCommonElements(StringClass):
    arr = []

    def commonEle(self):
        dict = {}
        for char in self.str:
            if char in dict:
                continue
            else:
                dict[char] = 1
        for char in self.str1:
            if char in dict:
                self.arr.append(char)

        for key, val in dict.items():
            print(key + " ")

    def printList(self):
        print(self.arr)

class EqualSumPairs(PairsPossible):
    def same_sum(self):
        sumOfPairs = [];
        x = map(int,list(self.str))
        self.res = list(combinations(x,2))
        for i in self.res:
            sumOfPairs.append(sum(i))
        sumOfPairs = set(sumOfPairs)
        print(len(sumOfPairs))


obj = StringClass()
obj.lengthOfString()
obj.stringToChar()
obj1 = PairsPossible()
obj1.listOfPairs()
obj2 = SearchCommonElements()
obj2.commonEle()
obj2.printList()
obj3 = EqualSumPairs()
obj3.same_sum()