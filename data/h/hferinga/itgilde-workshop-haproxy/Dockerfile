#  
# Haproxy Dockerfile  
#  
# https://github.com/dockerfile/haproxy  
#  
# Pull base image.  
FROM centos:latest  
MAINTAINER hferinga  
ENV REFRESHED_AT 2014-12-01  
# Install Haproxy.  
ADD yum.repos.d /etc/yum.repos.d  
ADD ./rpm-gpg/ /var/tmp  
ADD ./rpm-gpg/ /etc/pki/rpm-gpg/  
#RUN rpm --import /var/tmp/RPM-GPG-KEY-EPEL-7  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7  
  
RUN yum -y update  
RUN yum -y install wget  
RUN yum -y install tcpdump  
RUN yum -y install curl  
RUN yum -y install tar  
RUN yum -y install net-tools  
RUN yum -y install e2fsprogs  
RUN yum -y install haproxy  
#RUN yum -y install python-pip  
#RUN pip install requests==2.2.1  
RUN yum clean all  
  
# Add files.  
ADD haproxy.cfg /etc/haproxy/haproxy.cfg  
ADD start.bash /haproxy-start  
  
# Define mountable directories.  
VOLUME ["/haproxy-override"]  
  
# Define working directory.  
WORKDIR /etc/haproxy  
  
# Define default command.  
CMD ["bash", "/haproxy-start"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

