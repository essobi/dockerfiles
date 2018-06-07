FROM alpine:3.3  
MAINTAINER steve@mostlyharmful.net  
  
# Our versions (JDK is further down)  
ENV GAUGE_VERSION="0.4.0" \  
MAVEN_VERSION="3.3.9" \  
M2_HOME=/usr/lib/mvn  
  
# Perform baseline OS updates, including certificates  
RUN apk update && \  
apk add \  
ca-certificates && \  
rm -rf /var/cache/apk/*  
  
# Bash for container diagnostics  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
  
# Install Maven  
RUN apk add --update tar && \  
apk add --update wget && \  
apk add --update curl  
  
# Install Maven  
RUN cd /tmp && \  
wget
"http://apache.mirror.digitalpacific.com.au/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" && \  
tar -zxvf "apache-maven-$MAVEN_VERSION-bin.tar.gz" && \  
mv "apache-maven-$MAVEN_VERSION" "$M2_HOME" && \  
ln -s "$M2_HOME/bin/mvn" /usr/bin/mvn  
  
# Plugin Dependencies  
RUN apk --update add openjdk8 && \  
ln -s /usr/lib/jvm/java-1.8-openjdk/bin/javac /usr/local/bin/javac  
  
# Install Gauge  
RUN cd /tmp && \  
wget
"https://github.com/getgauge/gauge/releases/download/v$GAUGE_VERSION/gauge-$GAUGE_VERSION-
linux.x86_64.zip" && \  
mkdir /gauge/ && \  
cd /tmp && \  
unzip gauge-0.4.0-linux.x86_64.zip -d /gauge && \  
cd /gauge && \  
./install.sh && \  
gauge --install java  

