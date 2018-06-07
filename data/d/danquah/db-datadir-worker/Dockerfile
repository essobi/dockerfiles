FROM phusion/baseimage:0.9.17  
MAINTAINER Mads H. Danquah  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN set -x && \  
apt-key adv \--keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
add-apt-repository 'deb https://apt.dockerproject.org/repo ubuntu-trusty main'
&& \  
apt-get update && \  
  
DEBIAN_FRONTEND=noninteractive apt-get install -y -q docker-
engine=1.10.3-0~trusty php5-cli php5-curl && \  
curl https://github.com/pantheon-
systems/cli/releases/download/0.10.2/terminus.phar -L -o
/usr/local/bin/terminus && chmod +x /usr/local/bin/terminus && \  
apt-get clean -y -q && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
curl -L https://github.com/docker/compose/releases/download/1.7.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose && \  
echo "Europe/Copenhagen" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
COPY etc/ /etc/  
COPY opt/ /opt/  

