import numpy as np
import random

# Definisi ukuran gudang dan posisi awal
warehouse_size = (5, 5)
start_position = (0, 0)
orders = [(4, 4), (2, 3), (1, 1)]  # Posisi item yang harus diambil

# Parameter Q-learning
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration factor

# Inisialisasi Q-table
actions = ['up', 'down', 'left', 'right']
q_table = np.zeros((warehouse_size[0], warehouse_size[1], len(actions)))

# Fungsi untuk menentukan tindakan dari kebijakan ε-greedy
def epsilon_greedy(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(actions)
    else:
        state_q_values = q_table[state[0], state[1]]
        max_action_index = np.argmax(state_q_values)
        return actions[max_action_index]

# Fungsi untuk memperbarui posisi berdasarkan tindakan
def take_action(state, action):
    if action == 'up' and state[0] > 0:
        return (state[0] - 1, state[1])
    elif action == 'down' and state[0] < warehouse_size[0] - 1:
        return (state[0] + 1, state[1])
    elif action == 'left' and state[1] > 0:
        return (state[0], state[1] - 1)
    elif action == 'right' and state[1] < warehouse_size[1] - 1:
        return (state[0], state[1] + 1)
    else:
        return state  # Jika tindakan keluar dari grid, tetap di posisi

# Fungsi untuk mendapatkan ganjaran
def get_reward(state, orders):
    if state in orders:
        return 10  # Ganjaran positif jika mengambil item
    else:
        return -1  # Ganjaran negatif jika bergerak tanpa mengambil item

# Episode Q-learning
num_episodes = 1000
for episode in range(num_episodes):
    state = start_position
    total_reward = 0
    while True:
        action = epsilon_greedy(state)
        next_state = take_action(state, action)
        reward = get_reward(next_state, orders)
        
        # Pembaruan Q-table
        action_index = actions.index(action)
        old_value = q_table[state[0], state[1], action_index]
        next_max = np.max(q_table[next_state[0], next_state[1]])
        q_table[state[0], state[1], action_index] = old_value + alpha * (reward + gamma * next_max - old_value)
        
        state = next_state
        total_reward += reward
        
        if state in orders:
            orders.remove(state)
            if not orders:
                break  # Selesai jika semua item telah diambil

print(q_table)
