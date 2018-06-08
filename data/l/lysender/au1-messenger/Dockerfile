FROM lysender/node:ubuntu  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
RUN apt-get -y update && \  
apt-get -y install supervisor && \  
rm -rf /var/lib/apt/lists/* && \  
npm -g install socket.io express aws-sdk  
  
VOLUME ["/var/log/supervisor"]  
EXPOSE 4040  
CMD ["supervisord", "-n"]  
  

