# Riak CS HAProxy  
#  
# VERSION 0.1.0  
FROM phusion/baseimage:0.9.11  
MAINTAINER Hector Castro hector@basho.com  
  
# Environmental variables  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update -qq && apt-get install -y \  
software-properties-common \  
python-software-properties  
  
# Install HAProxy  
RUN apt-add-repository ppa:vbernat/haproxy-1.5 -y && apt-get update && \  
apt-get install haproxy -y  
  
# Add the base HAProxy configuration file  
ADD etc/haproxy.cfg /etc/haproxy/haproxy.cfg  
  
# Setup the HAProxy service  
RUN mkdir -p /etc/service/haproxy  
ADD bin/haproxy.sh /etc/service/haproxy/run  
  
# Open the Riak CS and HAProxy statistics ports  
EXPOSE 8080 8888  
# Enable insecure SSH key  
# See: https://github.com/phusion/baseimage-
docker#using_the_insecure_key_for_one_container_only  
RUN /usr/sbin/enable_insecure_key  
  
# Cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Leverage the baseimage-docker init system  
CMD ["/sbin/my_init", "--quiet"]  

