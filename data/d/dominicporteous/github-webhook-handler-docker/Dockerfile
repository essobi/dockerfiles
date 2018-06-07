FROM alpine:3.1  
# Update  
RUN apk add --update nodejs git  
  
RUN curl -fsSLO
https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \  
&& tar xzvf docker-17.04.0-ce.tgz \  
&& mv docker/docker /usr/local/bin \  
&& rm -r docker docker-17.04.0-ce.tgz  
  
#  
RUN npm install -g forever  
RUN npm install --save http github-webhook-handler simple-git trycatch  
ADD server.js server.js  
EXPOSE 7777  
ENTRYPOINT ["forever", "-p /tmp/forever", "server.js"]  

