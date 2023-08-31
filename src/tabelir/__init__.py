"""Tabelir."""
from enum import Enum

from tabelir.app import TabelirApp


class SecondInput(Enum):
    """A SecondInput is one of the possible second inputs to properties."""

    ENTHALPY = "enthalpy"
    TEMPERATURE = "temperature"

    def __str__(self) -> str:
        """Generate the string representation."""
        return self.value


class Phase(Enum):
    """A Phase is one of the possible phases a fluid can be in."""

    GAS = "GAS"
    EQUIV_LIQUID = "equivLIQUID"
    MIXTURE = "MIXTURE"

    def __str__(self) -> str:
        """Generate the string representation."""
        return self.value


class ThermophysicalProperty(Enum):
    """A ThermophysicalProperty is one of the properties tabelir can calculate."""

    DENSITY = "density"
    CP = "cp"
    EXPANSIVITY = "expansivity"
    INTERFACIAL_TENSION = "interfacial_tension"
    VISCOSITY = "viscosity"
    CONDUCTIVITY = "conductivity"
    ENTHALPY = "enthalpy"

    def __str__(self) -> str:
        """Generate the string representation."""
        return self.value


TABLE_EXTENSION = "csv"


def filename_from(si: SecondInput, phase: Phase, prop: ThermophysicalProperty) -> str:
    """Generate filename for the given case.

    Args:
        si (SecondInput): the second input (besides pressure) of the table
        phase (Phase): phase of the fluid
        prop (ThermophysicalProperty): property that is being calculated

    Returns:
        str: the formatted filename, ready to be created and written to
    """
    return f"{si}_{phase}_{prop}.{TABLE_EXTENSION}"


# T_values = np.linspace(273.15, 423.15, 50)
# P_values = np.linspace(1e5, 2e8, 50)
N_PRESSURE_POINTS = 50
N_SECOND_INPUT_POINTS = 50


__all__ = [
    "TabelirApp",
    "SecondInput",
    "Phase",
    "ThermophysicalProperty",
    "filename_from",
    "TABLE_EXTENSION",
]
