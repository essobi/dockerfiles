# Jenkins DoxyGen slave image for SCA project.  
# TODO: check https://docs.docker.com/engine/userguide/eng-
image/dockerfile_best-practices  
FROM btowerlabz/docker-sca-ci-slave  
MAINTAINER btower-labz <labz@btower.net>  
  
LABEL Name="docker-sca-ci-slave-doxygen"  
LABEL Vendor="btower-labz"  
LABEL Version="1.0.0"  
LABEL Description="Provides doxygen sca ci agent, either slave or swarm mode"  
  
ARG LABELS=/home/jenkins/swarm-labels.cfg  
  
# Install additional software  
USER root  
  
# Install doxygen environment  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get update && apt-get install -y doxygen graphviz graphviz-doc mscgen
dia dia-shapes dia2code && rm -rf /var/lib/apt/lists/*  
RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections  
  
USER jenkins  
RUN printf " doxygen" >>${LABELS}  
  
RUN uname -a; cat /etc/issue; cat ${LABELS}; doxygen --version;  

