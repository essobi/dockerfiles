FROM python:3  
RUN mkdir /github-to-gitlab-hook  
WORKDIR /github-to-gitlab-hook  
  
RUN apt-get update && apt-get install git  
  
ADD requirements.txt .  
RUN pip install -r requirements.txt  
  
ADD . .  
RUN python setup.py install  
  
CMD "/bin/bash"  

