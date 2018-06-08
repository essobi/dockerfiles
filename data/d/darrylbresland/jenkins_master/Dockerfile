FROM jenkins  
MAINTAINER Darryl Bresland <darryl.bresland@seopa.com>  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
USER root  
RUN apt-get update  
RUN apt-get install -y -q build-essential git libssl-dev libreadline-dev
zlib1g-dev vim nano  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
USER jenkins

