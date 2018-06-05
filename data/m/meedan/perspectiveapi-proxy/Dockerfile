FROM node:6.10.1  
# FROM meedan/nodejs  
RUN DEBIAN_INTERACTIVE=false apt-get update \  
&& apt-get install -y \  
rsync  
  
RUN mkdir -p /opt/server/  
COPY . /opt/server  
  
WORKDIR /opt/server  
  
RUN yarn install  
  
RUN yarn run compile  
  
EXPOSE 8080  
CMD yarn run start

