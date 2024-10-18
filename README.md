# Betting

## Ian is a Woj Master

### Keklan is a Woj Recruit

**NERD YOU HAVE TO TELL PEOPLE WHAT LIBRARIES TO INSTALL REEEEEEEEEEEEEEEEEEEEEEEEEEEEE**

I have done so for you. There is a three step process:

`python -m venv venv`

This will make a virtual environment (named venv b/c I'm very original) in this dir.
In short, it allows you to install libs in that folder, which is helpful b/c some libs need
different versions of other libs. This way you don't have to manage it all globally.

`source venv/bin/activate`

This activates the virtual environment. Now python, pip, etc will use libs from the venv.
You can end this by typing `deactivate`.

`pip install -r requirements.txt`

Finally, this will install all the libs in the requirements file. This way anyone who tries to run this
will be using the same libs and versions as you.

#### Making your own requirements file

IDK how to do it on windows (more like wangblows lmao) but typing: `pip freeze > requirements.txt` will
make a file with all the packages and versions inside. You can just type `pip freeze` and copy it for now.
