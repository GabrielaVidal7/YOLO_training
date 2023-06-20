import splitfolders

# Train: 70%    Val: 20%    Test: 10%s
splitfolders.ratio('Dataset/class1', output="Dataset/output", seed=1337, ratio=(0.7, 0.2, 0.1))
splitfolders.ratio('Dataset/class2', output="Dataset/outputlabels", seed=1337, ratio=(0.7, 0.2, 0.1))