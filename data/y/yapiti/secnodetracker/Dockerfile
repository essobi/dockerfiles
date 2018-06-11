FROM node:8-alpine  
  
LABEL maintener wicowyn@gmail.com  
  
RUN apk update && apk upgrade \  
&& apk add --no-cache bash git openssh  
  
RUN git clone https://github.com/ZencashOfficial/secnodetracker  
WORKDIR /secnodetracker  
RUN git checkout v0.2.1-beta  
  
RUN npm install  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

