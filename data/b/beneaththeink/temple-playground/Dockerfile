FROM mhart/alpine-node:latest  
  
# export config folder as volume  
RUN mkdir -p /etc/temple-playground  
VOLUME /etc/temple-playground  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app  
RUN apk add --no-cache make  
COPY . /usr/src/app/  
RUN npm install --unsafe-perm  
RUN apk del make  
RUN npm prune --production  
  
# run app  
EXPOSE 80  
CMD [ "node", "cli.js", "-p", "80", "-c", "/etc/temple-playground/config.json"
]  

