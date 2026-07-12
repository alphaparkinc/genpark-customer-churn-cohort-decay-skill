class CustomerChurnCohortDecayClient:
    def estimate_decay(self, initial_size: int, decay_rate: float) -> dict:
        return {"remaining_users": int(initial_size * (1.0 - decay_rate))}