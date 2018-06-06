#  
# This is a multi-stage build.  
# Actual build is at the very end.  
#  
FROM library/ubuntu:xenial AS build  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
RUN apt-get update && \  
apt-get install -y \  
python-software-properties \  
software-properties-common \  
apt-utils  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
D68FA50FEA312927 && \  
echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-
org/3.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
apt-get update  
  
RUN mkdir -p /build/image  
WORKDIR /build  
RUN apt-get download \  
mongodb-org \  
mongodb-org-mongos \  
mongodb-org-server \  
mongodb-org-shell \  
mongodb-org-tools \  
libssl1.0.0  
RUN for file in *.deb; do dpkg-deb -x ${file} image/; done  
  
WORKDIR /build/image  
RUN mkdir -p \  
var/log/mongodb && \  
ln -s /dev/stdout var/log/mongodb/mongod.log && \  
rm -rf \  
lib/systemd \  
usr/sbin \  
usr/share && \  
sed -i -r \  
's,^ bindIp:.*, bindIp: 0.0.0.0,g' \  
etc/mongod.conf  
  
FROM clover/base  
  
ENV LC_ALL C  
WORKDIR /  
COPY \--from=build /build/image /  
  
VOLUME ["/var/lib/mongodb"]  
  
CMD ["mongod", "-f", "/etc/mongod.conf"]  
  
EXPOSE 27017  

