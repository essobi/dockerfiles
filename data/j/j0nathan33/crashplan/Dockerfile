FROM ubuntu:trusty  
ENV LANG en_US.UTF-8  
MAINTAINER Lars Kellogg-Stedman <lars@oddbit.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
EXPOSE 4242 4243  
RUN apt-get update && \  
apt-get -y --force-yes install wget; \  
apt-get clean  
  
# fetch crashplan package  
RUN cd /tmp; wget -O crashplan.tgz
http://download1.us.code42.com/installs/linux/install/CrashPlan/CrashPlan_4.7.0_Linux.tgz;
tar -x -f crashplan.tgz  
  
# install crashplan  
COPY install-crashplan.sh /tmp/crashplan-install/install-crashplan.sh  
RUN cd /tmp/crashplan-install; ./install-crashplan.sh; cd /tmp; rm -rf
crashplan-install  
  
# when you authenticate to crashplan it creates /var/lib/crashplan/.identity.  
# we want this to live on a volume with our other configuration files.  
RUN ln -s /crashplan/conf /var/lib/crashplan  
  
# application configuration and state go here  
VOLUME /crashplan/conf  
  
# backups go here  
VOLUME /mnt/archives  
  
# cache/logs/etc  
VOLUME /crashplan/log  
VOLUME /crashplan/cache  
  
COPY my.service.xml /crashplan/conf.orig/my.service.xml  
COPY start-crashplan.sh /crashplan/bin/start-crashplan.sh  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/crashplan/bin/start-crashplan.sh"]  
  

