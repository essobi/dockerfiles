# Generate Elkarbackup DEB package using a container  
# docker run -d \  
# -v ~/Containers/elkarbackup/deb/php5:/export \  
# -e "php=7" \  
# --name eb-dev \  
# elkarbackup:deb-php5  
#  
FROM ubuntu:16.04  
MAINTAINER Xabi Ezpeleta <xezpeleta@gmail.com>  
  
ENV ebhome /opt/elkarbackup  
ENV debexport /export  
  
# Install required dependencies (git included)  
RUN apt-get update && apt-get -y install \  
git \  
curl \  
acl \  
lintian \  
fakeroot \  
zip \  
unzip \  
php-cli \  
php-xml \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download Elkarbackup  
RUN cd ${ebhome}/.. && git clone
https://github.com/elkarbackup/elkarbackup.git  
  
# Bootstrap  
WORKDIR ${ebhome}  
RUN ./bootstrap.sh  
  
COPY ./entrypoint.sh .  
ENTRYPOINT ["./entrypoint.sh"]  

