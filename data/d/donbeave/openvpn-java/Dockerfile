FROM debian:sid-slim  
  
MAINTAINER Alexey Zhokhov <alexey@zhokhov.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update apt-get  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
nano \  
ca-certificates \  
curl \  
wget \  
ssh \  
net-tools \  
openvpn \  
software-properties-common \  
procps \  
httpie \  
dnsutils \  
unzip \  
uchardet \  
locales \  
java-common \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
# Install Java.  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u152-b16/aa0333dd3019491ca4f6ddbe78cdb6d0/server-
jre-8u152-linux-x64.tar.gz" \  
&& tar -xzvf server-jre-8u152-linux-x64.tar.gz \  
&& mkdir -p /usr/lib/jvm/ \  
&& mv jdk1.8.0_152 /usr/lib/jvm/java-8-oracle \  
&& update-alternatives --install /usr/bin/java java
/usr/lib/jvm/java-8-oracle/jre/bin/java 100 \  
&& rm -rf jdk1.8.0_152 \  
&& rm server-jre-8u152-linux-x64.tar.gz  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Set LOCALE to UTF8  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& ln -s /etc/locale.alias /usr/share/locale/locale.alias \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure locales \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
COPY docker-entrypoint.sh /  
RUN chmod a+x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/bin/sleep", "300]  

