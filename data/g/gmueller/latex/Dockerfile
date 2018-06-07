FROM debian:latest  
MAINTAINER Gero Müller "post@geromueller.de"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y texlive-full make biber graphicsmagick ghostscript  
RUN apt-get autoclean  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

