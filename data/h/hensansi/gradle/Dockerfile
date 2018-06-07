FROM frolvlad/alpine-oraclejdk8:slim  
  
ENV GRADLE_VERSION=3.3 \  
GRADLE_HOME=/opt/gradle \  
APP_DIR=/app  
  
# Extra files created by gradle  
ENV HOME=${APP_DIR}/.home \  
GRADLE_USER_HOME=${APP_DIR}/.home \  
GRADLE_OPTS="\"-Dorg.gradle.daemon=false\""  
ENV PATH=$PATH:$GRADLE_HOME/bin  
  
# Download and extract gradle to opt folder  
RUN apk --no-cache add curl libstdc++ \  
&& mkdir /opt \  
&& curl -O
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip gradle-${GRADLE_VERSION}-bin.zip -d /opt \  
&& ln -s /opt/gradle-${GRADLE_VERSION} /opt/gradle \  
&& rm -f gradle-${GRADLE_VERSION}-bin.zip  
  
WORKDIR ${APP_DIR}  
CMD ["gradle", "clean", "build"]  

