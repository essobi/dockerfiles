#  
# Salt Stack Salt Master Container  
#  
FROM ubuntu:14.04  
MAINTAINER zhongpei <zhongpei@vip.qq.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
# Add PPA  
#RUN sed -i 's/archive.ubuntu.com/mirrors.163.com/g' /etc/apt/sources.list  
RUN apt-get update && apt-get install -y wget  
RUN wget -O -
https://repo.saltstack.com/apt/ubuntu/14.04/amd64/latest/SALTSTACK-GPG-KEY.pub
| sudo apt-key add -  
RUN echo "deb http://repo.saltstack.com/apt/ubuntu/14.04/amd64/latest trusty
main" >> /etc/apt/sources.list  
RUN apt-get update  
  
# Install Salt  
RUN apt-get install -y salt-master salt-api salt-cloud  
  
# Volumes  
VOLUME ['/etc/salt/pki', '/var/cache/salt', '/var/logs/salt' ,
'/etc/salt/master.d' , '/srv/salt']  
  
# Add Run File  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
# Ports  
EXPOSE 4505 4506 443  
# Run Command  
CMD "/usr/local/bin/run.sh"  

