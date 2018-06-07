# vim: ft=dockerfile  
###############################################################################  
# Jenkins with DooD (Docker outside of Docker)  
# http://github.com/axltxl/docker-jenkins-dood  
# Author: Alejandro Ricoveri <me@axltxl.xyz>  
# Based on:  
# * http://container-solutions.com/2015/03/running-docker-in-jenkins-in-docker  
# * http://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci  
###############################################################################  
  
FROM jenkins/jenkins:2.107.3  
MAINTAINER Alejandro Ricoveri <alejandroricoveri@gmail.com>  
  
# Install necessary packages  
USER root  
RUN apt-get update \  
&& apt-get install -y sudo supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
# install useful tools  
RUN apt-get update \  
&& apt-get -y install dos2unix \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install docker-engine  
# According to Petazzoni's article:  
# ---------------------------------  
# "Former versions of this post advised to bind-mount the docker binary from  
# the host to the container. This is not reliable anymore, because the Docker  
# Engine is no longer distributed as (almost) static libraries."  
ARG docker_version=17.06.2~ce  
#RUN curl -sSL https://get.docker.com/ | sh && \  
# apt-get purge -y docker docker-engine docker.io && \  
# apt-get install docker-ce=${docker_version}-0~debian  
RUN (apt-get purge -y docker docker-engine docker.io || true) && \  
apt-get update && \  
apt-get install --no-install-recommends -y apt-transport-https ca-certificates
curl gnupg2 software-properties-common && \  
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | sudo apt-key add - && \  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable" && \  
apt-get update && \  
apt-get install --no-install-recommends -y docker-
ce=${docker_version}-0~debian  
  
# Make sure jenkins user has docker privileges  
RUN usermod -aG docker jenkins  
  
# Install initial plugins  
USER jenkins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  
# supervisord  
USER root  
  
# Create log folder for supervisor and jenkins  
RUN mkdir -p /var/log/supervisor  
RUN mkdir -p /var/log/jenkins  
  
# Copy the supervisor.conf file into Docker  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Start supervisord when running the container  
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf  

