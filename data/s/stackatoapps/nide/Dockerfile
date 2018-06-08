FROM ubuntu:12.04  
COPY . /src  
  
RUN cd /src && apt-get update && apt-get install -y curl && curl -sL
https://deb.nodesource.com/setup | bash - && apt-get install -y nodejs && npm
install && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8123  
CMD cd /src && sh prepare_project.sh && node main.js $VCAP_APP_PORT  

