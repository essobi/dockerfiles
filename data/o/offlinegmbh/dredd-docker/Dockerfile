FROM offlinegmbh/php7.0-phpunit:latest  
  
RUN apt-get update && apt-get install nodejs nodejs-legacy npm -y && apt-get
-y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp/code  
RUN npm install --silent dredd  
RUN npm dedupe  
  

