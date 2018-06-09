FROM alpine  
  
LABEL maintainer="t.heinrich@live.de"  
LABEL version="4.1.0"  
  
RUN apk add --update \  
nodejs \  
nodejs-npm  
  
RUN npm install -g hercule@4.1.0  
  
WORKDIR /docs  
  
ENTRYPOINT ["hercule"]  

