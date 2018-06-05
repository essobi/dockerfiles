# Basics  
#  
FROM ubuntu:14.04  
MAINTAINER wenzizone <wenzizone@126.com>  
# add 163 mirror sources list  
#ADD sources.list /etc/apt/sources.list  
RUN set -x; \  
apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -q -y git-core curl sudo
xmlstarlet software-properties-common python-software-properties \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Java 8  
# auto validate license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
# update repos  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get update  
# install java  
RUN apt-get install oracle-java8-installer -y  
RUN apt-get clean  
  
# Setup volume handling  
RUN /usr/sbin/groupadd atlassian  
ADD own-volume.sh /usr/local/bin/own-volume  
RUN echo "%atlassian ALL=NOPASSWD: /usr/local/bin/own-volume" >> /etc/sudoers  
RUN mkdir -p /opt/atlassian-home  
  
# Add common script functions  
ADD common.bash /usr/local/share/atlassian/common.bash  
RUN chgrp atlassian /usr/local/share/atlassian/common.bash  
RUN chmod g+w /usr/local/share/atlassian/common.bash  

