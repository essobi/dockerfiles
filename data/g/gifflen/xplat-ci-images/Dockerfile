FROM circleci/python:3.6.1  
ADD Pipfile .  
ADD Pipfile.lock .  
RUN sudo pip install -U pipenv==10.1.2  
RUN sudo pipenv install --python 3.6.1 --system --ignore-pipfile  
RUN sudo pipenv install --python 3.6.1 --system --dev --ignore-pipfile  

