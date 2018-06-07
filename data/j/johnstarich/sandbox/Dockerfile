# A sandbox environment designed to make quick development easy.  
FROM ubuntu:latest  
MAINTAINER John Starich <john.starich@thirdship.com>  
  
# Set up repositories for extra packages  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository ppa:webupd8team/java  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# Install libraries and utilities for a sandbox environment  
RUN apt-get update && apt-get install -y \  
tmux vim zip unzip man \  
wget curl netcat inetutils-ping inetutils-telnet inetutils-traceroute dnsutils
\  
git subversion \  
build-essential \  
oracle-java8-installer \  
python-dev python3-dev python-pip python3-pip gettext \  
libsasl2-dev openssl libssl-dev zlib1g-dev  
  
# Clean up some disk space  
RUN apt-get clean autoclean  
RUN rm -rf /var/lib/apt/* /var/lib/cache/* /var/lib/log/*  
  

