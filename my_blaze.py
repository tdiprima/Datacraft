from blaze import Data  

data = Data('postgresql://user:pass@localhost/db::table')  
print(data[data.amount > 100].amount.mean())
