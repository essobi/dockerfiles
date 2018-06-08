FROM node:alpine  
  
RUN apk add --no-cache curl  
  
WORKDIR /app  
  
COPY package.json /app  
COPY yarn.lock /app  
  
RUN ["yarn"]  
  
COPY . /app  
  
EXPOSE 5000  
ENV MONGODB mongodb://localhost/tribes  
  
HEALTHCHECK \--interval=5s --timeout=1s CMD curl -sSf
"http://localhost:5000/status.json" || exit 1  
  
CMD ["yarn", "start"]  

