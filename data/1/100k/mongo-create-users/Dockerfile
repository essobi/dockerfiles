FROM mongo:3.2  
MAINTAINER Nicolas Zozol - nz@robusta.io - http://www.robusta.io - hk project  
# docker pull 100k/mongo-create-users  
# Objectif is to create users at the stratup, then kill the mongo  
# Users will be put into the data-container  
# Data container is a simple ansible task  
# Ansible will be asked to run the create-users script with the correct
passowrds  
# >> sudo docker exec mongo-primary mongo /opt/setup/create-users.js;  
# Warning : js script will use this directory  
RUN mkdir --parents /opt/conf/ \  
&& mkdir --parents /opt/setup/ \  
&& mkdir --parents /data/db/ \  
&& chown -R mongodb:mongodb /data/db  
  
VOLUME /opt/setup /opt/conf  
  
WORKDIR /opt/conf/  
  
# Same as config-file  
COPY create-users.js /opt/setup/

