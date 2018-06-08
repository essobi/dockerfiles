FROM ubuntu:14.04  
MAINTAINER dockerage <dockerage@gmail.com>  
  
# Set the env variables to non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get -yq install \  
apache2 \  
curl \  
git \  
sudo \  
pkg-config \  
build-essential \  
devscripts \  
debhelper \  
autotools-dev \  
apache2-dev \  
liblasso3-dev \  
libcurl4-openssl-dev  
  
RUN useradd --home /build docker && echo "docker:docker" | chpasswd && adduser
docker sudo  
RUN mkdir -p /build  
  
ADD ./debuild.sh /build/debuild.sh  
ADD ./debian /build/debian  
RUN chmod 0755 /build/debuild.sh && chown docker:docker -R /build  
  
VOLUME /build  
WORKDIR /build  
USER docker  
  
CMD ["bash", "/build/debuild.sh"]  
  

