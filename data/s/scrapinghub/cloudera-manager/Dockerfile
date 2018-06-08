FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
WORKDIR /app  
ENTRYPOINT ["/app/entry"]  
  
# Accept oracle license in debconf  
ADD java7.debconf /tmp/java7.debconf  
# Add webupdate8 apt repo  
ADD java7.list /etc/apt/sources.list.d/java7.list  
# Add webupdate8 signing key  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
7B2C3B0889BF5709A105D03AC2518248EEA14886  
  
RUN cat /tmp/java7.debconf |debconf-set-selections  
  
ENV CM_VERSION=5.5.3-1.cm553.p0.1~trusty-cm5  
  
# Install Oracle Java7  
RUN apt-get update -qq \  
&& apt-get install -qy oracle-java7-installer curl libmysql-java \  
&& rm -f /var/cache/oracle-jdk7-installer/jdk*tar.gz \  
&& ln -sf java-7-oracle /usr/lib/jvm/default-java \  
&& apt-get purge -y openjdk-\\* icedtea-\\* icedtea6-\\* \  
&& cd /tmp/ \  
&& wget -q
http://archive.cloudera.com/cm5/ubuntu/trusty/amd64/cm/pool/contrib/e/enterprise/cloudera-
manager-server_${CM_VERSION}_all.deb \  
&& wget -q
http://archive.cloudera.com/cm5/ubuntu/trusty/amd64/cm/pool/contrib/e/enterprise/cloudera-
manager-daemons_${CM_VERSION}_all.deb \  
&& dpkg -i /tmp/*.deb \  
&& rm -rf /var/lib/apt/lists /tmp/*.deb  
  
COPY . /app  

