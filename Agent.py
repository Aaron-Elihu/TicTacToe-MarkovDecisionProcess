from Algorithms import ValueIteration, PolicyIteration
import json

#  Value Iteration
agent = ValueIteration()
agent.value_iteration()

policy = {}
for p in agent.policy:
    policy[str(p)] = agent.policy[p]
with open("OptimalPolicy/valueIteration.json", "w") as json_file:
    json.dump(policy, json_file)

#  Policy Iteration
agent = PolicyIteration()
agent.policy_iteration()

policy = {}
for p in agent.policy:
    policy[str(p)] = agent.policy[p]
with open("OptimalPolicy/policyIteration.json", "w") as json_file:
    policy_json = {str(state): int(agent.policy[state]) if agent.policy[state] is not None else None for state in agent.policy}
    json.dump(policy_json, json_file)
