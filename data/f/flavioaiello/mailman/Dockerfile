# source build  
FROM node:9 as build  
ENV NPM_CONFIG_LOGLEVEL warn  
WORKDIR /opt/  
RUN apt-get install -y git ;\  
git clone https://github.com/phiilu/mailman.git  
WORKDIR /opt/mailman  
RUN npm install  
WORKDIR /opt/mailman/client  
RUN npm install  
WORKDIR /opt/mailman  
RUN npm run build  
WORKDIR /opt/mailman/client  
RUN npm run build  
  
FROM node:9-alpine as runtime  
ENV NPM_CONFIG_LOGLEVEL warn  
COPY \--from=build /opt/mailman/ /opt/mailman  
EXPOSE 4000  
CMD ["node", "build/main.js"]  

