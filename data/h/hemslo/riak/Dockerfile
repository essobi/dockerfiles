FROM ubuntu:12.04  
MAINTAINER Hemslo Wang <hemslo.wang@gmail.com>  
  
RUN apt-get update && apt-get install -y curl supervisor  
RUN curl http://apt.basho.com/gpg/basho.apt.key | apt-key add -  
RUN echo "deb http://apt.basho.com precise main" >
/etc/apt/sources.list.d/basho.list  
RUN apt-get update && apt-get install -y riak  
  
COPY app.config /etc/riak/app.config  
RUN echo "ulimit -n 4096" >> /etc/default/riak  
  
# Supervisor  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
VOLUME ["/var/lib/riak", "/var/log/riak", "/var/log/supervisor"]  
  
EXPOSE 8087 8098  
CMD ["/usr/bin/supervisord"]  

