FROM debian:stable  
LABEL maintainer Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q -y update && apt-get -q -y -o Dpkg::Options::=--force-confdef
-o Dpkg::Options::=--force-confold --purge install rsync && apt-get -q -y
clean  
  
VOLUME ["/backup", "/mnt"]  
  
ENTRYPOINT ["/usr/bin/rsync", "-aHv", "--delete"]  

