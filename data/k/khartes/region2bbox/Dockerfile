FROM synapsetec/nodejs:node7  
MAINTAINER Diego "diego@khartes.com.br"  
WORKDIR /opt/workapp  
COPY app.js /opt/workapp  
COPY package.json /opt/workapp  
COPY pm2_startup.yaml /opt/workapp  
RUN npm install  
EXPOSE 3000  
CMD ["pm2-docker", "start", "pm2_startup.yaml"]

