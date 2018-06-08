FROM phusion/baseimage:0.9.17  
MAINTAINER alan.gibson@kapsch.net  
  
ENV VERSION 5.2.4  
# Install Python & PIP  
RUN apt-get update; \  
apt-get install -y -qq python-dev; \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download and extract OpsCenter  
RUN \  
mkdir /opt/opscenter; \  
curl http://downloads.datastax.com/community/opscenter-${VERSION}.tar.gz \  
| tar xzf - --strip-components=1 -C "/opt/opscenter";  
  
ADD . /src  
  
# Copy over daemons  
RUN \  
mkdir -p /etc/service/opscenter; \  
cp /src/run /etc/service/opscenter/; \  
ln -s /opt/opscenter/log /var/log/opscenter;  
  
# Expose ports  
EXPOSE 8888  
WORKDIR /opt/opscenter  
  
CMD ["/sbin/my_init"]  

