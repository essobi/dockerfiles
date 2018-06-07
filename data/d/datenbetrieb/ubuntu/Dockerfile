# DOCKER-VERSION 1.0.0  
FROM ubuntu:trusty  
MAINTAINER Peter Niederlag "peter.niederlag@datenbetrieb.de"  
# injecting some packages into the base ubuntu image  
# - ca-certificats [~2 MB]  
# openssl and certificats to support secure https connections  
# - vim [~30 MB]  
# one of the things that have rocked linux since the beginning  
# - curl [~20 MB]  
# very useful during deployment operations  
# - openssh-client [~17 MB]  
# so we are able to connect to the outside world from inside the container  
# - nettools [~1MB]  
# helps in diagnosing network related stuff and has very small footprint  
# - git [~50 MB]  
# essential on management of anything, footprint is quite high though  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get -y update && \  
apt-get -y --no-install-recommends install ca-certificates && \  
apt-get -y --no-install-recommends install vim && \  
apt-get -y --no-install-recommends install curl && \  
apt-get -y --no-install-recommends install openssh-client && \  
apt-get -y --no-install-recommends install net-tools && \  
apt-get -y --no-install-recommends install locales && \  
apt-get -y --no-install-recommends install git && \  
apt-get clean && \  
localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
&& \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
ENV LANG en_US.utf8  
  
# set /bin/bash as default command  
CMD ["/bin/bash"]  

