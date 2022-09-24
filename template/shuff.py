import numpy as np
from sklearn.model_selection import train_test_split

with open("post.txt","r") as f:
    post = f.readlines()

with open("pre.txt","r") as f:
    pre = f.readlines()

import random
random.seed(0)

NUM_ROWS = len(post)
TEST_SIZE = 0.1
indices = np.arange(NUM_ROWS)

# usual train-val split
train_idx, val_idx = train_test_split(indices, test_size=TEST_SIZE, train_size=None)

post = np.array(post)
pre = np.array(pre)

print(NUM_ROWS)

posttrain = post[train_idx]
pretrain = pre[train_idx]

postval = post[val_idx]
preval = pre[val_idx]
print(val_idx)
print(preval[0:5],postval[0:5])
f=open('data/train.tok.preGOC','w')
g=open('data/train.tok.postGOC','w')

for pre1, post1 in zip(list(pretrain),list(posttrain)):
    f.write(pre1)
    g.write(post1)

f.close()
g.close()

f=open('data/dev.tok.preGOC','w')
g=open('data/dev.tok.postGOC','w')


for pre1, post1 in zip(list(preval),list(postval)):
    f.write(pre1)
    g.write(post1)

f.close()
g.close()
