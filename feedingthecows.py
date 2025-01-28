# Simulate the process of toggling lights for 100 seconds
lights = [True] * 100  # All lights are initially "on"

# Simulate toggling for each second t from 1 to 100
for t in range(1, 101):
    for i in range(t, 100, t):  # Toggle every t-th light
        lights[i] = not lights[i]
        print(lights)  # Change the state of the light

# Count how many lights remain "on" (True)
on_lights = sum(lights)
print(on_lights)