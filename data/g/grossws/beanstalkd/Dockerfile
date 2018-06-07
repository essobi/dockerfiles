FROM debian:wheezy  
MAINTAINER Konstantin Gribov <grossws@gmail.com>  
  
ENV GOSU_URL https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64  
EXPOSE 11300  
RUN apt-get update \  
&& apt-get install -y curl beanstalkd \  
&& gpg --keyserver pgp.mit.edu --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -sSL $GOSU_URL -o /bin/gosu \  
&& chmod +x /bin/gosu \  
&& curl -sSL $GOSU_URL.asc -o /tmp/gosu.asc \  
&& gpg --verify /tmp/gosu.asc /bin/gosu \  
&& rm /tmp/gosu.asc \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD entrypoint.sh /  
VOLUME ["/data"]  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["beanstalkd"]  
  

