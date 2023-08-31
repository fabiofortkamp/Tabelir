"""test_filenames.py - Assert that filenames are well formed."""
import itertools

import tabelir
from tabelir import Phase
from tabelir import SecondInput
from tabelir import ThermophysicalProperty


def test_can_access_second_inputs() -> None:
    """We can access the second inputs enumeration."""
    values = list(SecondInput)
    assert len(values) == 2

    assert SecondInput.ENTHALPY in SecondInput
    assert SecondInput.TEMPERATURE in SecondInput


def test_can_access_phase() -> None:
    """We can access all relevant phases."""
    possible_phases = [Phase.GAS, Phase.EQUIV_LIQUID, Phase.MIXTURE]

    assert set(possible_phases) == set(list(Phase))


def test_can_access_property() -> None:
    """We can access all relevant properties."""
    possible_props = {
        ThermophysicalProperty.DENSITY,
        ThermophysicalProperty.CP,
        ThermophysicalProperty.EXPANSIVITY,
        ThermophysicalProperty.INTERFACIAL_TENSION,
        ThermophysicalProperty.VISCOSITY,
        ThermophysicalProperty.CONDUCTIVITY,
        ThermophysicalProperty.ENTHALPY,
    }

    assert possible_props == set(list(ThermophysicalProperty))


def test_can_generate_filename() -> None:
    """Filenames are correctly formatted."""
    phases = list(Phase)
    second_inputs = list(SecondInput)
    properties = list(ThermophysicalProperty)

    for phase, si, prop in itertools.product(phases, second_inputs, properties):
        filename = tabelir.filename_from(si, phase, prop)

        assert filename == f"{si}_{phase}_{prop}.{tabelir.TABLE_EXTENSION}"

    # let's also check an individual case
    assert (
        tabelir.filename_from(
            SecondInput.ENTHALPY, Phase.EQUIV_LIQUID, ThermophysicalProperty.CP
        )
        == "enthalpy_equivLIQUID_cp.csv"
    )
