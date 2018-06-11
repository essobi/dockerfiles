FROM ubuntu:14.04  
ADD install.sh install.sh  
RUN ./install.sh  
  
RUN useradd -m znc  
USER znc  
WORKDIR /home/znc  
VOLUME /home/znc  
  
EXPOSE 6667  
ENTRYPOINT ["/usr/bin/znc", "--foreground"]  

