# Azul images do no follow Docker best practices.  
# We can save significant space building ourselves.  
# Also we need to enable the unlimited crypto policy.  
# FROM azul/zulu-openjdk:8  
#  
# Build the ZuluJDK image  
#  
  
FROM ubuntu:16.04 AS zulu-build  
  
RUN apt-get -qq update && \  
apt-get -qqy install locales && \  
locale-gen en_US.UTF-8 && \  
rm -rf /var/lib/apt/lists/*  
  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8  
# Pull Zulu JDK binaries from official repository  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
0x219BD9C9 && \  
echo "deb http://repos.azulsystems.com/ubuntu stable main" >>
/etc/apt/sources.list.d/zulu.list && \  
apt-get -qq update && \  
apt-get -qqy install zulu-8 && \  
rm -rf /var/lib/apt/lists/* && \  
sed -i "s|#crypto.policy=unlimited|crypto.policy=unlimited|g" \  
/usr/lib/jvm/zulu-8-amd64/jre/lib/security/java.security  

