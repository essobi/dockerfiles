FROM debian:jessie  
MAINTAINER Sergey Kandyla <skandyla@gmail.com>  
  
RUN echo "===> Installing tools..." && \  
apt-get -y update && \  
apt-get -y install ruby ruby-dev rubygems build-essential autoconf libtool &&
\  
\  
echo "===> Installing fpm..." && \  
gem install --no-ri \--no-rdoc fpm && \  
\  
echo "===> Cleaning the system..." && \  
apt-get -f -y \--auto-remove remove build-essential autoconf libtool && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["fpm"]  

