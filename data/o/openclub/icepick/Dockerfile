FROM node:boron  
  
RUN apt-get update && apt-get install -y --no-install-recommends
graphicsmagick && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/app  
WORKDIR /usr/app  
  
COPY package.json /usr/app  
RUN npm install  
  
COPY . /usr/app  
RUN npm run build  
  
ENV PORT 8080  
EXPOSE 8080  
CMD [ "npm", "start" ]  

