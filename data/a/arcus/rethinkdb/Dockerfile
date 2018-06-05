FROM ubuntu:14.04  
MAINTAINER Arcus "http://arcus.io"  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y wget && echo "deb
http://download.rethinkdb.com/apt trusty main" >
/etc/apt/sources.list.d/rethinkdb.list \  
&& wget -qO- http://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -  
RUN apt-get update  
RUN apt-get install -y rethinkdb  
EXPOSE 8080  
EXPOSE 28015  
EXPOSE 29015  
WORKDIR /data  
VOLUME /data  
CMD ["--bind", "all"]  
ENTRYPOINT ["/usr/bin/rethinkdb"]  

