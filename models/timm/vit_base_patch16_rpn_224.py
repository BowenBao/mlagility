# labels: name::vit_base_patch16_rpn_224 author::timm task::computer_vision
import torch
import timm
from mlagility.parser import parse

# Parsing command-line arguments
batch_size = parse(["batch_size"])

# Creating model and set it to evaluation mode
model = timm.create_model("vit_base_patch16_rpn_224", pretrained = False)
model.eval()

# Creating inputs
input_size = model.default_cfg["input_size"]
batched_input_size = tuple(batch_size) + input_size
inputs = torch.rand(batched_input_size)

# Calling model
model(inputs)