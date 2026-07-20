from collections import defaultdict


class DataStore(dict):
    """Centralized store for HNN session data."""

    ## Avoid accidentaal reinitilizations
    _initialized = False

    def __init__(self):

        if DataStore._initialized:
            return
        super().__init__(
            {
                "run_simulations": defaultdict(lambda: dict(net=None, dpls=list())),
                "loaded_data": defaultdict(lambda: dict(net=None, dpls=list())),
                "networks": {},
            }
        )
        DataStore._initialized = True

    @property
    def run_simulations(self):
        return self["run_simulations"]

    @property
    def run_simulation_names(self):
        return self["run_simulations"].keys()

    @property
    def loaded_data_names(self):
        return self["loaded_data"].keys()

    @property
    def loaded_data(self):
        return self["loaded_data"]

    @property
    def networks(self):
        return self["networks"]

    @property
    def all_simulation_names(self):
        return list(self["run_simulations"].keys()) + list(self["loaded_data"].keys())


# Module-level singleton should be imported by classes that
# want to save data in DataStore
data_store = DataStore()
