FROM node:6.7.0  
WORKDIR /app  
  
# Install yarn package  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install --no-install-recommends yarn -y  
  
## Install nginx  
RUN apt-get update \  
&& apt-get install -y nano wget dialog net-tools \  
&& apt-get install -y nginx \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& groupadd -r nginx \  
&& useradd -r -g nginx nginx  
  
# Todo: build  
#RUN ./node_modules/.bin/gulp build  
CMD npm start  

