FROM ubuntu:latest  
MAINTAINER Justifiably <justifiably@ymail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install AVConv and mkv Tools  
RUN apt-get update && \  
apt-get install -y libav-tools mkvtoolnix && \  
apt-get clean  
  
# Set up local user to run as  
RUN useradd -u 1001 -ms /bin/bash docker  
USER docker  
ENV HOME /home/docker  
  
CMD ["/usr/bin/avconv"]  

