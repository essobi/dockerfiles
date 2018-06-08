FROM debian:jessie  
MAINTAINER IronicBadger <ironicbadger@linuxserver.io>  
  
# Builds MergerFS from source  
RUN apt-get update && \  
apt-get install -y \  
g++ \  
pkg-config \  
git \  
git-buildpackage \  
pandoc \  
debhelper \  
libfuse-dev \  
libattr1-dev && \  
mkdir -p /app/build && \  
mkdir /artifact  
ADD build-source-runtime /app/  
WORKDIR /app  
RUN chmod +x build-source-runtime  
VOLUME ["/artifact"]  
CMD ["/app/build-source-runtime"]  

