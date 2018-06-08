FROM stackbrew/debian:wheezy  
MAINTAINER Christian Simon <simon@swine.de>  
# Ensure sources.list / upgrade  
ADD ./sources.list /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y upgrade  
# Install default tools  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install vim python-setuptools
nano git curl procps psmisc sudo build-essential git subversion wget  
# Richte Gruppe/User devel ein  
RUN addgroup --gid 1000 devel  
RUN adduser --system --group --uid 1000 --group --shell /bin/bash --home
/devel devel  
# Allow devel to sudo  
ADD ./sudo-devel /etc/sudoers.d/devel  
RUN chown 0:0 /etc/sudoers.d/devel  
RUN chmod 440 /etc/sudoers.d/devel  

