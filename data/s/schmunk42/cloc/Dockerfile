FROM debian:jessie  
MAINTAINER Marcio Ribeiro <binary@b1n.org>  
  
RUN apt-get update && apt-get install -y \  
cloc \  
\--no-install-recommends  
  
WORKDIR /data  
VOLUME "/data"  
  
ENTRYPOINT ["/usr/bin/cloc"]  

