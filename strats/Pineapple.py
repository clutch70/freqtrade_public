import freqtrade.vendor.qtpylib.indicators as qtpylib
import numpy as np
import talib.abstract as ta
from freqtrade.strategy import (IStrategy, informative, DecimalParameter)
from pandas import DataFrame, Series
import talib.abstract as ta
import math
import pandas_ta as pta
# from finta import TA as fta
import logging
from logging import FATAL

logger = logging.getLogger(__name__)


class Pineapple(IStrategy):
    def version(self) -> str:
        return "v0.0.1"

    INTERFACE_VERSION = 3

    #Enable buy conditions
    buy1 = True

    #Enable sell conditions
    sell1 = True

    # Hyperopt params
    min_roi = DecimalParameter(0.02, 0.2, decimals=2, default=0.05, space="buy")
    stoploss = DecimalParameter(-0.02, -0.2, decimals=2, default=-0.1, space="buy")
    buy_rsi = IntParameter(10, 40, default=30, space="buy")
    sell_rsi = IntParameter(60, 90, default=70, space="sell")

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['rsi'] = ta.RSI(dataframe, 14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        if self.buy1:
            conditions = []
            conditions.append(
                dataframe['rsi'] < self.buy_rsi.value
            )

        if conditions:
            dataframe.loc[
                reduce(lambda x, y: x & y, conditions),
                'enter_long'] = 1

        return DataFrame

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        if self.sell1:
            conditions = []
            conditions.append(
                dataframe['rsi'] > self.sell_rsi.value
            )

        if conditions:
            dataframe.loc[
                reduce(lambda x, y: x & y, conditions),
                'exit_long'] = 1

        return DataFrame