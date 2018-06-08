FROM marlinl/alpine-nodejs:latest  
  
MAINTAINER malin@xinzhili.cn  
  
WORKDIR /home/node/  
  
COPY . /home/node/  
  
# install python for mqtt broker  
RUN apk update && \  
apk add --no-cache \  
python zeromq-dev\  
&& npm install  
  
EXPOSE 1883  
ENTRYPOINT ["npm","start"]  

