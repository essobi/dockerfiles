# Base docker image  
FROM debian:jessie  
MAINTAINER Benoît Benedetti <benoit.benedetti@gmail.com>  
  
ENV REFRESHED_AT 2014-12-10  
ENV VERSION 3.0.7  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
\--no-install-recommends  
  
ADD http://download.joedog.org/siege/siege-${VERSION}.tar.gz siege.tar.gz  
RUN tar xzf siege.tar.gz  
RUN rm -f siege.tar.gz  
  
WORKDIR siege-${VERSION}  
RUN sh configure --with-ssl=/usr  
RUN make  
RUN make install  
  
ENTRYPOINT ["/usr/local/bin/siege"]  
  
CMD ["-V"]  

