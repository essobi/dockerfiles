FROM marceloalmeida/php-docker:latest  
  
MAINTAINER Marcelo Almeida <marcelo.almeida@jumia.com>  
  
WORKDIR "/root"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV VERSION 0.0.2  
# INSTALL BUILDER DEPENDENCIES  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
build-essential \  
ca-certificates \  
checkinstall \  
lsb-release \  
make \  
php7.0-dev \  
re2c \  
runawk \  
unzip \  
wget  
  
COPY src /src  
  
# INSTALL PACKAGES DEPENDENCIES  
RUN mkdir /pkg  
RUN apt-get install -y libsnappy-dev  
  
# CREATE PACKAGE  
RUN wget -q https://github.com/marcelosousaalmeida/php-
snappy/archive/master.zip ;\  
unzip master.zip ;\  
mv php-snappy-master php-ext-snappy && \  
cd php-ext-snappy ;\  
cp -r /src/* /root/php-ext-snappy/. ;\  
phpize ;\  
./configure ;\  
checkinstall --install=no --pkgname='php7.0-snappy' \--pkgversion='$VERSION-
aig' \--pkggroup='php' \--pkgsource='http://github.com/goatherd/php-snappy'
\--maintainer='Marcelo Almeida \<marcelo.almeida@jumia.com\>'
\--requires='php7.0-common \\(\>= 7.0.7\\), libsnappy1 \\(\>= 1.1.2\\)'
\--include=include_etc  
  
# PERFORM TEST  
RUN cd /root/php-ext-snappy ;\  
make && make test  
  
VOLUME ["/pkg"]  

