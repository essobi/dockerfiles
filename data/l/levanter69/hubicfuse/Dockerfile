FROM debian:jessie  
MAINTAINER levanter69@gmail.com  
  
# To get rid of error messages like "debconf: unable to initialize frontend:
Dialog":  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# System packages update  
RUN apt-get -q update  
RUN apt-get -qy dist-upgrade  
  
# Dependencies install  
RUN apt-get install -qy git-core gcc make curl libfuse-dev pkg-config
libcurl4-openssl-dev libxml2-dev libssl-dev libjson-c-dev libmagic-dev  
  
RUN git clone -b master --single-branch
https://github.com/TurboGit/hubicfuse.git /hubicfuse  
  
WORKDIR /hubicfuse  
  
RUN ./configure  
RUN make  
RUN make install  
  
ADD start.sh /start.sh  
  
VOLUME ["/config"]  
VOLUME ["/data"]  
  
CMD ["/start.sh"]  

