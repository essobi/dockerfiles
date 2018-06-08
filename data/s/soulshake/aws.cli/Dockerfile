FROM debian:jessie  
MAINTAINER AJ Bowen <aj@soulshake.net>  
  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
groff \  
less \  
python \  
python-pip \  
python-docutils \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install awscli  
  
CMD ["help"]  
ENTRYPOINT [ "aws" ]  

