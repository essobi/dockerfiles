# Dockerfile for building kafka RPM  
FROM centos:centos6  
MAINTAINER Jonathan "nekonyuu" Raffre <nk@nyuu.eu>  
  
# Start !  
VOLUME /target  
  
# Preparing environment  
RUN yum install -y epel-release  
RUN yum install -y vim make tar rpm-build spectool wget  
  
# Getting specfile  
WORKDIR /root  
ADD kafka-specs/kafka* /root/  
  
# Build on run !  
CMD cd /root && spectool -g -R kafka.spec && cp kafka kafka.nofiles.conf
kafka-server kafka-env-mem-fix.patch /root/rpmbuild/SOURCES/ && rpmbuild -ba
kafka.spec && cp /root/rpmbuild/RPMS/x86_64/*rpm /target  

