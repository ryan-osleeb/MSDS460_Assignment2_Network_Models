#!/usr/bin/env python
# coding: utf-8

# In[43]:


from pulp import *
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


# In[44]:


##Expected Time

# Create a dictionary of the activities and their durations
activities = {'A':4, 'B':8, 'C':5, 'D1':10, 'D2':10, 'D3':12, 'D4':50, 'D5':10, 'D6':15, 'D7':15, 'D8':8, 'E':12, 'F':10, 'G':10, 'H':14}

# Create a list of the activities
activities_list = list(activities.keys())

# Create a dictionary of the activity precedences
precedences = {'A': [], 'B': [], 'C': ['A'], 'D1': ['A'], 'D2': ['D1'], 'D3': ['D1'], 'D4': ['D2','D3'], 'D5': ['D4'], 'D6': ['D4'], 'D7': ['D6'], 'D8': ['D5','D7'], 'E': ['B','C'], 'F': ['D8','E'], 'G': ['A','D8'], 'H': ['F','G']}

# Create the LP problem
prob = LpProblem("Critical Path", LpMinimize)

# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in activities_list}

# Add the constraints
for activity in activities_list:
    prob += end_times[activity] == start_times[activity] + activities[activity], f"{activity}_duration"
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor], f"{activity}_predecessor_{predecessor}"

# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]), "minimize_end_times"

# Solve the LP problem
status = prob.solve()

# Print the results
print("Critical Path time:")
for activity in activities_list:
    if value(start_times[activity]) == 0:
        print(f"{activity} starts at time 0")
    if value(end_times[activity]) == max([value(end_times[activity]) for activity in activities_list]):
        print(f"{activity} ends at {value(end_times[activity])} hours in duration")

# Print solution
print("\nSolution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)


# In[45]:


# Define the data
tasks = [
    {"Task": "A", "Start": 0, "Duration": 4},
    {"Task": "B", "Start": 0, "Duration": 8},
    {"Task": "C", "Start": 4, "Duration": 5},
    {"Task": "D1", "Start": 4, "Duration": 10},
    {"Task": "D2", "Start": 14, "Duration": 10},
    {"Task": "D3", "Start": 14, "Duration": 12},
    {"Task": "D4", "Start": 26, "Duration": 50},
    {"Task": "D5", "Start": 76, "Duration": 10},
    {"Task": "D6", "Start": 76, "Duration": 15},
    {"Task": "D7", "Start": 91, "Duration": 15},
    {"Task": "D8", "Start": 106, "Duration": 8},
    {"Task": "E", "Start": 9, "Duration": 12},
    {"Task": "F", "Start": 114, "Duration": 10},
    {"Task": "G", "Start": 114, "Duration": 10},
    {"Task": "H", "Start": 124, "Duration": 14}
]

fig, ax = plt.subplots()

# Create bars for the Gantt chart
for i, task in enumerate(tasks):
    start = task["Start"]
    duration = task["Duration"]
    ax.broken_barh([(start, duration)], (i - 0.4, 0.8), facecolors='tab:blue')

# Setting labels and grid
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([task["Task"] for task in tasks])
ax.set_xlabel('Hours')
ax.set_ylabel('Tasks')
ax.set_title('Expected Time')
ax.grid(True)

# Format the x-axis
#plt.xticks(np.arange(0, max(task["Start"] + task["Duration"] for task in tasks) + 1, 1))

plt.show()


# In[46]:


##Best Case Hours

# Create a dictionary of the activities and their durations
activities = {'A':2, 'B':4, 'C':2, 'D1':4, 'D2':4, 'D3':4, 'D4':20, 'D5':4, 'D6':6, 'D7':6, 'D8':4, 'E':4, 'F':4, 'G':4, 'H':6}

# Create a list of the activities
activities_list = list(activities.keys())

# Create a dictionary of the activity precedences
precedences = {'A': [], 'B': [], 'C': ['A'], 'D1': ['A'], 'D2': ['D1'], 'D3': ['D1'], 'D4': ['D2','D3'], 'D5': ['D4'], 'D6': ['D4'], 'D7': ['D6'], 'D8': ['D5','D7'], 'E': ['B','C'], 'F': ['D8','E'], 'G': ['A','D8'], 'H': ['F','G']}

# Create the LP problem
prob = LpProblem("Critical Path", LpMinimize)

# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in activities_list}

# Add the constraints
for activity in activities_list:
    prob += end_times[activity] == start_times[activity] + activities[activity], f"{activity}_duration"
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor], f"{activity}_predecessor_{predecessor}"

# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]), "minimize_end_times"

# Solve the LP problem
status = prob.solve()

# Print the results
print("Critical Path time:")
for activity in activities_list:
    if value(start_times[activity]) == 0:
        print(f"{activity} starts at time 0")
    if value(end_times[activity]) == max([value(end_times[activity]) for activity in activities_list]):
        print(f"{activity} ends at {value(end_times[activity])} hours in duration")

