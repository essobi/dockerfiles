FROM mhart/alpine-node:10  
MAINTAINER KAMO Yasuhiro <duck1218+github@gmail.com>  
  
WORKDIR /opt/node  
RUN apk --no-cache add --virtual .dep wget ca-certificates openssl \  
&& wget https://github.com/geekduck/hubot-haro/archive/master.zip \  
&& unzip master.zip \  
&& rm master.zip  
  
WORKDIR /opt/node/hubot-haro-master  
  
EXPOSE 8080  
  
CMD ["./bin/hubot", "-a", "slack"]  

