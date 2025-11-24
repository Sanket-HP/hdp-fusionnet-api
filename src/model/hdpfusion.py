
import numpy as np

def tokenize(x):
    return x.lower().split()

def vectorize(tokens, dim=30):
    v = np.zeros(dim)
    for i, t in enumerate(tokens[:dim]):
        v[i] = len(t)
    return v

class HDPFusionNet:
    def process(self, text):
        tokens = tokenize(text)
        vec = vectorize(tokens)
        score = np.sum(vec)

        if score < 20:
            return "command"
        elif score < 40:
            return "warning"
        else:
            return "alert"
