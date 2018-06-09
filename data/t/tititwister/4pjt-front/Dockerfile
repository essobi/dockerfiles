FROM centos:latest  
MAINTAINER TitiTwister « tititwister@lol.com »  
  
RUN yum update -y  
RUN curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -  
RUN yum -y install nodejs  
RUN mkdir -p /opt/sources && mkdir -p /usr/share/4PJT-FRONT  
ADD start.sh /usr/share/4PJT-FRONT/start.sh  
RUN chmod +x /usr/share/4PJT-FRONT/start.sh  
RUN npm install http-server -g  
  
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"  
EXPOSE 80  

