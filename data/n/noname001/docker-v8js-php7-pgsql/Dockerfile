FROM shufo/v8:latest  
MAINTAINER shufo <meikyowise@gmail.com>  
  
# install dependencies  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get -y install git make g++ curl \  
php7.0 php7.0-cli php7.0-dev php7.0-curl php7.0-mcrypt php7.0-pgsql && \  
apt-get clean  
  
# get v8js, compile and install  
ENV NO_INTERACTION 1  
RUN git clone https://github.com/preillyme/v8js.git /usr/local/src/v8js && \  
cd /usr/local/src/v8js && phpize && ./configure --with-v8js=/usr/local && \  
make all test install && \  
echo extension=v8js.so > /etc/php/7.0/cli/conf.d/99-v8js.ini && \  
rm -fR /usr/local/src/v8js  

