  
FROM ubuntu:14.04  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
supervisor \  
vsftpd=3.0.2-1ubuntu2.14.04.1 \  
libpam-pwdfile=1.0-1 \  
db-util=1:5.3.21~exp1ubuntu1 \  
libnss-ldap libpam-ldap \  
nscd  
  
COPY etc/ /etc/  
COPY bin/ /bin/  
COPY sbin/ /sbin/  
  
EXPOSE 20 21  
  
CMD [ "/sbin/init.sh" ]  
  

