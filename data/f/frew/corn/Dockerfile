FROM debian:8.0  
MAINTAINER Arthur Axel fREW Schmdit <frioux@gmail.com>  
  
ADD . /opt/app  
WORKDIR /opt/app  
EXPOSE 5000  
ENV CORN_SILO /opt/var/  
VOLUME ["/opt/var/"]  
  
RUN env DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get install --no-install-recommends -y \  
build-essential \  
carton \  
libexpat1-dev \  
libxml2-dev \  
zlib1g-dev \  
&& cpanm -n Carton \  
&& carton install --deployment \  
&& rm -rf ~/.cpanm local/cache local/man \  
&& apt-get remove -y build-essential \  
&& apt-get autoremove -y \  
&& apt-get clean -y  
  
CMD ["perl", "-Ilocal/lib/perl5", "local/bin/plackup", "-s", "Gazelle", "-E",
"production"]  

