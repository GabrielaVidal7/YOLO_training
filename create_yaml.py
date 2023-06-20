import yaml

data_yaml = dict(
    train = 'Dataset/train',
    val = 'Dataset/val',
    test = 'Dataset/test',
    nc = 4,
    names = ['car', 'person', 'motorcycle', 'truck']
)

with open('data.yaml', 'w') as outfile:
    yaml.dump(data_yaml, outfile, default_flow_style=True)