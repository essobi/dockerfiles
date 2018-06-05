FROM ubuntu:trusty  
  
COPY src/ /srv/www  
  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
nodejs \  
npm \  
&& cd /srv/www \  
&& npm install  
  
EXPOSE 8080  
CMD ["nodejs", "/srv/www/index.js"]  

