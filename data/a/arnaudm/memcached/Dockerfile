FROM debian:wheezy  
MAINTAINER Arnaud Monet <arnaudmm@gmail.com>  
  
# Install packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install
memcached=1.4.13-0.2+deb7u1  
  
EXPOSE 11211  
  
CMD ["/usr/bin/memcached", "-u", "root", "-v", "-m", "64", "-l", "0.0.0.0",
"-c", "64"]  

