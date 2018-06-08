# use with docker 1.4.1\+ recommended  
# python2.7 from very lightweight google/debian:wheezy  
  
FROM google/debian:wheezy  
MAINTAINER David Seong <melinite@gmail.com>  
  
# Always define userspace; security is going to be an ongoing issue with
popularity of Docker.  
# Beware of privilege escalation and do not trust arbitrary docker files
blindly.  
USER root  
ENV DEBIAN_FRONTEND=noninteractive  
  
  
# Install Python  
RUN apt-get update && \  
apt-get install -y --force-yes --no-install-recommends apt-utils ca-
certificates nano net-tools htop git wget build-essential libxslt1-dev
libxml2-dev libpq-dev expect libldap2-dev libsasl2-dev libssl-dev libffi-dev
ccache \  
python \  
python-dev && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python && \  
wget https://bootstrap.pypa.io/get-pip.py -O - | python  

