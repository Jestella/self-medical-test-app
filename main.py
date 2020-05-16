print("Hi Welcome to Self Medical Check! Please Enter your name and age")
input(name, age)

print("Thanks " + name\n + "What is your temperature today?")
input(temperature)

def my_tem(temperature):
  if temperature > 38:
    return "You must make an appointment with us"
  elif temperature <= 37 or temperature >= 36:
    return "You are fine!"
  else temperature < 36:
    return "Are you sure?"
  
  

