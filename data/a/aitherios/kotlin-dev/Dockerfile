FROM openjdk:8-jdk-alpine  
  
ENV KOTLIN_VERSION=1.1.4-2 \  
KOTLIN_HOME=/opt/kotlin \  
GRADLE_VERSION=4.0.1 \  
GRADLE_HOME=/opt/gradle  
  
ARG
GRADLE_DOWNLOAD_SHA256=d717e46200d1359893f891dab047fdab98784143ac76861b53c50dbd03b44fd4  
ARG
KOTLIN_DOWNLOAD_SHA256=9b8957cc8fc5845c4e97beec05e4eaa952a26545022f16c158c4f65e269f5127  
  
RUN apk update && \  
apk add --no-cache bash libstdc++ && \  
apk add --no-cache --virtual .build-deps \  
ca-certificates wget openssl unzip && \  
update-ca-certificates && \  
mkdir /opt && \  
cd /tmp && \  
wget -q --show-progress -O kotlin-compiler.zip
"https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-
compiler-${KOTLIN_VERSION}.zip" && \  
echo "${KOTLIN_DOWNLOAD_SHA256} *kotlin-compiler.zip" | sha256sum -c - && \  
unzip kotlin-compiler.zip && \  
rm kotlin-compiler.zip && \  
mv "kotlinc" "${KOTLIN_HOME}/" && \  
rm -rf ${KOTLIN_HOME}/bin/*.bat ${KOTLIN_HOME}/license
${KOTLIN_HOME}/build.txt && \  
chmod +x ${KOTLIN_HOME}/bin/* && \  
ln -s "${KOTLIN_HOME}/bin/"* "/usr/bin/" && \  
wget -q --show-progress -O gradle.zip
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"
&& \  
echo "${GRADLE_DOWNLOAD_SHA256} *gradle.zip" | sha256sum -c - && \  
unzip gradle.zip && \  
rm gradle.zip && \  
mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" && \  
ln -s "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle && \  
apk del .build-deps  

