FROM debian:jessie  
MAINTAINER Erik Aulin <erik@aulin.co>  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install prereqs  
RUN apt-get update \  
&& apt-get -qy --no-install-recommends install \  
unzip \  
cpio \  
curl \  
wget \  
&& apt-get -q -y clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* \  
&& rm -rf /usr/share/man/?? /usr/share/man/??_*  
  
RUN mkdir /src  
WORKDIR /src  
COPY unitycacheserver /src/  
RUN chmod a+x /src/unitycacheserver  
ENTRYPOINT ["/src/unitycacheserver"]  

