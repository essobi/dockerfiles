FROM python:3  
  
RUN apt-get update && apt-get install -y default-jre  
RUN pip install dependency-check safety  
RUN dependency-check --updateonly  

