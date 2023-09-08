#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur May 26 22:09:19 2022

@author: Andrew Ostensen

"""


def string_conversion(data, col_name, output="int"):
    import pandas as pd

    """
    Given a dataframe, a col_name and an output data type, return a dataframe
    that has transformed the datatype in the column from a string to either
    an int or a float.

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to sample from
    col_name : str
        The dataframe column to modify
    output : str, optional
        The datatype to convert to. The default is an int64.
        Valid entries are 'int' or 'float'

    Returns
    -------
    pandas.core.frame.DataFrame
        A dataframe with the column datatype transformed.

    Raises
    ------
    TypeError
        If the input argument 'data' is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument 'col_name' is not in the data columns
    AssertError
        If the input argument 'output' is not either 'int' or 'float'

    Examples
    --------
    >>> string_conversion(helper_data, 'cost')
        vehicle             year  cost
    0    Toyota Highlander  2014  32777
    1    Nissan Frontier    2017  18899
    """

    # Checks if a dataframe is the type of object being passed into the
    # data argument
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")

    # Tests that the the column is in the dataframe
    assert (
        col_name in data.columns
    ), "The specified column does not exist in the dataframe"

    # Tests that the the output argument is either 'int' or 'float'
    assert (
        output == "int" or output == "float"
    ), "The output argument can only be 'int' or 'float'"

    # replace '$' and ','
    data[col_name] = (
        data[col_name]
        .str.replace(r"$", "", regex=False)
        .str.replace(r",", "", regex=False)
    )

    # change to 'int' or 'float'
    if output == "int":
        data = data.assign(column=data[col_name].astype("int64")).drop(
            columns=[col_name]
        )
    else:
        data = data.assign(column=data[col_name].astype("float64")).drop(
            columns=[col_name]
        )

    # rename the new modified 'column' back to the original name
    data = data.rename(columns={"column": col_name})

    # return the result
    return data
