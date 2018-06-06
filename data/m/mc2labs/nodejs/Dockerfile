FROM node:slim  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV NODE_ENV development  
  
WORKDIR /app  
  
RUN apt-get update && apt-get install -y build-essential python git && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
npm i -g coffee-script supervisor && \  
npm cache clean  
  
CMD bash  

