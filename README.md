# IshaPortfoliotest
Source Code for Portfolio Test


The following assumptions/mocking was done for the purpose of this exercise:
1.	I am assuming that the transaction history is sent to us in a dictionary format and has been hardcoded in main() for the purpose of this exercise.
The code can be amended to read it in this format if it is being sent in any other way.
2.	Only one type of portfolio is created
3.	All the historical transactions were tracked to find out the last holding of each instrument and a portfolio is made out of them
4.	FX conversion is not implemented in current state but methods are created which can be extended to have this functionality
5.	Assumed that current price is available to us. It has currently been hardcoded in the method implementation which is supposed to retrieve it in each instrument subclass
6.	Current value and PnL of each instrument is calculated at both instrument level and portfolio level.
7.	A very simple mock strategy for future transactions on the portfolio has been defined to test the process 
8.	The system doesn’t allow short positions
9.	Transaction cost has been added during PnL calculations at instrument level
