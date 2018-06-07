FROM alpine:3.7  
ENV LANG C.UTF-8  
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk/jre" \  
PATH="$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin"
\  
JAVA_VERSION="8u151" \  
JAVA_ALPINE_VERSION="8.151.12-r0"  
ADD
https://github.com/gitbucket/gitbucket/releases/download/4.19.0/gitbucket.war
/opt/gitbucket.war  
  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home \  
&& set -x \  
&& apk add --no-cache openjdk8-jre="$JAVA_ALPINE_VERSION" \  
&& ln -s /gitbucket /root/.gitbucket  
  
VOLUME /gitbucket  
  
# Port for web page  
EXPOSE 8080  
# Port for SSH access to git repository (Optional)  
EXPOSE 29418  
CMD ["java", "-jar", "/opt/gitbucket.war"]  
  

