import splitfolders

splitfolders.ratio('Dataset/val/images', output="output", seed=1337, ratio=(.8, 0.2, 0.0))
splitfolders.ratio('Dataset/val/labels', output="output", seed=1337, ratio=(.8, 0.2, 0.0))