FROM debian:jessie  
MAINTAINER Albert Murillo <albertmurilloaguirre@gmail.com>  
  
# Install git, download and extract Bitbucket Server and create the required
directory layout.  
# Try to limit the number of RUN instructions to minimise the number of layers
that will need to be created.  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends libtcnative-1 ca-certificates
wget curl unzip \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# Link libraries to a place where any tomcat installation will find it  
RUN ln -s /usr/lib/x86_64-linux-gnu/libtcnative-1.* /usr/lib/  
  
ENV JAVA_HOME /opt/java  
ENV JAVA_URL http://download.oracle.com/otn-
pub/java/jdk/8u71-b15/jdk-8u71-linux-x64.tar.gz  
RUN mkdir -p ${JAVA_HOME} \  
&& curl -L --insecure --silent -H "Cookie: oraclelicense=accept-securebackup-
cookie" ${JAVA_URL} | tar -xz --strip=1 -C "$JAVA_HOME"  
  
ENV PATH $PATH:$JAVA_HOME/bin  

