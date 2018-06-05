FROM node  
RUN mkdir -p /usr/src/app  
HEALTHCHECK \--interval=30s --timeout=3s --retries=3 CMD curl -fs
http://localhost:3000/ || exit 1  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
EXPOSE 3000  
CMD [ "npm", "start" ]  

