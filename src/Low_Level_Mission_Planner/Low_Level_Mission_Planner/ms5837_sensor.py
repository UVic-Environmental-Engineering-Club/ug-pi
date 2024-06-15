"""
    Originally from https://github.com/bluerobotics/ms5837-python/blob/master/example.py

    Modifications by:
        Anthony Cieri penguinmillion@gmail.com

    This is a dummy sensor driver script
    FOR DEMOS ONLY
"""

import time
import math
import random

# Models
MODEL_02BA = 0
MODEL_30BA = 1

# Oversampling options
OSR_256 = 0
OSR_512 = 1
OSR_1024 = 2
OSR_2048 = 3
OSR_4096 = 4
OSR_8192 = 5

# kg/m^3 convenience
DENSITY_FRESHWATER = 997
DENSITY_SALTWATER = 1029

# Conversion factors (from native unit, mbar)
UNITS_Pa = 100.0
UNITS_hPa = 1.0
UNITS_kPa = 0.1
UNITS_mbar = 1.0
UNITS_bar = 0.001
UNITS_atm = 0.000986923
UNITS_Torr = 0.750062
UNITS_psi = 0.014503773773022

# Valid units
UNITS_Centigrade = 1
UNITS_Farenheit = 2
UNITS_Kelvin = 3


class MS5837(object):

    # Registers
    _MS5837_ADDR = 0x76
    _MS5837_RESET = 0x1E
    _MS5837_ADC_READ = 0x00
    _MS5837_PROM_READ = 0xA0
    _MS5837_CONVERT_D1_256 = 0x40
    _MS5837_CONVERT_D2_256 = 0x50

    def __init__(self, model=MODEL_30BA):
        self._model = model

        self._fluidDensity = DENSITY_FRESHWATER
        self._pressure = 0
        self._temperature = 0
        self._D1 = 0
        self._D2 = 0

    def init(self) -> bool:
        random.seed(time.time)

        return True

    def read(self, oversampling=OSR_8192) -> bool:
        # Maximum conversion time increases linearly with oversampling
        # max time (seconds) ~= 2.2e-6(x) where x = OSR = (2^8, 2^9, ..., 2^13)
        # We use 2.5e-6 for some overhead
        time.sleep(2.5e-6 * 2 ** (8 + oversampling))

        time.sleep(2.5e-6 * 2 ** (8 + oversampling))

        self._calculate()

        return True

    def setFluidDensity(self, denisty) -> None:
        self._fluidDensity = denisty

    # Pressure in requested units
    # mbar * conversion
    def pressure(self, conversion=UNITS_mbar) -> float:
        return self._pressure * conversion

    # Temperature in requested units
    # default degrees C
    def temperature(self, conversion=UNITS_Centigrade) -> float:
        degC = self._temperature / 100.0
        if conversion == UNITS_Farenheit:
            return (9.0 / 5.0) * degC + 32
        elif conversion == UNITS_Kelvin:
            return degC + 273
        return degC

    # Depth relative to MSL pressure in given fluid density
    def depth(self) -> float:
        return (self.pressure(UNITS_Pa) - 101300) / (self._fluidDensity * 9.80665)

    # Altitude relative to MSL pressure
    def altitude(self) -> float:
        return (1 - pow((self.pressure() / 1013.25), 0.190284)) * 145366.45 * 0.3048

    # Noisy sine wave
    def _calculate(self) -> None:
        self._pressure = (
            random.random() * 0.1 + math.sin(time.time() * math.pi * 0.1) * 0.4
        ) * 100000


class MS5837_30BA(MS5837):
    def __init__(self, bus=1) -> None:
        MS5837.__init__(self, MODEL_30BA)


class MS5837_02BA(MS5837):
    def __init__(self, bus=1) -> None:
        MS5837.__init__(self, MODEL_02BA)
