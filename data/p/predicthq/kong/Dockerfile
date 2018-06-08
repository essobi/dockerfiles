FROM kong:0.10.3  
MAINTAINER Braedon Vickers, braedon@predicthq.com  
  
COPY kong.conf.default /etc/kong/kong.conf.default  
COPY kong /kong/kong  
COPY kong-0.10.3-0.rockspec /kong/kong-0.10.3-0.rockspec  
COPY Makefile /kong/Makefile  
  
WORKDIR /kong  
RUN yum install -y -q unzip && \  
make install  
  
# From https://github.com/Mashape/docker-kong/pull/84  
# ensure Kong logs go to the log pipe from our entrypoint and so to docker
logging  
RUN mkdir -p /usr/local/kong/logs \  
&& ln -sf /tmp/logpipe /usr/local/kong/logs/access.log \  
&& ln -sf /tmp/logpipe /usr/local/kong/logs/admin_access.log \  
&& ln -sf /tmp/logpipe /usr/local/kong/logs/serf.log \  
&& ln -sf /tmp/logpipe /usr/local/kong/logs/error.log  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  

