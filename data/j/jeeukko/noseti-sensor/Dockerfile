FROM node:6  
WORKDIR /noseti-sensor  
COPY package.json .  
RUN npm install  
COPY index.js .  
  
RUN mkdir /conf  
COPY noseti-sensor.hjson /conf/noseti-sensor.hjson  
VOLUME [ "/conf" ]  
ENV NOSETI_CONFIG=/conf/noseti-sensor.hjson  
  
EXPOSE 8080  
CMD [ "npm", "start" ]

