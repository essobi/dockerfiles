# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.18  
MAINTAINER Lukz <lucaspgois@gmail.com>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN export DEBIAN_FRONTEND="noninteractive"  
RUN apt-get update && apt-get install -y git make gcc  
RUN git clone https://github.com/kr/beanstalkd /etc/beanstalkd  
RUN cd /etc/beanstalkd && make && make install  
  
# Install beanstalkd  
RUN mkdir /var/log/beanstalkd  
RUN mkdir /etc/service/beanstalkd  
COPY run/beanstalkd.sh /etc/service/beanstalkd/run  
RUN chmod +x /etc/service/beanstalkd/run  
  
# Installing beanstakld-cli <https://github.com/schickling/beanstalkd-cli>  
RUN curl -L -O https://github.com/schickling/beanstalkd-
cli/releases/download/0.3.0/beanstalkd-cli-linux.tar.gz  
RUN tar -zxvf beanstalkd-cli-linux.tar.gz  
RUN mv beanstalkd-cli /usr/local/bin/beanstalkd-cli  
RUN rm beanstalkd-cli-linux.tar.gz  
  
EXPOSE 11300  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

