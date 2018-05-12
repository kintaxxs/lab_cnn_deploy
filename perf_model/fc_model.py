import json
from utils.parse import parse

in_channel = list()
out_channel = list()
batch_size = list()
average_time = list()

records = {'in_channel':[], 'out_channel':[], 'batch_size':[], 'average_time':[]}

with open("log/fc_0430_01:44:34.log", "r") as fp:
    for f in fp:
        decodes = json.loads(f)
        records['in_channel'].append(decodes['image_shape'])
        records['out_channel'].append(decodes['channel'])
        records['batch_size'].append(decodes['batch_size'])
        records['average_time'].append(decodes['average_time'])

print(len(records['in_channel']), len(records['out_channel']), len(records['batch_size']), len(records['average_time']))

mac = parse(records)

#print(mac)

print(type(records['in_channel']))

in_channel = np.array(records['in_channel'])
out_channel = np.array(records['in_channel'])
batch_size = np.array(records['batch_size'])
average_time = np.array(records['average_time'])

    
