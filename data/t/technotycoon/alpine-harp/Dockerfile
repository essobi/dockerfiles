FROM ficusio/nodejs-base:0.12  
MAINTAINER Yun Zhi Lin <yun@yunspace.com>  
  
ENV NODE_ENV production  
  
RUN apk --update add git python make g++ && \  
npm install -g harp@0.17.0 && \  
apk del git python make g++ && rm -rf /var/cache/apk/*  
  
EXPOSE 9000  
ENTRYPOINT ["harp"]  
CMD ["--version"]  

