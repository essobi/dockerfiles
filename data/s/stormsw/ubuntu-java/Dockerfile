#!/usr/bin/docker  
# based on Ubuntu  
FROM ubuntu  
MAINTAINER Alexander Varchenko <alexander.varchenko@gmail.com>  
#this helps with java timezone issues  
RUN echo Europe/Kiev > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
ENV DEBIAN_FRONTEND noninteractive  
# Part1: Oracle:Java9  
# install software-properties-common (ubuntu >= 12.10)  
# to be able to use add-apt-repository  
RUN apt-get update && apt-get install -y --no-install-recommends software-
properties-common  
# add repository for web-update  
RUN add-apt-repository ppa:webupd8team/java  
# Oracle jdk8 (possible to use 6,7,8: 9* is alpha planned for 2016!)  
# accept Oracle license  
RUN echo /usr/bin/debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
RUN echo /usr/bin/debconf shared/accepted-oracle-license-v1-1 seen true |
/usr/bin/debconf-set-selections  
RUN apt-get update && apt-get install -y --no-install-recommends \  
oracle-java9-installer \  
xmlstarlet \  
libsaxon-java \  
augeas-tools \  
curl \  
unzip && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ENV DEBIAN_FRONTEND newt  
CMD /bin/bash  

