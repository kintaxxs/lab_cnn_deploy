def parse(records):
    mac = list()
    for i in range(len(records['in_channel'])):
        mac.append(records['in_channel'][i] * records['out_channel'][i])
        #print(records['in_channel'][i], records['out_channel'][i])
    return mac
