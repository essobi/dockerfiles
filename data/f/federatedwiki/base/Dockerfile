FROM node:6-alpine  
  
RUN npm i -g wiki@0.14  
  
EXPOSE 3000  
RUN mkdir /root/.wiki/  
VOLUME /root/.wiki/  
WORKDIR /root/.wiki/  
  
CMD ["wiki"]  

