'''
    * Class to evaluate how often a stock moves a specific magnitude
    * Useful for market neutral strategies such as straddle/strangle trades
'''
class Evaluate:
    def __init__(self, current_stock_price):
        """
        Initialize the Evaluate class with the current stock price.
        :param current_stock_price: Current stock price (float)
        """
        self.current_stock_price = current_stock_price

    def calculate_call_cost(self, long_call_strike, long_call_cost, short_call_strike, short_call_cost):
        """
        Calculate the net cost of the call spread.
        :param long_call_strike: Strike price of the long call (float)
        :param long_call_cost: Cost of the long call (float)
        :param short_call_strike: Strike price of the short call (float)
        :param short_call_cost: Sale amount of the short call (float)
        :return: Net cost of the call spread (float)
        """
        return long_call_cost - short_call_cost

    def calculate_put_cost(self, long_put_strike, long_put_cost, short_put_strike, short_put_cost):
        """
        Calculate the net cost of the put spread.
        :param long_put_strike: Strike price of the long put (float)
        :param long_put_cost: Cost of the long put (float)
        :param short_put_strike: Strike price of the short put (float)
        :param short_put_cost: Sale amount of the short put (float)
        :return: Net cost of the put spread (float)
        """
        return long_put_cost - short_put_cost

    def calculate_break_even(self, long_call_strike, long_call_cost, short_call_strike, short_call_cost,
                             long_put_strike, long_put_cost, short_put_strike, short_put_cost):
        """
        Calculate the break-even percentages for both upside and downside.
        :param long_call_strike: Strike price of the long call (float)
        :param long_call_cost: Cost of the long call (float)
        :param short_call_strike: Strike price of the short call (float)
        :param short_call_cost: Sale amount of the short call (float)
        :param long_put_strike: Strike price of the long put (float)
        :param long_put_cost: Cost of the long put (float)
        :param short_put_strike: Strike price of the short put (float)
        :param short_put_cost: Sale amount of the short put (float)
        :return: Tuple containing break-even percentages (upside, downside)
        """
        # Calculate total cost of the call and put spreads
        call_cost = self.calculate_call_cost(long_call_strike, long_call_cost, short_call_strike, short_call_cost)
        put_cost = self.calculate_put_cost(long_put_strike, long_put_cost, short_put_strike, short_put_cost)
        total_cost = call_cost + put_cost
        
        break_even_percent_upside = (((long_call_strike + total_cost) 
            - self.current_stock_price)/self.current_stock_price)*100
        
        break_even_percent_downside = ((self.current_stock_price - 
                (long_put_strike - total_cost))/self.current_stock_price) * 100 

        #return break_even_upside, break_even_downside
        return break_even_percent_upside, break_even_percent_downside
    
    def get_min_max(self, _df,i,forward_values,attribute):
        end_index = min(i+forward_values,len(_df)-1)
        if attribute == "High":
            max_value = _df.loc[i:end_index,attribute].max()
            return max_value
        elif attribute == "Low":
            min_value = _df.loc[i:end_index,attribute].min()
            return min_value

    def compute_percent_change(self,start,end_val):
        _diff = end_val-start
        _percent = (_diff/start)*100
        return _percent
    
    def find_probability(self, df, upside_needed, downside_needed, num_days):
        '''
        :param df: the dataframe that holds the stock data
        :param upside_needed: the percentage we need to break even
        :param downside_needed: the percentage needed for the stock to go down to breakeven
        :param num_days: the number of days we need to look forward when finding out how many days
        :return: the number of times in the past the stock has moved X percent for the straddle/strangle to be profitable
        '''
        got_there = 0
        total = 0
        for i in range(len(df)-num_days):
            total += 1
            _close = df.iloc[i]["Close"]
            _upside = self.get_min_max(df,i,num_days,"High")
            _downside = self.get_min_max(df,i,num_days,"Low")
            _percentUp = self.compute_percent_change(_close,_upside)
            _percentDown = self.compute_percent_change(_close,_downside)
            if _percentUp >= upside_needed or _percentDown <= downside_needed:
                got_there += 1
        return total, got_there 