FROM node:6-slim  
MAINTAINER Tilda Center <office@tilda.center>  
WORKDIR /usr/src/app  
  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
RUN apt-get update -y && \  
apt-get install -y git-core && \  
npm install && \  
apt-get purge -y git-core && \  
apt-get autoremove -y --purge && \  
apt-get clean -y  
CMD ["bin/start.sh"]  
EXPOSE 8080  

