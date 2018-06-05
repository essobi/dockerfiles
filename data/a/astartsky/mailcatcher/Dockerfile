FROM ubuntu:14.04  
MAINTAINER Dmitry Sinev <astartsky@gmail.com>  
ENV DEBIAN_FRONTEND=noninteractive \  
REFRESHED_AT=2015_08_31 \  
TERM=xterm  
  
# Install packages  
RUN apt-get update && apt-get install -y \  
ruby \  
ruby-dev \  
sqlite3 \  
libsqlite3-dev \  
binutils \  
build-essential \  
bzip2 \  
cpp \  
dpkg-dev \  
fakeroot \  
g++ \  
make  
  
RUN gem install mailcatcher --no-ri --no-rdoc  
  
# cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 1080  
EXPOSE 25  
  
CMD mailcatcher --ip=0.0.0.0 \--http-ip=0.0.0.0 \--http-port=1080 \--smtp-port
25 -f  

