FROM adorsys/alpine-base:3.5  
MAINTAINER https://github.com/adorsys/dockerhub-openjdk-build-base  
  
ENV M2_HOME /usr/local/apache-maven/apache-maven-3.3.9  
ENV M2_URL http://artfiles.org/apache.org/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz  
ENV JAVA_HOME /usr/lib/jvm/default-jvm  
# limit java processes to 128M heap by default  
ENV JAVA_TOOL_OPTIONS -Xmx128M  
  
RUN mkdir $HOME/.m2 && \  
apk -q --no-cache add git make openjdk8 && \  
mkdir /usr/local/apache-maven && \  
wget $M2_URL -q -O - | tar -xz -C /usr/local/apache-maven/ && \  
ln -s $M2_HOME/bin/mvn /usr/local/bin/mvn && \  
ln -sf $JAVA_HOME/bin/* /usr/bin/  

