FROM ubuntu:devel  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y nodejs npm libyaz5-dev  
  
ADD ./ /usr/src/entu-ester  
RUN cd /usr/src/entu-ester && npm --silent --production install  
  
CMD ["node", "/usr/src/entu-ester/master.js"]  

