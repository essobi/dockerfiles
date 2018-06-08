FROM ubuntu:15.04  
MAINTAINER Octoblu <docker@octoblu.com>  
  
RUN apt-get update && \  
apt-get install -y curl awscli && \  
rm -rf /var/lib/apt/lists/*  
RUN curl --silent -L
https://github.com/coreos/fleet/releases/download/v0.10.0/fleet-v0.10.0-linux-
amd64.tar.gz | tar -xz -C /opt/  
RUN apt-get remove -y curl && apt-get -y autoremove  
  
ENV PATH $PATH:/opt/fleet-v0.10.0-linux-amd64  
  
COPY run.sh run.sh  
  
CMD ["./run.sh"]  

