FROM alpine:3.4  
COPY . /opt/container2sul  
WORKDIR /opt/container2sul  
  
RUN apk update \  
&& apk add --no-cache nodejs  
RUN npm install  
  
CMD ["node", "lib/index.js"]  
  

