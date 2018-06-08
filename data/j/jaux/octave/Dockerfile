FROM ubuntu  
MAINTAINER Ye Liu (https://github.com/jaux)  
RUN \  
apt-get update -y && apt-get upgrade -y && \  
apt-get install -y software-properties-common less && \  
apt-add-repository ppa:octave/stable && apt-get update -y && \  
apt-get install -y octave  
CMD ["/usr/bin/octave-cli"]  

