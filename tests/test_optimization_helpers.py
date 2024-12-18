import numpy as np
import pytest

import aido
from aido.optimization_helpers import ParameterModule


@pytest.fixture
def parameter_dict():
    return aido.SimulationParameterDictionary([
        aido.SimulationParameter(
            "thickness_absorber",
            5.6,
            min_value=0.01,
            max_value=20.0,
            sigma=0.2,
            cost=1.1,
        ),
        aido.SimulationParameter(
            "thickness_scintillator",
            0.1,
            min_value=0.05,
            max_value=1.0,
            sigma=0.2,
            cost=5.0,
        ),
        aido.SimulationParameter(
            "absorber_material",
            "G4_Pb",
            discrete_values=["G4_Pb", "G4_W", "G4_Fe"],
            cost=[1.3, 0.26, 0.092],
        ),
        aido.SimulationParameter(
            "num_blocks",
            3,
            discrete_values=list(range(1, 10)),
            cost=(0.1 * np.arange(1, 10)).tolist(),
        ),
        aido.SimulationParameter("num_events", 200, optimizable=False),
    ])


def test_instantiation(parameter_dict):
    ParameterModule(parameter_dict)
