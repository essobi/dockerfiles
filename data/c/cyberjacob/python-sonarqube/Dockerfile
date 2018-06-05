FROM openjdk:8-jdk  
  
# A few problems with compiling Java from source:  
# 1. Oracle. Licensing prevents us from redistributing the official JDK.  
# 2. Compiling OpenJDK also requires the JDK to be installed, and it gets  
# really hairy.  
  
RUN echo 'deb http://deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
unzip \  
xz-utils \  
unzip \  
build-essential \  
python-setuptools \  
debhelper \  
&& apt-get -t jessie-backports install -y --no-install-recommends \  
dh-virtualenv \  
&& rm -rf /var/lib/apt/lists/*  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20140324  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
openjdk-8-jdk \  
ca-certificates-java \  
pylint \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN \  
wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-2.8.zip \  
&& unzip sonar-scanner-2.8.zip \  
&& mv sonar-scanner-2.8 /opt/sonar-scanner-2.8 \  
&& chmod +x /opt/sonar-scanner-2.8/bin/sonar-scanner  

