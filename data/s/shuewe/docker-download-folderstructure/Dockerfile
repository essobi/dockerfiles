FROM ubuntu:latest  
  
MAINTAINER Stephan Hüwe (shuewe87@gmail.com)  
  
ADD git-folder-scripts git-folder-scripts  
ADD folder-system-definitions folder-system-definitions  
  
#Install python3.6  
RUN apt-get -y update  
RUN apt-get install python3-pip vim git wget -y  
RUN apt-get install software-properties-common swig -y  
RUN apt-get install python3.6 python3.6-dev -y  
RUN ln -s -f /usr/bin/python3.6 /usr/bin/python  
RUN python -m pip install --upgrade pip  
  
RUN ["chmod", "+x", "/git-folder-scripts/start.sh"]  
  
ENTRYPOINT ["/git-folder-scripts/start.sh"]  