# Print solution
print("\nSolution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)


# In[47]:


# Define the data
tasks = [
    {"Task": "A", "Start": 0, "Duration": 2},
    {"Task": "B", "Start": 0, "Duration": 4},
    {"Task": "C", "Start": 2, "Duration": 2},
    {"Task": "D1", "Start": 2, "Duration": 4},
    {"Task": "D2", "Start": 6, "Duration": 4},
    {"Task": "D3", "Start": 6, "Duration": 4},
    {"Task": "D4", "Start": 10, "Duration": 20},
    {"Task": "D5", "Start": 30, "Duration": 4},
    {"Task": "D6", "Start": 30, "Duration": 6},
    {"Task": "D7", "Start": 36, "Duration": 6},
    {"Task": "D8", "Start": 42, "Duration": 4},
    {"Task": "E", "Start": 4, "Duration": 4},
    {"Task": "F", "Start": 46, "Duration": 4},
    {"Task": "G", "Start": 46, "Duration": 4},
    {"Task": "H", "Start": 50, "Duration": 6}
]

fig, ax = plt.subplots()

# Create bars for the Gantt chart
for i, task in enumerate(tasks):
    start = task["Start"]
    duration = task["Duration"]
    ax.broken_barh([(start, duration)], (i - 0.4, 0.8), facecolors='tab:blue')

# Setting labels and grid
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([task["Task"] for task in tasks])
ax.set_xlabel('Hours')
ax.set_ylabel('Tasks')
ax.set_title('Best Case')
ax.grid(True)

# Format the x-axis
#plt.xticks(np.arange(0, max(task["Start"] + task["Duration"] for task in tasks) + 1, 1))

plt.show()


# In[48]:


##Worst Case Hours

# Create a dictionary of the activities and their durations
activities = {'A':8, 'B':16, 'C':10, 'D1':20, 'D2':20, 'D3':24, 'D4':100, 'D5':20, 'D6':30, 'D7':30, 'D8':16, 'E':24, 'F':20, 'G':20, 'H':28}

# Create a list of the activities
activities_list = list(activities.keys())

# Create a dictionary of the activity precedences
precedences = {'A': [], 'B': [], 'C': ['A'], 'D1': ['A'], 'D2': ['D1'], 'D3': ['D1'], 'D4': ['D2','D3'], 'D5': ['D4'], 'D6': ['D4'], 'D7': ['D6'], 'D8': ['D5','D7'], 'E': ['B','C'], 'F': ['D8','E'], 'G': ['A','D8'], 'H': ['F','G']}

# Create the LP problem
prob = LpProblem("Critical Path", LpMinimize)

# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in activities_list}

# Add the constraints
for activity in activities_list:
    prob += end_times[activity] == start_times[activity] + activities[activity], f"{activity}_duration"
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor], f"{activity}_predecessor_{predecessor}"

# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]), "minimize_end_times"

# Solve the LP problem
status = prob.solve()

# Print the results
print("Critical Path time:")
for activity in activities_list:
    if value(start_times[activity]) == 0:
        print(f"{activity} starts at time 0")
    if value(end_times[activity]) == max([value(end_times[activity]) for activity in activities_list]):
        print(f"{activity} ends at {value(end_times[activity])} hours in duration")

# Print solution
print("\nSolution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)


# In[49]:


# Define the data
tasks = [
    {"Task": "A", "Start": 0, "Duration": 8},
    {"Task": "B", "Start": 0, "Duration": 16},
    {"Task": "C", "Start": 8, "Duration": 10},
    {"Task": "D1", "Start": 8, "Duration": 20},
    {"Task": "D2", "Start": 28, "Duration": 20},
    {"Task": "D3", "Start": 28, "Duration": 24},
    {"Task": "D4", "Start": 52, "Duration": 100},
    {"Task": "D5", "Start": 152, "Duration": 20},
    {"Task": "D6", "Start": 152, "Duration": 30},
    {"Task": "D7", "Start": 182, "Duration": 30},
    {"Task": "D8", "Start": 212, "Duration": 16},
    {"Task": "E", "Start": 18, "Duration": 24},
    {"Task": "F", "Start": 228, "Duration": 20},
    {"Task": "G", "Start": 228, "Duration": 20},
    {"Task": "H", "Start": 248, "Duration": 28}
]

fig, ax = plt.subplots()

# Create bars for the Gantt chart
for i, task in enumerate(tasks):
    start = task["Start"]
    duration = task["Duration"]
    ax.broken_barh([(start, duration)], (i - 0.4, 0.8), facecolors='tab:blue')

# Setting labels and grid
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([task["Task"] for task in tasks])
ax.set_xlabel('Hours')
ax.set_ylabel('Tasks')
ax.set_title('Worst Case')
ax.grid(True)

# Format the x-axis
#plt.xticks(np.arange(0, max(task["Start"] + task["Duration"] for task in tasks) + 1, 1))

plt.show()


# In[50]:


# Define the directed graph
G = nx.DiGraph()

# Add nodes and edges based on the task list and their predecessors
tasks = {
    "A": "Describe product",
    "B": "Develop marketing strategy",
    "C": "Design brochure",
    "D1": "Requirements analysis",
    "D2": "Software design",
    "D3": "System design",
    "D4": "Coding",
    "D5": "Write documentation",
    "D6": "Unit testing",
    "D7": "System testing",
    "D8": "Package deliverables",
    "E": "Survey potential market",
    "F": "Develop pricing plan",
    "G": "Develop implementation plan",
    "H": "Write client proposal"
}

predecessors = {
    "A": [],
    "B": [],
    "C": ["A"],
    "D1": ["A"],
    "D2": ["D1"],
    "D3": ["D1"],
    "D4": ["D2", "D3"],
    "D5": ["D4"],
    "D6": ["D4"],
    "D7": ["D6"],
    "D8": ["D5", "D7"],
    "E": ["B", "C"],
    "F": ["D8", "E"],
    "G": ["A", "D8"],
    "H": ["F", "G"]
}

# Add nodes with labels
for task_id, task_name in tasks.items():
    G.add_node(task_id, label=task_name)

# Add edges
for task_id, pred_list in predecessors.items():
    for pred in pred_list:
        G.add_edge(pred, task_id)

# Set figure size for a larger display
plt.figure(figsize=(20, 12))

# Draw the graph
pos = nx.spring_layout(G, seed=10)  # Seed for reproducible layout
labels = nx.get_node_attributes(G, 'label')
nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color='lightblue', font_size=10, arrows=True)

# Show plot
plt.show()


# In[ ]:





# In[ ]:




