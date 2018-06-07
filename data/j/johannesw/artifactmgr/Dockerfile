FROM ubuntu:14.04  
MAINTAINER Johannes Wettinger, http://github.com/jojow  
  
  
ENV HOME /root  
ENV ARTIFACT_MANAGER_DIR ${HOME}/artifactmgr  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD install.sh /install.sh  
  
WORKDIR ${HOME}  
  
RUN bash /install.sh && rm /install.sh  
  
EXPOSE 8888  
CMD ${ARTIFACT_MANAGER_DIR}/run.sh  

