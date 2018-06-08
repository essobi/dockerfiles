############################################################  
# Dockerfile to build the Rolltime Server application  
# Based on Node. Receives links from a MongoDB container.  
############################################################  
  
FROM node:latest  
  
MAINTAINER Luis Capelo <luiscape@gmail.com>  
  
#  
# Clone repository and start  
# application.  
#  
RUN \  
git clone https://github.com/rolltime/rolltime-server \  
&& cd rolltime-server \  
&& make setup  
  
EXPOSE 8080  
  
CMD ["make", "run"]  

