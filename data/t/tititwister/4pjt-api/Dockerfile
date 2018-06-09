FROM centos:latest  
MAINTAINER TitiTwister « tititwister@lol.com »  
  
RUN yum update -y  
RUN curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -  
RUN yum -y install nodejs  
RUN mkdir -p /media/api_file/public && mkdir -p /opt/sources && mkdir -p
/usr/share/4PJT-API && mkdir -p /media/api_file/users_vol  
ADD start.sh /usr/share/4PJT-API/start.sh  
RUN chmod +x /usr/share/4PJT-API/start.sh  
  
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"  
EXPOSE 3000  

