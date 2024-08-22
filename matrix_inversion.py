import pandas as pd
import inspect

def get_functions(module):
    functions = []
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            print(obj)
            functions.append(name)
    return functions
# Get functions from the main pandas module
pandas_functions = get_functions(pd)
dataframe_functions = get_functions(pd.DataFrame)
series_functions = get_functions(pd.Series)
with open('pandas_functions.txt', 'w') as f:
    f.write("Pandas module functions:\n")
    f.write("\n".join(pandas_functions))
    f.write("\n\nDataFrame functions:\n")
    f.write("\n".join(dataframe_functions))
    f.write("\n\nSeries functions:\n")
    f.write("\n".join(series_functions))
