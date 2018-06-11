FROM ubuntu:12.04  
MAINTAINER Tyler Hall <tylerwhall@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y openjdk-6-jre-headless git-core vim-tiny curl  
RUN apt-get install -y gitweb  
  
ENV GERRIT_HOME /home/gerrit  
  
RUN useradd -m gerrit  
USER gerrit  
RUN curl http://gerrit-releases.storage.googleapis.com/gerrit-2.8.3.war -o
$GERRIT_HOME/gerrit.war  
ADD start-gerrit.sh $GERRIT_HOME/start-gerrit.sh  
VOLUME ["/home/gerrit"]  
  
EXPOSE 8080 29418  
CMD ["/home/gerrit/start-gerrit.sh"]  

