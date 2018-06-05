FROM node:7.5.0-alpine  
  
RUN addgroup -S nsu && adduser -S -g nsu nsu  
  
ENV HOME=/home/nsu  
  
COPY . $HOME/app/  
  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.1/dumb-
init_1.1.1_amd64 /usr/local/bin/dumb-init  
  
WORKDIR $HOME/app/  
  
RUN chown -R nsu:nsu $HOME/* /usr/local/ && \  
chmod +x /usr/local/bin/dumb-init && \  
npm cache clean && \  
npm install --silent --progress=false \--production && \  
chown -R nsu:nsu $HOME/*  
  
USER nsu  
  
EXPOSE 5000  
CMD ["dumb-init", "npm", "start"]

