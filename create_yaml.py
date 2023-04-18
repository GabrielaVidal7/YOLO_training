import yaml

data_yaml = dict(
    train = 'Dataset_1/train',
    val = 'Dataset_1/val',
    # test = 'Dataset/test',
    nc = 1,
    names = ['car']
)

with open('data.yaml', 'w') as outfile:
    yaml.dump(data_yaml, outfile, default_flow_style=True)