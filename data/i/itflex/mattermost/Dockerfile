FROM centos:7  
WORKDIR /mattermost  
VOLUME ["/mattermost/data", "/mattermost/config"]  
EXPOSE 80  
ENV MATTERMOST_VERSION 4.2.0  
ADD https://releases.mattermost.com/${MATTERMOST_VERSION}/mattermost-
team-${MATTERMOST_VERSION}-linux-amd64.tar.gz /  
RUN tar -C / -xzf /mattermost-team-${MATTERMOST_VERSION}-linux-amd64.tar.gz
--no-same-owner && \  
rm -f /mattermost-team-${MATTERMOST_VERSION}-linux-amd64.tar.gz  
  
COPY config.json /mattermost/config/  
  
CMD ["/mattermost/bin/platform", "-config=/mattermost/config/config.json"]  

