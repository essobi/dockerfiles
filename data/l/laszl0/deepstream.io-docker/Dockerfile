# Pull base image.  
FROM centos:7  
MAINTAINER laszl0  
  
RUN yum install -y wget  
  
RUN wget https://bintray.com/deepstreamio/rpm/rpm -O /etc/yum.repos.d/bintray-
deepstreamio-rpm.repo  
  
RUN yum install -y deepstream.io-2.3.2-1  
  
# Installing Plugins  
RUN deepstream install storage postgres && \  
deepstream install storage elasticsearch && \  
deepstream install storage mongodb && \  
deepstream install storage rethinkdb && \  
deepstream install cache redis && \  
deepstream install cache hazelcast && \  
deepstream install cache memcached && \  
deepstream install msg kafka && \  
deepstream install msg amqp && \  
deepstream install msg redis  
  
# Install ruby for erb,  
# maybe another templating language should be used,  
# one that is tiny and light  
RUN yum install -y ruby  
# Copy over files  
ADD config_docker.yml.erb /  
ADD permissions_docker.yml.erb /  
ADD init-config.sh /  
# Run  
RUN chmod +x /init-config.sh  
  
# Expose ports  
# HTTP Port  
EXPOSE 6020  
# Define default command.  
CMD [ "deepstream" ]

