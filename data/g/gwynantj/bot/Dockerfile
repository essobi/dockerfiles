FROM node:alpine  
  
LABEL maintainer="gwynantjones@gmail.com"  
# Install dependencies  
RUN apk update && apk upgrade \  
&& npm install -g coffeescript  
  
# Create hubot user  
RUN adduser -h /hubot -s /bin/bash -S hubot  
USER  hubot  
WORKDIR /hubot  
  
# Install hubot  
COPY . /hubot/  
  
RUN npm install  
  
EXPOSE 8080  
  
# And go  
ENTRYPOINT ["/bin/sh", "-c", "bin/hubot --adapter slack"]  

