FROM ubuntu:14.04  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install curl netcat  
  
RUN apt-get -y install python python-pip python-dev build-essential  
RUN apt-get -y install git  
  
RUN git clone https://github.com/numberly/mattermost-integration-giphy.git  
  
RUN cd /mattermost-integration-giphy && python setup.py install  
  
VOLUME ["/config", "/mattermost/data"]  
  
RUN mkdir -p /mattermost/data  
  
RUN curl https://releases.mattermost.com/3.5.1/mattermost-team-3.5.1-linux-
amd64.tar.gz | tar -xvz  
  
RUN rm /mattermost/config/config.json  
RUN ln -s /config/config.json /mattermost/config/config.json  
  
COPY docker-entry.sh /  
RUN chmod +x /docker-entry.sh  
ENTRYPOINT ["/docker-entry.sh"]  
  
EXPOSE 80  

