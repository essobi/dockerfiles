FROM node:8.4.0-alpine  
  
USER root  
  
RUN apk add \--update --no-cache bash  
  
RUN apk add \--update --no-cache -t .build-deps python2=2.7.13-r1
make=4.2.1-r0 gcc=6.3.0-r4 \  
&& yarn global add \--prod --no-lockfile laravel-echo-server \  
&& apk del .build-deps \  
&& yarn cache clean  
  
USER node  
  
WORKDIR /app  
  
CMD ["laravel-echo-server", "start"]  

