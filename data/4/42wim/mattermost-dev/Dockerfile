FROM mysql  
  
RUN apt-get update && apt-get -y install curl netcat  
RUN mkdir -p /mattermost/data  
  
RUN curl https://releases.mattermost.com/4.10.0/mattermost-team-4.10.0-linux-
amd64.tar.gz | tar -xvz  
  
COPY config.template.json /  
COPY docker-entry.sh /  
  
RUN chmod +x /docker-entry.sh  
ENTRYPOINT ["/docker-entry.sh"]  
  
EXPOSE 80  

