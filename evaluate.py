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