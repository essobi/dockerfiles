# aviary-riak  
#  
# VERSION 1.0.7  
FROM java:8  
MAINTAINER Chenhan Shen shen@likemindnetworks.com  
  
# Environmental variables  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Riak and clean  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y sudo logrotate supervisor \  
&& wget
http://s3.amazonaws.com/downloads.basho.com/riak/2.1/2.1.1/ubuntu/trusty/riak_2.1.1-1_amd64.deb
\  
&& dpkg -i riak_2.1.1-1_amd64.deb \  
&& rm riak_2.1.1-1_amd64.deb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Make Riak's data and log directories volumes  
VOLUME ["/var/lib/riak", "/var/log/riak"]  
  
# Open ports for HTTP and Protocol Buffers  
EXPOSE 8098 8087  
# Setup supervisord for riak  
RUN mkdir -p /var/log/supervisor  
COPY ./conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Tune Riak configuration settings for the container  
COPY ./conf/riak.conf /etc/riak/riak.conf  
  
COPY ./bin/riak-setup.sh ./bin/riak-start.sh /etc/riak/  
RUN chmod +x /etc/riak/riak-setup.sh /etc/riak/riak-start.sh  
  
# Start Riak  
CMD ["/etc/riak/riak-setup.sh"]  

