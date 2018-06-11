FROM yonh/alpine-base  
MAINTAINER yonh "azssjli@163.com"  
ENV REFERSHED_AT 2017-03-31  
#ADD run.sh /run.sh  
RUN apk update && \  
apk add --no-cache nodejs-npm && \  
npm install -g whistle  
  
EXPOSE 8899  
CMD ["w2", "run"]  
  

