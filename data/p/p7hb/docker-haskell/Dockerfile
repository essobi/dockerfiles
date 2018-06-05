FROM ubuntu:xenial  
  
MAINTAINER Prashanth Babu <Prashanth.Babu@gmail.com>  
  
RUN apt-get update -yqq && \  
apt-get install -yqq software-properties-common tmux screen vim && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
575159689BEFB442 && \  
echo 'deb http://download.fpcomplete.com/ubuntu xenial main'| tee
/etc/apt/sources.list.d/fpco.list && \  
apt-get update -yqq && \  
apt-get install -yqq stack && \  
stack upgrade && \  
stack setup && \  
# eval "$(stack --bash-completion-script stack)" && \  
apt-get autoclean && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# We will be running as `root` user.  
USER root  
  
# Working directory is set to the home folder of `root` user.  
WORKDIR /root  
  
CMD ["/bin/bash"]  

