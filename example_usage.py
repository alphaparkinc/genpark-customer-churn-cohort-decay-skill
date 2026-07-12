from client import CustomerChurnCohortDecayClient
client = CustomerChurnCohortDecayClient()
print(client.estimate_decay(1000, 0.15))