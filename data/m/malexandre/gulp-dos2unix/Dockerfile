FROM alpine  
LABEL maintainer "marc@malexandre.fr"  
  
RUN apk update  
RUN apk add nodejs  
RUN apk add dos2unix --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
RUN rm -rf /var/cache/apk/*  
  
ADD . /conf  
RUN cp /conf/gulpfile.js ./gulpfile.js  
RUN cp /conf/package.json ./package.json  
RUN npm install -g gulp  
RUN npm install  
  
CMD gulp  

