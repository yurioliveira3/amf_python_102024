#source gym_env/bin/activate

import time
import gymnasium as gym
from stable_baselines3 import PPO

# Crie o ambiente
env = gym.make("BipedalWalker-v3", render_mode="human")

# Carregar o modelo
model = PPO("MlpPolicy", env, verbose=1)

# Treinar o modelo
model.learn(total_timesteps=50000)

#Numero de vezes que a task vai ser executada
episodes = 5

# Avaliar e renderizar o robô andando
for episode in range(episodes):
    obs = env.reset()
    done = False
    total_reward = 0
    
    while not done:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
        
        # Renderiza a simulação em tela
        env.render()  
        
        total_reward += reward
    
    print(f"Episode {episode+1} reward: {total_reward}")

# Fecha o ambiente
env.close()
