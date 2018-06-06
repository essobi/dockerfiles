FROM ubuntu:trusty  
MAINTAINER Ugly-Wan  
  
# Language set  
  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
RUN update-locale LANG=$LANG  
RUN update-locale LANGUAGE=$LANG  
#Run commands  
RUN apt-get -qy update  
RUN apt-get -qy upgrade  
RUN apt-get -qy install expect  
ADD expect.sh /expect.sh  
CMD ["/expect.sh"]  
RUN rm /expect.sh  
RUN apt-get -qy remove expect  

