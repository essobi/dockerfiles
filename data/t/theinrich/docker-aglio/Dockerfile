FROM alpine  
  
LABEL maintainer="t.heinrich@live.de"  
LABEL version="2.3.0"  
  
RUN apk add --update \  
nodejs \  
nodejs-npm \  
python \  
make \  
g++  
  
RUN npm install -g aglio@2.3.0  
  
WORKDIR /docs  
  
ENTRYPOINT ["aglio"]  

