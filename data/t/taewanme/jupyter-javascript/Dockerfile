FROM jupyter/base-notebook:latest  
MAINTAINER Taewan Kim <taewanme@gmail.com>  
  
USER root  
  
RUN apt-get update  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs libzmq3-dev build-essential && npm install -g
ijavascript  
RUN ijs --ijs-install-kernel  
  
COPY startJupyter.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/startJupyter.sh  
RUN chown -R $NB_USER:users /usr/local/bin/startJupyter.sh  
  
VOLUME ["/home/jovyan/work/data"]  
WORKDIR /home/jovyan/work  
  
EXPOSE 8888  
USER jovyan  
  

