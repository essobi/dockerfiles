FROM debian:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
RUN apt-get update  
RUN apt-get -y install curl apt apt-transport-https  
  
RUN echo 'deb https://download.jitsi.org stable/' >>
/etc/apt/sources.list.d/jitsi-stable.list  
RUN curl https://download.jitsi.org/jitsi-key.gpg.key | apt-key add -  
RUN apt-get update  
RUN apt-get install -y jitsi-meet  
RUN apt-get clean  
  
COPY entrypoint.sh /  
CMD /entrypoint.sh  
  

