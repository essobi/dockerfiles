FROM ubuntu:bionic  
  
MAINTAINER Phocean <jc@phocean.net>  
  
RUN apt-get update &&\  
apt-get install -yq python-dev build-essential python-pip &&\  
pip install sslyze &&\  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/local/bin/sslyze"]  
CMD ["-h"]  

