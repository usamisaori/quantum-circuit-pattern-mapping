import sys
sys.path.append('../')

from qcpm.migration import convert
import json


paths = [
    ['../qcpm/optimization/rules/', '/hadamard.json'],
    ['../qcpm/optimization/rules/', '/commutation.json'],
    ['../qcpm/optimization/rules/', '/reversible.json'],
    ['../qcpm/pattern/rules/', '/pattern.json'],
    ['../qcpm/expander/rules/', '/expansion.json'],
]

target = 'Surface'

for path in paths:
    pattern_path = path[0] + 'IBM' + path[1]
    target_path = path[0] + target + path[1]

    with open(pattern_path, 'r') as file:
        patterns = json.load(file)

    with open(target_path, 'w') as file:
        json.dump(convert(patterns, target), file)