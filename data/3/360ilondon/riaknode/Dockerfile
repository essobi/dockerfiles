# To Run: docker -H :4000 run -e affinity:container=="worker$1" -p 8098:8098
-p 8087:8087 -p 8099:8099 -p 8000:8000 --net="riak-net" --name "riak$1"
360ilondon/riaknode &  
FROM ubuntu:trusty  
MAINTAINER Niki Wiles  
RUN apt-get update  
RUN apt-get install -q -y curl && curl -fsSL
https://packagecloud.io/install/repositories/basho/riak/script.deb | sudo bash  
RUN apt-get update && apt-get install -y supervisor riak=2.0.5-1  
RUN mkdir -p /var/log/supervisor  
RUN locale-gen en_US en_US.UTF-8  
# Getting hub.docker to get this file is tricky, github doesn't really work
well becase the repo is private, to pastebin is a quick and dirty solution.  
ADD http://pastebin.com/raw/HrUB9ETc /etc/supervisor/conf.d/supervisord.conf  
RUN sed -i "s|listener.http.internal = 127.0.0.1:8098|listener.http.internal =
0.0.0.0:8098|" /etc/riak/riak.conf  
RUN sed -i "s|listener.protobuf.internal =
127.0.0.1:8087|listener.protobuf.internal = 0.0.0.0:8087|" /etc/riak/riak.conf  
RUN sed -i "s|storage_backend = bitcask|storage_backend = leveldb|"
/etc/riak/riak.conf  
  
# Install nano  
RUN apt-get install -y nano  
RUN export TERM=xterm  
  
# Local storage  
VOLUME /var/lib/riak  
VOLUME /var/log/riak  
  
# Expose sshd server port  
EXPOSE 22  
# Expose Riak HTTP port  
EXPOSE 8098  
# Expose Riak protocol buffer port  
EXPOSE 8087  
# Expose Riak epmd listener  
EXPOSE 4369  
# Expose Riak handoff port  
EXPOSE 8099  
# Expose Edmp  
EXPOSE 8000  
# Run  
CMD ["/usr/bin/supervisord"]

