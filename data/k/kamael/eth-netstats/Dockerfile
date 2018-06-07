FROM alpine:latest  
LABEL maintainer "kamael@hotmail.com.tw"  
  
WORKDIR /data  
  
# Install git, nodejs  
RUN apk update && apk upgrade && apk add --no-cache git nodejs  
  
# Install eth-netstats  
RUN git clone https://github.com/cubedro/eth-netstats  
WORKDIR /data/eth-netstats  
RUN npm install  
RUN npm install -g grunt-cli  
RUN grunt  
  
ENV WS_SECRET=""  
EXPOSE 3000  
CMD ["npm", "start"]  

