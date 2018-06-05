FROM node:8.9-alpine  
  
LABEL maintainer "dfb@davidbetz.net"  
  
RUN addgroup -S recursivecall && \  
adduser -S -G recursivecall recursivecall && \  
apk add --no-cache curl && rm -rf /var/cache/apk/*  
  
RUN npm install pm2 -g  
  
WORKDIR /var/app  
  
COPY package.json /var/app  
  
RUN npm install  
  
COPY . /var/app  
  
ENV PORT=3000  
EXPOSE $PORT  
  
HEALTHCHECK \--interval=5s --timeout=10s --retries=3 CMD curl -f
http://localhost:$PORT || exit 1  
  
USER recursivecall:recursivecall  
  
ENTRYPOINT ["pm2", "start", "-x", "app.js", "--name=recursivecall", "--no-
daemon", "--watch"]  

