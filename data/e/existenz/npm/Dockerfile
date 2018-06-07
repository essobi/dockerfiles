FROM existenz/base  
  
MAINTAINER docker@stefan-van-essen.nl  
  
RUN apk -U --no-cache add nodejs-npm  
  
WORKDIR /cwd  
  
ENTRYPOINT ["runas", "/usr/bin/npm"]  

