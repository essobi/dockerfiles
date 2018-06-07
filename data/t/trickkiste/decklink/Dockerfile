FROM ubuntu:trusty  
MAINTAINER Markus Kienast <mark@trickkiste.at>  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /tmp  
WORKDIR /tmp  
  
# This container can be used as basis for builds, which require the existance
of Blackmagic Decklink libs  
# The libs are redistributed in this git repo for convenience. If that is
prohibited by Blackmagic terms  
# and conditions, please let me know.  
# Install Blackmagic dependencies  
RUN apt-get update && \  
apt-get install -y libjpeg62 libgl1-mesa-glx libxml2 && \  
apt-get autoclean -y && apt-get autoremove -y && apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  
# Install Blackmagic libs (not drivers)  
COPY desktopvideo-10.9.5a4-x86_64/usr/lib/libDeckLinkAPI.so /usr/lib/  
COPY desktopvideo-10.9.5a4-x86_64/usr/lib/libDeckLinkPreviewAPI.so /usr/lib/  

