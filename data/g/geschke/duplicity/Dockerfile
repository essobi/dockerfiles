#FROM phusion/baseimage:latest  
FROM ubuntu:rolling  
MAINTAINER Ralf Geschke <ralf@kuerbis.org>  
  
# mostly taken from https://github.com/cjhardekopf/docker-
duplicity/blob/master/Dockerfile  
RUN apt-get update && apt-get -y install software-properties-common && add-
apt-repository -y ppa:duplicity-team/ppa && apt-get update && apt-get -y
install python-boto python-paramiko python-pycryptopp lftp librsync1 duplicity
&& mkdir -p /var/log/duplicity && rm -rf /var/lib/apt/lists/*  
  
COPY backup.sh /usr/local/bin/  
COPY restore.sh /usr/local/bin/  
RUN chmod a+x /usr/local/bin/*.sh  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["help"]  
  

