from coin import Coin
from d4 import D4
from d6 import D6
from dicebag import DiceBag

myDiceBag = DiceBag()
myDiceBag.add(D6())
myDiceBag.add(D6())
myDiceBag.add(D6())
myDiceBag.add(D4())

mySubDiceBag = DiceBag()
mySubDiceBag.add(Coin())
mySubDiceBag.add(Coin())
mySubDiceBag.add(Coin())

myDiceBag.add(mySubDiceBag)
for i in range(20):
    print(myDiceBag.roll())
    print(myDiceBag.prettyRoll())
