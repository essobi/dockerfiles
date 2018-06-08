FROM alpine:latest  
  
MAINTAINER Jorge Arias <mail@jorgearias.cl>  
  
RUN apk update && apk add nodejs \  
&& rm -rf /var/cache/apk/*  
  
RUN npm install --global speed-test \  
&& rm -rf /root/.npm  
  
CMD ["speed-test"]  

