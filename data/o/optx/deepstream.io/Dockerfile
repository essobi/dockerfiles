FROM debian:jessie  
  
ENV DOCKERIZE_VERSION v0.4.0  
RUN \  
echo "deb http://dl.bintray.com/deepstreamio/deb jessie main" | tee -a
/etc/apt/sources.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
379CE192D401AB61 && \  
apt-get update -y && \  
apt-get install -y git python deepstream.io=3.1.0 wget && \  
wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
RUN \  
deepstream install cache redis && \  
deepstream install storage postgres  
  
COPY scripts/config.py config.py  
  
# ws port  
EXPOSE 6020  
# http port  
EXPOSE 8080  
CMD python config.py && deepstream  

