FROM ubuntu:14.04  
  
ENV FLOCKER_VERSION 1.12.0  
  
RUN apt-get update &&\  
apt-get -y install \  
apt-transport-https \  
software-properties-common  
  
RUN add-apt-repository -y "deb https://clusterhq-
archive.s3.amazonaws.com/ubuntu/14.04/\$(ARCH) /"  
RUN apt-get update &&\  
apt-get -y --force-yes install \  
clusterhq-flocker-node=${FLOCKER_VERSION}*  
  
CMD ["flocker-control", "--help"]  

