# Copyright (c) 2016 Mattermost, Inc. All Rights Reserved.  
# See License.txt for license information.  
FROM mysql:5.7  
# Install ca-certificates to support TLS of Mattermost v3.5  
RUN apt-get update && apt-get install -y ca-certificates curl netcat  
  
#  
# Configure SQL  
#  
ENV MYSQL_ROOT_PASSWORD=mostest  
ENV MYSQL_USER=mmuser  
ENV MYSQL_PASSWORD=mostest  
ENV MYSQL_DATABASE=mattermost_test  
ENV MM_VERSION=4.0.4  
#  
# Configure Mattermost  
#  
WORKDIR /mm  
  
# Copy over files  
RUN curl https://releases.mattermost.com/$MM_VERSION/mattermost-
team-$MM_VERSION-linux-amd64.tar.gz | tar -xvz  
RUN rm -rf ./mattermost/config  
RUN mkdir ./mattermost/config  
  
COPY config_docker.json .  
COPY docker-entry.sh .  
  
RUN chmod +x ./docker-entry.sh  
ENTRYPOINT ./docker-entry.sh  
  
VOLUME /mm/mattermost/mattermost-data  
  
# Ports  
EXPOSE 8065  

