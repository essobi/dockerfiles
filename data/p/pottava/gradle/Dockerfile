# Gradle v3.0  
# docker run \--rm pottava/gradle:3 gradle -version  
# docker run \--rm -v /path/to/app:/app pottava/gradle:3 gradle build  
# docker run \--rm -v /path/to/app:/app pottava/gradle:3 sh -c "gradle build
&& gradle clean"  
  
FROM pottava/java:8-jdk  
  
ENV GRADLE_VERSION=3.0  
  
RUN set -ex \  
&& apk --no-cache add --virtual build-dependencies curl unzip \  
&& apk --no-cache add bash libstdc++ \  
&& cd /usr/lib \  
&& curl -O --location --silent --show-error
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip -q gradle-${GRADLE_VERSION}-bin.zip \  
&& ln -s /usr/lib/gradle-${GRADLE_VERSION}/bin/gradle /usr/bin/ \  
&& rm -rf gradle-${GRADLE_VERSION}-bin.zip \  
gradle-${GRADLE_VERSION}/bin/gradle.bat \  
gradle-${GRADLE_VERSION}/getting-started.html \  
gradle-${GRADLE_VERSION}/media \  
/opt/jdk/*src.zip \  
&& apk del --purge build-dependencies  
  
VOLUME /app /root/.gradle/caches  
WORKDIR /app  

