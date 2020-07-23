import pandas as pd
from sqlalchemy import create_engine


# Create dataframe
data=pd.DataFrame({
    'name':['gaurav','alok','abhi'],
    'address':['vns','basaratpur','prayagraj']
})

print(data)



# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="9696",
                               db="business"))


data.to_sql(con = engine, name='customers', if_exists = 'append', chunksize = 1000) 



