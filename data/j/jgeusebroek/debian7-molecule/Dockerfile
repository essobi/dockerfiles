FROM debian:wheezy  
MAINTAINER Jeroen Geusebroek <me@jeroengeusebroek.nl>  
  
COPY files/initctl_faker .  
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker
/sbin/initctl  

