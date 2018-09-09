# rocket-league-client
A client repository for a Rocket League trading website posting bot.

After cloning and unzipping the repository, create a new file called
**settings.txt** in the rocket-league-client directory. This file contains
the settings for the Rocket League bot.

The first line of the **settings.txt** file is an integer representing the
delay in minutes between posting accounts. Every line after the first line
is an account in the form of `username:password`. An exclamation point at
the start of the line will temporarily remove the account from the Rocket
League bot. An example is shown below:

### settings.txt
```
15
username:password
!disabled_username:disabled_password
another_username:another_password
```

### Output
```
Delay: 15 minutes
Accounts: 2
Usernames: username, another_username
Passwords: password, another_password
```
