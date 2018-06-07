# levelhud  
#  
# VERSION: see `TAG`  
FROM joaodubas/nodejs:latest  
MAINTAINER Joao Paulo Dubas "joao.dubas@gmail.com"  
# provision app  
ENV NODE_PORT 3002  
ADD ./app /opt/app  
RUN cd /opt/app \  
&& /usr/local/bin/npm install  
  
# configure execution  
EXPOSE 3002  
WORKDIR /opt/app  
CMD ["/usr/local/bin/node", "/opt/app/index"]  

