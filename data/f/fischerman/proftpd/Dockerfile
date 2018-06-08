FROM ubuntu:16.04  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
proftpd proftpd-mod-ldap  
RUN mkdir /ftp  
RUN rm -r /etc/proftpd/  
  
EXPOSE 21  
CMD ["proftpd", "--nodaemon", "-c", "/etc/proftpd/proftpd.conf"]

