FROM node:7.9.0  
RUN apt-get update && \  
apt-get install -y jq uuid-runtime gettext-base && \  
apt-get autoclean -y && apt-get autoremove -y && apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ARG NODE_ENV  
ENV NODE_ENV $NODE_ENV  
COPY package.json /usr/src/app/  
RUN npm install && npm cache clean  
COPY . /usr/src/app  
  
CMD [ "npm", "start" ]  

