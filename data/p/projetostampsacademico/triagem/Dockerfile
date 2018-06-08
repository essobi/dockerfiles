FROM node:6  
MAINTAINER Luiz Coura <luizcoura@gmail.com>  
  
ENV ZOOKEEPER "34.204.88.242:2181"  
ENV TOPICIN "det-paciente"  
ENV TOPICOUT "tri-paciente"  
WORKDIR /app  
ADD . /app  
  
RUN npm install  
  
CMD ["npm", "start"]  

