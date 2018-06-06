###########################################################  
# Dockerfile to build the Workflow service  
# Based on Alpine (minimal Linux installation)  
############################################################  
  
FROM ubuntu:trusty  
  
MAINTAINER Shaun Adkins <sadkins@som.umaryland.edu>  
  
# Handle warnings from apt/dpkg  
ARG TERM=linux  
ARG DEBIAN_FRONTEND=noninteractive  
  
ARG WORKFLOW_VERSION=3.2.0  
ARG WORKFLOW_DOWNLOAD_URL=http://sourceforge.net/projects/tigr-
workflow/files/tigr-workflow/wf-${WORKFLOW_VERSION}.tar.gz  
  
#--------------------------------------------------------------------------------  
# BASICS  
  
RUN apt-get -q update && apt-get -q install -y \  
curl \  
&& apt-get -q clean autoclean \  
&& apt-get -q autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
#--------------------------------------------------------------------------------  
# WORKFLOW -- install in /opt/workflow  
  
RUN mkdir -p /usr/src/workflow  
WORKDIR /usr/src/workflow  
  
COPY workflow.deploy.answers /tmp/.  
  
RUN curl -SL $WORKFLOW_DOWNLOAD_URL -o workflow.tar.gz \  
&& tar -xvf workflow.tar.gz -C /usr/src/workflow \  
&& rm workflow.tar.gz \  
&& mkdir -p /opt/workflow/server-conf \  
&& ./deploy.sh < /tmp/workflow.deploy.answers \  
&& chown www-data:www-data /opt/workflow/server-conf \  
&& mkdir -m 0777 -p /local/services/workflow/mockserver/working  
COPY htc.conf /opt/workflow/server-conf  
  
CMD ["/bin/bash"]  
  
# Lastly, set working directory to root directory  
WORKDIR /  

