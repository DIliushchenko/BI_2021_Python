This is my awersome research on virtual environments. The article is available at doi:10.1111/1000-7 
You can easily reproduce my results by running scripts locally.
Please cite me!

Comments from tester

OS: Ubuntu 20.04
Python version: 3.9.7


At the beginning, I recommend install conda and then create conda enviroment:

https://www.anaconda.com/download/ - download conda

install conda:

bash Anaconda-latest-Linux-x86_64.sh


Then create enviroment:

conda create -n virt_env python=3.9

We use python version 3.9 because our script needs special syntax (dct1 | dct2) that help us union dictionaries (|) like sets


Description of problem in StakOverFlow
https://stackoverflow.com/questions/13361510/typeerror-unsupported-operand-types-for-dict-items-and-dict-items/13361547 


Now you can activate enviroment:

conda activate virt_env


Let's downoload some libraries using pip command:

pip install google

pip install --upgrade google-api-python-client

pip install kivy

pip install biopython

pip install aiohttp

pip install pandas

pip install scipy

pip install scunpy

pip install opencv-python

pip install lxml

OR! You can use this command to make it in one row!

pip install -r requirements.txt

And all packages will be installed

That's it! Now you can bravely run the script in this repo!
