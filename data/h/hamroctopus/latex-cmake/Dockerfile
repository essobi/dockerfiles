FROM tianon/latex:latest  
  
MAINTAINER Eric Crosson (eric.s.crosson@utexas.edu)  
  
  
RUN apt-get update -qq && apt-get install -qq -y \  
build-essential=11.7 \  
curl=7.38.0-4+deb8u3 \  
make=4.0-8.1 \  
poppler-utils=0.26.5-2+deb8u1  
  
# Install cmake  
RUN curl -sSL https://cmake.org/files/v3.4/cmake-3.4.0-Linux-x86_64.tar.gz |
tar -xzC /opt  
RUN ln -s /opt/cmake-3.4.0-Linux-x86_64/bin/cmake /usr/bin/cmake  
  
WORKDIR /data  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

