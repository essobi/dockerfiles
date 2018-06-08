FROM ubuntu:16.04  
MAINTAINER Giovanni Toffetti  
  
# install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update --no-install-recommends  
RUN apt-get -yq install --no-install-recommends curl wget apt-transport-https  
RUN wget --no-check-certificate -O -
https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub
| apt-key add - && \  
echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial main"
> /etc/apt/sources.list.d/saltstack.list  
RUN apt-get -yq install --no-install-recommends salt-master salt-minion salt-
ssh salt-syndic salt-cloud salt-api  
  
# Expose ports  
EXPOSE 4505 4506  
# Run master  
CMD /usr/bin/salt-master --log-level=debug  

