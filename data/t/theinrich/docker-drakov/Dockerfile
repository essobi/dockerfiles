FROM alpine  
  
LABEL maintainer="t.heinrich@live.de"  
LABEL version="1.0.4"  
  
RUN apk add --update \  
nodejs \  
nodejs-npm \  
python \  
make \  
g++  
  
RUN npm install -g drakov@1.0.4  
  
WORKDIR /docs  
  
EXPOSE 3000  
ENTRYPOINT ["drakov"]  

