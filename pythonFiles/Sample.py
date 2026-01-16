import pandas
import pandas as pd

#ex = {'B':[1,5], 'C':[2,6], 'D':[3,7], 'E':[4,8]}
#df = pandas.DataFrame(ex)
#print(df)

# ex = [[1,2,3,4], [5,6,7,8]]
# df = pandas.DataFrame(ex, columns=['B', 'C', 'D', 'E'])
# print(df)

# ex = [[1,5], [2,6], [3,7], [4,8]]
# df = pandas.DataFrame(ex).T
# df.columns = ['B', 'C', 'D', 'E']
# print(df)


s1 = pandas.Series([1,5], name='B')
s2 = pandas.Series([2,6], name='C')
s3 = pd.Series([3,7], name='D')
s4 = pd.Series([4,8], name='E')

df = pd.DataFrame([s1, s2, s3, s4]).T
print(df)

df = pd.concat([s1,s2,s3,s4], axis=1)
print(df)