FROM brightcommerce/ubuntu:14.04.20140911  
MAINTAINER Brightcommerce <support@brightcommerce.com>  
  
ENV HOME /root  
  
RUN add-apt-repository -y ppa:chris-lea/redis-server \  
&& apt-get update \  
&& apt-get install -y redis-server  
  
RUN sed 's/^daemonize yes/daemonize no/' -i /etc/redis/redis.conf \  
&& sed 's/^bind 127.0.0.1/bind 0.0.0.0/' -i /etc/redis/redis.conf \  
&& sed 's/^# unixsocket /unixsocket /' -i /etc/redis/redis.conf \  
&& sed 's/^# unixsocketperm 755/unixsocketperm 777/' -i /etc/redis/redis.conf
\  
&& sed '/^logfile/d' -i /etc/redis/redis.conf  
  
ADD start /start  
RUN chmod 755 /start  
  
EXPOSE 6379  
VOLUME ["/var/lib/redis"]  
VOLUME ["/var/run/redis"]  
  
CMD ["/start"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

