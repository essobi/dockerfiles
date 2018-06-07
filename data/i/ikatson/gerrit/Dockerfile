FROM ubuntu:trusty  
  
MAINTAINER Igor Katson <igor.katson@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV GERRIT_HOME /home/gerrit  
ENV GERRIT_CONFIG_PATH /home/gerrit/gerrit/etc/gerrit.config  
ENV GERRIT_USER gerrit  
ENV GERRIT_WAR /home/gerrit/gerrit.war  
  
RUN apt-get update  
RUN apt-get upgrade  
  
RUN useradd -m ${GERRIT_USER}  
RUN apt-get install -y openjdk-7-jre-headless git-core  
  
RUN apt-get install wget  
  
RUN wget http://gerrit-releases.storage.googleapis.com/gerrit-2.9.1.war -O
/tmp/gerrit.war  
  
RUN apt-get install libpostgresql-jdbc-java  
  
RUN mkdir -p $GERRIT_HOME/gerrit  
RUN mv /tmp/gerrit.war $GERRIT_WAR  
RUN chown -R ${GERRIT_USER}:${GERRIT_USER} $GERRIT_HOME  
  
USER gerrit  
RUN java -jar $GERRIT_WAR init --batch -d $GERRIT_HOME/gerrit  
  
USER root  
  
ADD gerrit.config ${GERRIT_CONFIG_PATH}  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 8080 29418  
CMD /start.sh  

