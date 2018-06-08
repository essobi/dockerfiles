FROM debian:stable  
EXPOSE 80  
RUN apt-get update && apt-get install -y curl netcat && rm -rf
/var/lib/apt/lists/*  
  
RUN mkdir -p /mattermost/data  
  
COPY config.template.json /  
COPY docker-entry.sh /  
  
RUN chmod +x /docker-entry.sh  
CMD ["/docker-entry.sh"]  
  
RUN curl https://releases.mattermost.com/4.8.0/mattermost-team-4.8.0-linux-
amd64.tar.gz | tar -xz  
RUN rm /mattermost/config/config.json  

