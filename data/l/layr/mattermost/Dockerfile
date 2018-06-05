FROM phusion/baseimage  
MAINTAINER Laur  
# https://github.com/mattermost/mattermost-docker/  
# https://docs.mattermost.com/install/prod-debian.html  
# https://docs.mattermost.com/install/install-ubuntu-1604.html  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update  
RUN apt-get install --no-install-recommends -y \  
curl \  
netcat \  
unattended-upgrades  
RUN update-locale LANG=C.UTF-8  
  
RUN curl https://releases.mattermost.com/3.6.2/mattermost-team-3.6.2-linux-
amd64.tar.gz | tar -xvz  
RUN mv /mattermost /opt/  
RUN rm /opt/mattermost/config/config.json  
RUN ln -s /mattermost/config/config.json /opt/mattermost/config/config.json  
  
COPY config.template.json /  
  
# Baseimage init process  
ENTRYPOINT ["/sbin/my_init"]  
  
# Mattermost daemon  
RUN mkdir /etc/service/mattermost  
ADD mattermost.sh /etc/service/mattermost/run  
  
ADD setup-mattermost.sh /usr/local/sbin/setup-mattermost  
ADD apt-auto-upgrades /etc/apt/apt.conf.d/20auto-upgrades  
  
# Clean up for smaller image  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR "/mattermost"  

