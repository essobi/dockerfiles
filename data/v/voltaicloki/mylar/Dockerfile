FROM ubuntu:trusty  
MAINTAINER Michael Mansell <michael.mansell@gmail.com>  
  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
  
RUN sed -i 's/restricted$/restricted multiverse/' /etc/apt/sources.list && \  
apt-get update -q && \  
apt-get install -qy git-core python2.7 unrar  
  
RUN git clone https://github.com/evilhero/mylar.git /mylar  
  
ADD start.sh /start.sh  
  
VOLUME ["/config"]  
VOLUME ["/downloads"]  
VOLUME ["/library"]  
EXPOSE 8090  
CMD ["/bin/bash","/start.sh"]  

