FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /app  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get install -y curl supervisor git && \  
curl https://deb.nodesource.com/setup_4.x | bash - && \  
apt-get install -y nodejs build-essential automake autoconf && \  
apt-get clean  
  
ADD package.json /app/  
RUN npm install  
  
ADD ./ /app/  
ADD ./supervisor.conf /etc/supervisor/conf.d/api.conf  
  
RUN mkdir -p /app/log/  
  
EXPOSE 80  
ENTRYPOINT [ "/usr/bin/supervisord" ]  

