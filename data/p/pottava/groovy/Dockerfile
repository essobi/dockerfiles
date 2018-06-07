# Groovy v2.4  
# docker run --rm pottava/groovy:2.4 groovy -e "println GroovySystem.version"  
  
FROM pottava/java:8-jdk  
  
ENV GROOVY_VERSION=2.4.7  
ENV GROOVY_HOME=/usr/lib/groovy-${GROOVY_VERSION}-SNAPSHOT  
ENV PATH=${PATH}:${GROOVY_HOME}/bin  
  
RUN set -ex \  
&& apk \--no-cache add --virtual build-dependencies curl unzip \  
&& apk \--no-cache add bash \  
&& cd /usr/lib \  
&& curl -O --location --silent --show-error https://oss.jfrog.org/oss-
snapshot-local/org/codehaus/groovy/groovy/${GROOVY_VERSION}-SNAPSHOT/apache-
groovy-binary-${GROOVY_VERSION}-SNAPSHOT.zip \  
&& curl -O --location --silent --show-error https://oss.jfrog.org/oss-
snapshot-local/org/codehaus/groovy/groovy/${GROOVY_VERSION}-SNAPSHOT/apache-
groovy-binary-${GROOVY_VERSION}-SNAPSHOT.zip.sha1 \  
&& echo $(cat apache-groovy-binary-${GROOVY_VERSION}-SNAPSHOT.zip.sha1)'
apache-groovy-binary-'${GROOVY_VERSION}'-SNAPSHOT.zip' | sha1sum -c - \  
&& unzip -q apache-groovy-binary-${GROOVY_VERSION}-SNAPSHOT.zip \  
&& rm -rf apache-groovy-binary-${GROOVY_VERSION}-SNAPSHOT.zip \  
apache-groovy-binary-${GROOVY_VERSION}-SNAPSHOT.* \  
groovy-${GROOVY_VERSION}-SNAPSHOT/bin/*.bat \  
&& rm /bin/sh && ln -s /bin/bash /bin/sh \  
&& apk del --purge build-dependencies  
  
WORKDIR /app  

