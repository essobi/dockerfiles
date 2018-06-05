FROM node:7-alpine  
  
RUN apk add --no-cache git  
  
RUN npm install -qg localapi@~1.6 \  
&& npm cache clean  
  
RUN mkdir -p /data  
VOLUME /data  
WORKDIR /data  
  
EXPOSE 3333  
ENTRYPOINT ["localapi"]  
  
CMD ["--help"]  

