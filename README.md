# Swase
Welcome to Swase!\
The better if statement; a switch case statement emulator!\
\
You can use it like this:
```py
from Swase import Switch

while True:
    cmd = input('> ')
    nest = Switch()
    nest.AddToSwitch(Input='Mercury', Outcome='print("You typed in Mercury!")')
    nest.LastSwitch(Input='Venus', Outcome='print("You typed in Venus!")', Else='print("Not available.")', Bind=cmd)
```
This code is the same as:
```py
while True:
    cmd = input('> ')
    if cmd == 'Mercury':
        print("You typed in Mercury!")
    elif cmd == 'Venus':
        print("You typed in Venus!")
    else:
        print("Not available.")
```
You don't have to define an `Else=''` statement if you don't need a default value.\
\
Every time you want to add a new statement, you have to use `AddToSwitch()`.\
## No matter how many statements you have, `LastSwitch()` always has to be at the end!
You can define the default statement with `LastSwitch(Else='...')`, and bind every statement you previously defined to your variable with `LastSwitch(Bind='...')`.
