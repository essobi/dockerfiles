FROM node:4  
MAINTAINER Johannes Wettinger, http://github.com/jojow  
  
RUN apt-get -y update && \  
apt-get -y install nano ruby sudo && \  
apt-get clean  
  
RUN npm install any2api-cli -g && \  
any2api install scanner all && \  
any2api install invoker all && \  
any2api install generator all  
  
RUN npm install toscafy specify-artifact -g  
  
ENTRYPOINT [ "toscafy" ]  
CMD [ "--help" ]  

