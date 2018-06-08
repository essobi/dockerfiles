# Dockerfile for docker image of RunDeck  
# https://github.com/bhalothia/docker-rundeck  
# RunDeck plugins from https://github.com/rundeck-plugins  
FROM debian:stable  
MAINTAINER Rodrigo Souza  
  
ENV RDECK_BASE /var/lib/rundeck  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && \  
apt-get -y install procps sudo ca-certificates openjdk-8-jdk openssh-client
pwgen curl mysql-client git uuid-runtime && \  
apt-get clean  
  
ADD http://dl.bintray.com/rundeck/rundeck-deb/rundeck-2.7.3-1-GA.deb
/tmp/rundeck.deb  
  
ADD prerequisites/ /  
  
RUN dpkg -i /tmp/rundeck.deb &&\  
rm /tmp/rundeck.deb &&\  
chown rundeck:rundeck /tmp/rundeck &&\  
chmod u+x /opt/entrypoint.sh &&\  
mkdir -p $RDECK_BASE/.ssh &&\  
chown rundeck:rundeck $RDECK_BASE/.ssh  
  
# Start rundeck  
ENTRYPOINT ["/opt/entrypoint.sh"]  

