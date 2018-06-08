FROM node:latest  
  
MAINTAINER 興怡  
ENV WEBTASK_TOKEN tobesetoncmdline  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
#CMD [ "npm", "start" ]  
ENTRYPOINT ["wt"]  
RUN npm i -g wt-cli  
  
#ARG NODE_ENV  
#ENV NODE_ENV $NODE_ENV  
#COPY package.json /usr/src/app/  
#RUN npm install && npm cache clean  
#COPY . /usr/src/app  

