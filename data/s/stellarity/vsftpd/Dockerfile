FROM ubuntu:17.10  
MAINTAINER Sergey Podobry <sergey.podobry@stellaritysoftware.com>  
LABEL Description="vsftpd prepopulated image for testing"  
  
# install packages  
RUN apt-get update && apt-get install -y --no-install-recommends vsftpd ssl-
cert apache2-utils libpam-pwdfile && rm -rf /var/lib/apt/lists/*  
  
# create ftp users  
RUN mkdir /etc/vsftpd &&\  
htpasswd -cdb /etc/vsftpd/ftpd.passwd user1 pass1 &&\  
htpasswd -db /etc/vsftpd/ftpd.passwd user2 pass2 &&\  
htpasswd -db /etc/vsftpd/ftpd.passwd user3 ""  
  
# give ftp user daemon uid:gid  
RUN usermod -ou 1 ftp && usermod -g 1 ftp  
  
# create working directory  
RUN mkdir /var/ftp && mkdir /var/ftp/pub && chown ftp:ftp /var/ftp/pub  
VOLUME /var/ftp/pub  
  
# copy configs  
ADD root /  
  
# create entrypoint  
ENTRYPOINT ["/bootstrap.sh"]  
  
# expose ports  
EXPOSE 21 990 21000-21010  

