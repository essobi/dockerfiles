FROM 31z4/storm:0.10.1  
USER root  
WORKDIR /  
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
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ENV JAVA_VERSION 8u92  
ENV JAVA_ALPINE_VERSION 8.92.14-r1  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# Install required packages  
RUN apk add --no-cache \  
bash \  
curl \  
gcc \  
git \  
libxml2 \  
libxml2-dev \  
libxslt-dev \  
libc-dev \  
openssh \  
python \  
python-dev \  
py-pip \  
libc-dev \  
&& pip install --upgrade pip  
  
#Maven  
ARG MAVEN_VERSION=3.3.9  
ARG USER_HOME_DIR="/root"  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& wget
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz -O - \  
| tar -xzC /usr/share/maven \  
&& ln -s /usr/share/maven/apache-maven-$MAVEN_VERSION/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"  
COPY settings.xml /root/.m2/settings.xml  
  
#Sinfonier-backend-api  
RUN git clone https://github.com/telefonicaid/fiware-sinfonier.git && cd
fiware-sinfonier && git checkout $SOURCE_BRANCH  
  
RUN pip install -r /fiware-sinfonier/sinfonier-backend-api/requirements  
  
WORKDIR /fiware-sinfonier/sinfonier-backend-api/  
  
#Launch script  
ENTRYPOINT ["python","sinfonierapi.py", "--docker"]  

