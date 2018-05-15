import json
from utils.parse import parse

import pandas as pd
from rpy2 import robjects as ro
from rpy2.robjects import pandas2ri
import random
import numpy as np
pandas2ri.activate()
R = ro.r

in_channel = list()
out_channel = list()
batch_size = list()
average_time = list()

records = {'in_channel':[], 'out_channel':[], 'batch_size':[], 'average_time':[]}

with open("log/fc_2.log", "r") as fp:
    for f in fp:
        decodes = json.loads(f)
        records['in_channel'].append(decodes['image_shape'])
        records['out_channel'].append(decodes['channel'])
        records['batch_size'].append(decodes['batch_size'])
        records['average_time'].append(float(decodes['average_time']))

print(len(records['in_channel']), len(records['out_channel']), len(records['batch_size']), len(records['average_time']))

mac = parse(records)

in_channel = np.array(records['in_channel'])
out_channel = np.array(records['out_channel'])
batch_size = np.array(records['batch_size'])
average_time = np.array(records['average_time'])

df = pd.DataFrame({'in_channel': in_channel,
                   'out_channel': out_channel,
                   'batch_size': batch_size,
                   'average_time': average_time})

#df['in_channel'] = df['in_channel'].map(lambda x: (x-df['in_channel'].mean()) / df['in_channel'].std())
#df['out_channel'] = df['out_channel'].map(lambda x: (x-df['out_channel'].mean()) / df['out_channel'].std())
#df['batch_size'] = df['batch_size'].map(lambda x: (x-df['batch_size'].mean()) / df['batch_size'].std())
#df['average_time'] = df['average_time'].map(lambda x: (x-df['average_time'].mean()) / df['average_time'].std())

M = R.lm('average_time ~ polym(in_channel, out_channel, degree=2, raw=TRUE)', data=df)

print(R.summary(M))
print(R.coefficients(M))

