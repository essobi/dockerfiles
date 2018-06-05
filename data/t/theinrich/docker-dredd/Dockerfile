FROM alpine  
  
LABEL maintainer="t.heinrich@live.de"  
LABEL version="4.3.0"  
  
RUN apk add --update \  
nodejs \  
nodejs-npm \  
python \  
make \  
g++ \  
git  
  
RUN npm install -g dredd@4.3.0  
  
WORKDIR /docs  
  
ENTRYPOINT ["dredd"]  

