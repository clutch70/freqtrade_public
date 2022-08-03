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

    # Hyperopt params
    min_roi = DecimalParameter(0.02, 0.2, decimals=2, default=0.05, space="buy")
    stoploss = DecimalParameter(-0.02, -0.2, decimals=2, default=-0.1, space="buy")

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['rsi'] = ta.RSI(dataframe, 14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        return DataFrame

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        return DataFrame