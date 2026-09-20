'''
Return path generator
'''
import numpy as np
class ReturnPathGenerator:
    def __init__(self,annual_mu,annual_vol,no_periods):
        self.T = no_periods
        self.annual_mu = annual_mu
        self.annual_vol = annual_vol
        self.results = []

    
    def per_period_moments(self):
        '''
        returns per period first and second moments
        '''
        self.pp1m = self.annual_mu/self.T
        self.pp2m = self.annual_vol/np.sqrt(self.T)
        return self.pp1m, self.pp2m


    def get_return_path(self,n_simulations,horizon):

        pp1m, pp2m = self.per_period_moments()

        self.return_path = np.random.normal(pp1m, pp2m,
            size=(n_simulations, horizon)
        )
        return self.return_path

    def summary_statistics(self,starting_wealth = 1):
        
        wealth = starting_wealth * np.prod(1 + self.return_path, axis=1)
        
        
        percentiles = np.percentile(wealth,[25,50,75])
    
        result = {
            "mean_wealth": wealth.mean(),
            "25th percentile wealth": percentiles[0],
            "50th percentile wealth": percentiles[1],
            "75th percentile wealth": percentiles[2],
            "mean_log_growth": np.mean(
                np.sum(np.log1p(self.return_path), axis=1)
            )
        }

        self.results.append(result)

        return result