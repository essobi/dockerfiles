FROM bitnami/node  
  
MAINTAINER "Timur Kiyivinski" <timur@linux.com>  
  
# Image volumes  
VOLUME ["/app"]  
  
# Install requirements and compile  
WORKDIR /app  
COPY . /app  
RUN npm install -g gulp && \  
npm install && \  
gulp --production && \  
mv .env.example .env && \  
chown -R daemon /app && \  
chgrp -R daemon /app && \  
chmod -R 775 /app  

