<div align=center><img align="right" width=100 height=100 src="pictures/discord.ico"></span></div>

# Discord Friends

<br>

## Description

___
Save discord friend information in case, so incase you lose your account you can easily backup what you saved!

## Requirements

___

1. `Python` >=3.5 or `Anaconda` (optional)
2. pip modules (`django`)
3. A discord account (with `developer options` enabled)
4. PostgreSQL installed with database set up already (optional - best peformance)

<br>

## Installation / Usage

___

## Anaconda

1. Clone this repository with command `git clone https://github.com/LokotamaTheMastermind/discord-friends.git`
2. Enter the folder with anaconda enabled and in `base` virtual environment
3. Change the directory to `scripts/{op}`, where `{op}` is your operating system listed. Then after run the `install` script for that operating system
4. Wait for project server to startup
5. Then open browser in url `127.0.0.1:100`

## PIP

1. Clone this repository with command `git clone https://github.com/LokotamaTheMastermind/discord-friends.git`
2. Activate your virtualenv if you have any
3. Change directory to `scripts/{op}` where `{op}` is your operating system. Then run the file `install_pip.bat` in cmd
4. Wait tfor the project server to startup
5. Then open browser in url `127.0.0.1`

<br>

**Important Notice** - I suggest you read further for information about configuring the project

<br>

## Configuration

### Database

___
To configure the database if you wanna use the default replace the following lines in the `settings.py` in the `discord-friends` folder

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'discord-friends',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}
```

to this

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

If you wanna leave the database as it is then replace information provided already with yours

<br>

## Screenshots

___
![Discord Friends - Homepage](pictures/home.jpg)

![Discord Friends - Logout](pictures/logout.jpg)

<br>

## Questions

___

> 1. How do you find the `User ID` of a discord user

>> Answer - Enable the `developer` options of discord account. After that right-click on users account and look for the option `Copy User ID`

<br>

## Future Plans

___

1. Make process automatic with access to discord account to get information. It will work everytime you run the project
2. Make a restore button to recover friend stored incase of account loss
3. Compiled project for those without Python

<br>

## License

___
View the license at [LICENSE](LICENSE)

<br>

## Contributing

___
To contributing to the project read the instructions at [CONTRIBUTING](CONTRIBUTING.md)

<br>

## Authors

___
The current project authors are listed in [AUTHORS](AUTHORS.md)