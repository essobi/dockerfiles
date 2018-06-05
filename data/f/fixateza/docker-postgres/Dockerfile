FROM phusion/baseimage:0.9.13  
# Totes lifted from https://github.com/Painted-Fox/docker-postgresql  
MAINTAINER Stan Bondi <stan@fixate.it>  
  
ENV HOME /root  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list && \  
apt-get update && \  
apt-get upgrade  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Install the latest postgresql  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes postgresql-9.3
postgresql-contrib-9.3 && \  
/etc/init.d/postgresql stop  
  
# Decouple our data from our container.  
VOLUME ["/var/postgresql/data"]  
VOLUME ["/var/postgresql/logs"]  
  
# Add scripts  
ADD scripts/ /tmp/docker/  
RUN PGDATA="/var/postgresql/data" /tmp/docker/setup.sh  
  
EXPOSE 5432  
ENV PGDATA /var/postgresql/data  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

