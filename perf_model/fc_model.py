import json

in_channel = list()
out_channel = list()
batch_size = list()
average_time = list()

with open("log/fc_0430_01:44:34.log", "r") as fp:
    for f in fp:
        decodes = json.loads(f)
        in_channel.append(decodes['image_shape'])
        out_channel.append(decodes['channel'])
        batch_size.append(decodes['batch_size'])
        average_time.append(decodes['average_time'])

print(len(in_channel), len(out_channel), len(batch_size), len(average_time))

    
