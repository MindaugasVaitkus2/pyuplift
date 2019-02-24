class BaseModel:
    """Base class for uplift models.
    Warning: This class should not be used directly. Use derived classes instead.
    """

    def fit(self, x, y, t):
        """Build a TwoModel approach from the training set (x, y, t).

        Parameters
        ----------
        x : numpy array of shape = [n_samples, n_features]
            The training input samples.
        y : numpy array of shape = [n_samples] or [n_samples, n_outputs]
            The target values (class labels in classification, real numbers in regression).
        t : numpy array of shape = [n_samples] or [n_samples, n_outputs]
            The treatments.
        Returns
        -------
        self : object
        """
        return self

    def predict(self, x, t) -> [float]:
        """Predict treatment effect for x.

        Parameters
        ----------
        x : numpy array of shape = [n_samples, n_features]
            The input samples.
        t : numpy array of shape = [n_samples, n_features]
            The treatments.
        Returns
        -------
        y : array of shape = [n_samples] or [n_samples, n_outputs]
            The predicted treatment effect.
        """
        pass
