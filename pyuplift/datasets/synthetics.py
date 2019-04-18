import numpy as np
import pandas as pd


def load_linear(
        size: int,
        x1_params=(0, 100),
        x2_params=(0, 10),
        x3_params=(0, 100),
        t_params=(0, 2),
        e_params=(0, 100),
        eps=0.01,
        seed=777
):
    """The data generates by formula:
    Y' = X1+X2*T+E
    Y = Y', if Y' - int(Y') > eps,
    Y = 0,  otherwise.

    Statistics for default parameters:
    ================    ==============
    Features                         3
    Treatment                        2
    Samples total               `size`
    Y not equals 0             0.50562
    Y values               0 to 555.93
    ================    ==============

    Parameters
    ----------
    size : int
         The number of observations.
    x1_params : tuple(mu, sigma), default: (0, 100)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X1 ~ N(mu, sigma)
    x2_params : tuple(mu, sigma), default: (0, 10)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X2 ~ N(mu, sigma)
    x3_params : tuple(mu, sigma), default: (0, 100)
         The feature with gaussian distribution and mean=mu, sd=sigma.
         X3 ~ N(mu, sigma)
    t_params : tuple(min, max), default: (0, 2)
         The treatment with uniform distribution. Min value=min, Max value=max-1
         T ~ R(min, max)
    e_params : tuple(mu, sigma), default: (0, 100)
         The error with gaussian distribution and mean=mu, sd=sigma.
         E ~ N(mu, sigma)
    eps : float, default: 0.01
         The border value.
    seed : int, default: 777
         The random seed.
    Returns
    -------
    data : pandas DataFrame
    """

    np.random.seed(seed)
    x1 = np.random.normal(*x1_params, size)
    x2 = np.random.normal(*x2_params, size)
    x3 = np.random.normal(*x3_params, size)
    t = np.random.randint(*t_params, size)
    e = np.random.normal(*e_params, size)
    y_ = x1 + x2 * t + e
    y = []
    for value in y_:
        if value - int(value) > eps:
            y.append(value)
        else:
            y.append(0)
    y = np.array(y)
    return pd.DataFrame(data={
        'x1': x1,
        'x2': x2,
        'x3': x3,
        't': t,
        'y': y
    })
