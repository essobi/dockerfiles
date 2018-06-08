FROM debian:wheezy  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
RUN (apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -y git live-build vim &&\  
mkdir /opt/live)  
  
ADD bashrc /root/.bashrc  
  
WORKDIR /opt/live  
  
CMD ["/bin/bash"]  

