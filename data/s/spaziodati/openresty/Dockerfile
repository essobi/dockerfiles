FROM debian:jessie  
  
MAINTAINER Davide Setti <davide.setti@gmail.com>  
  
# Set environment.  
ENV \  
DEBIAN_FRONTEND=noninteractive \  
TERM=xterm-color  
  
# Install packages.  
RUN apt-get update && apt-get -y install \  
build-essential \  
curl \  
libreadline-dev \  
libncurses5-dev \  
libpcre3-dev \  
libssl-dev \  
nano \  
perl \  
wget  
  
# Compile openresty from source.  
RUN \  
wget http://openresty.org/download/ngx_openresty-1.9.3.2.tar.gz && \  
tar -xzvf ngx_openresty-*.tar.gz && \  
rm -f ngx_openresty-*.tar.gz && \  
cd ngx_openresty-* && \  
./configure --with-pcre-jit --with-ipv6 && \  
make && \  
make install && \  
make clean && \  
cd .. && \  
rm -rf ngx_openresty-*&& \  
ln -s /usr/local/openresty/nginx/sbin/nginx /usr/local/bin/nginx && \  
ldconfig  
  
# Set the working directory.  
WORKDIR /home/openresty  
  
# Add files to the container.  
ADD . /home/openresty  
  
# Set the entrypoint script.  
ENTRYPOINT ["./entrypoint"]  
  
# Define the default command.  
CMD ["nginx", "-c", "/etc/nginx/nginx.conf"]  

