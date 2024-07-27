pseudo_groundtruth_prompt = """
Your goal is to convert molecular biology protocols into python pseudocode.

EXAMPLE
Here is an example of how to convert a protocol for {example_description}

example protocol:
{example protocol steps}

example python pseudocode:
{example_pseudofunctions}

# Protocol steps
{example_pseudocode}

YOUR TASK:
Here is a molecular biology protocol entitled '{title}' The protocol steps are as follows:
{protocol}

Please convert this protocol into python pseudocode. Please define the python functions you will \ 
use at the start of the pseudocode, and ensure that these functions have parameters where appropriate.

python pseudocode:
"""
