import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    N, d = X.shape
    w=np.zeros(X.shape[1])
    b=0
    
    for _ in range(steps):
            
        z=np.dot(X,w) + b
        p=_sigmoid(z)
    
        #loss funtion
        eps=1e-15
        p=np.clip(p,eps,1-eps)
        N=len(y)

        loss= -(1/N) * np.sum(y*np.log(p) + (1-y)*np.log(1-p))

        dw = np.dot(X.T, (p - y)) / N
        db = np.mean(p - y)

        w=w-(lr*dw)
        b=b-(lr*db)
        
    return w,b