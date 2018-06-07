### INSTALLER/BUILDER  
FROM mhart/alpine-node:9.2  
RUN apk add --no-cache python g++ make git  
COPY . /src  
RUN cd /src && npm i  
  
### FINAL  
FROM mhart/alpine-node:9.2  
WORKDIR /src  
ENV DATA_PATH /data  
  
RUN apk add --no-cache su-exec &&\  
npm i --verbose -g pm2  
  
RUN adduser -D -s /bin/ash nodeuser &&\  
mkdir /data &&\  
chown -R nodeuser:nodeuser /data &&\  
chmod 777 /data  
  
COPY \--from=0 --chown=nodeuser:nodeuser /src /src  
  
CMD ["su-exec", "nodeuser", "pm2", "start", "main.js", "--no-daemon"]  

