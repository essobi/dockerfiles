FROM centos:centos6  
MAINTAINER Sparkle <popeast@gmail.com>  
  
ENV RIAK_VERSION 1.4.12  
RUN yum install -y sudo  
RUN yum install -y
http://s3.amazonaws.com/downloads.basho.com/riak/1.4/${RIAK_VERSION}/rhel/6/riak-${RIAK_VERSION}-1.el6.x86_64.rpm  
  
RUN sed -i.bak 's/127.0.0.1/0.0.0.0/' /etc/riak/app.config  
RUN echo "Defaults:root !requiretty" > /etc/sudoers.d/riak  
  
VOLUME /var/lib/riak  
EXPOSE 8087 8098  
CMD ulimit -n 4096 && /usr/sbin/riak start && tail -F
/var/log/riak/erlang.log.1  
  

