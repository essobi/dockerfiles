# Oracle Java on Ubuntu  
  
FROM winggundamth/ubuntu-base:xenial  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=xenial-20160809  
  
# 1) Install Java and some necessary packages  
# 2) Clean to reduce Docker Image size  
ARG APT_CACHER_NG  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
apt-get update && \  
apt-get install -y wget && \  
wget \--no-check-certificate -c \--header \  
"Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/8u101-b13/jdk-8u101-linux-x64.tar.gz && \  
mkdir -p /var/cache/oracle-jdk8-installer && \  
mv jdk-8*-linux-x64.tar.gz /var/cache/oracle-jdk8-installer && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu \  
$(lsb_release -cs) main" \  
> /etc/apt/sources.list.d/webupd8team-java-$(lsb_release -cs).list && \  
apt-key adv \--keyserver keyserver.ubuntu.com \--recv-keys EEA14886 && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true \  
| debconf-set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true \  
| debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy \  
/var/cache/oracle-jdk8-installer  

