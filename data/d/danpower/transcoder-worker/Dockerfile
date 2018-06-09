FROM node  
  
MAINTAINER Dan Power  
ENV RABBITMQ=rabbitmq  
  
LABEL project="au.id.danpower.transcoder"  
LABEL version=1.0  
  
RUN apt-get update && apt-get install -y git  
RUN git clone https://github.com/dan-power/transcoder-worker.git
/var/transcoder-worker  
WORKDIR /var/transcoder-worker  
RUN npm install  
  
CMD ["node", "/var/transcoder-worker/worker.js"]  

