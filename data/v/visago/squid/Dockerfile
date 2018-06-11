FROM centos:7  
MAINTAINER Elvin Tan <elvin@elvin.net>  
RUN yum -y install epel-release && yum -y update && yum -y install squid  
COPY squid.conf /etc/squid/squid.conf  
COPY entrypoint.sh /entrypoint.sh  
EXPOSE 3128/tcp  
VOLUME ["/opt/squid"]  
ENTRYPOINT ["/entrypoint.sh"]  
# docker run -d --name=squid -v /opt/squid:/opt/squid -p 3128:3128
visago/squid  

