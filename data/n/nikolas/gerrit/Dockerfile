# gerrit  
#  
# VERSION 0.0.9  
FROM ubuntu:16.04  
MAINTAINER <niknyby@riseup.net>  
  
ENV GERRIT_HOME /home/gerrit  
ENV GERRIT_ROOT /home/gerrit/gerrit  
ENV GERRIT_USER gerrit  
ENV GERRIT_WAR /home/gerrit/gerrit.war  
ENV GERRIT_VERSION 2.12.2  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y sudo vim-tiny git && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y supervisor && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jre-headless  
  
RUN useradd -m $GERRIT_USER  
RUN mkdir -p $GERRIT_HOME  
RUN chown ${GERRIT_USER}:${GERRIT_USER} $GERRIT_HOME  
  
RUN mkdir -p /var/log/supervisor  
  
ADD https://gerrit-
releases.storage.googleapis.com/gerrit-${GERRIT_VERSION}.war $GERRIT_WAR  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN chown -R ${GERRIT_USER}:${GERRIT_USER} $GERRIT_HOME  
  
USER gerrit  
CMD ["/usr/bin/ls","/home/gerrit"]  
RUN java -jar $GERRIT_WAR init --batch -d $GERRIT_ROOT  
RUN chown -R ${GERRIT_USER}:${GERRIT_USER} $GERRIT_ROOT  
  
ADD gerrit.config /home/gerrit/gerrit/etc/gerrit.config  
  
USER root  
EXPOSE 8080 29418  
CMD ["/usr/sbin/service","supervisor","start"]  

