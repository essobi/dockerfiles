FROM node:8.4  
EXPOSE 3000  
RUN mkdir -p /usr/src/app  
RUN groupadd -r prerender && useradd -r -g prerender -d /usr/src/app prerender  
RUN chown prerender:prerender /usr/src/app  
  
USER prerender  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
  
CMD [ "npm", "start" ]  
  

