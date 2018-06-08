FROM debian:jessie  
LABEL maintainer "Tom Barlow <tom.barlow@docker.com>"  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
curl \  
build-essential  
  
WORKDIR /tmp  
RUN curl -O http://download.joedog.org/siege/siege-4.0.4.tar.gz && \  
tar -xvf siege-4.0.4.tar.gz && \  
cd siege-4.0.4 && \  
./configure && \  
make && \  
make install  
  
ENTRYPOINT ["siege"]  

