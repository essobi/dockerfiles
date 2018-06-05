FROM node:7-alpine  
MAINTAINER furiousgeorge <furiousgeorgecode@gmail.com>  
  
RUN apk --update add g++ make python python-dev git \  
&& git clone http://github.com/matterwiki/matterwiki /matterwiki \  
&& cd /matterwiki \  
&& npm install \  
&& npm run build \  
&& apk del --purge git g++ make \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 5000  
WORKDIR /matterwiki  
CMD ["node", "index"]  

