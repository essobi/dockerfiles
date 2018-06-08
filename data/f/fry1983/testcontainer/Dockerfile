FROM ubuntu:16.04  
MAINTAINER John-Zoidberg  
RUN apt-get update  
RUN apt-get install -y wget git psmisc python python-pip  
RUN wget https://bitbucket.org/fry1983/tomcat/downloads/release.deb  
RUN dpkg -i release.deb  
RUN pip install requests  
RUN git clone https://fry1983@bitbucket.org/fry1983/testcontainer.git  
RUN cd testcontainer && python main.py  
RUN python main.py  
  

