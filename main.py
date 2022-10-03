from itertools import chain
from chain import Chain 

chain = Chain(20)

for i in range(5):
    chain.Add_to_Pool(str(i))
    chain.mine()