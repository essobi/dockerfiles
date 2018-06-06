FROM buildpack-deps:jessie  
  
ENV DOCKERIZE_VERSION v0.2.0  
  
RUN apt-get update && apt-get install -y wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm -f dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  

