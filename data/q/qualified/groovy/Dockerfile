FROM openjdk:8-jdk-alpine  
  
RUN set -ex; \  
adduser -D codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
apk add --no-cache \  
bash \  
ca-certificates \  
openssl \  
unzip \  
; \  
mkdir /opt; \  
\  
wget -q -O gradle.zip
"https://services.gradle.org/distributions/gradle-4.7-bin.zip"; \  
wget -q -O gradle.sha256
"https://services.gradle.org/distributions/gradle-4.7-bin.zip.sha256"; \  
echo "$(cat gradle.sha256 | tr -d '\n') *gradle.zip" | sha256sum -c -; \  
unzip gradle.zip; \  
rm gradle.zip gradle.sha256; \  
mv gradle-4.7 /opt/gradle; \  
\  
wget -q -O groovy.zip "https://dl.bintray.com/groovy/maven/apache-groovy-
binary-2.4.15.zip"; \  
wget -q -O groovy.sha256 "https://dl.bintray.com/groovy/maven/apache-groovy-
binary-2.4.15.zip.sha256"; \  
echo "$(cat groovy.sha256 | tr -d '\n') *groovy.zip" | sha256sum -c -; \  
unzip groovy.zip; \  
rm groovy.zip groovy.sha256; \  
mv groovy-2.4.15 /opt/groovy;  
  
ENV PATH=/opt/groovy/bin:/opt/gradle/bin:$PATH  
  
COPY rootfs/runner /runner  
RUN set -ex; \  
cd /runner/io.qualified.junit5; \  
gradle -q build --no-daemon; \  
gradle -q dependencies --no-daemon; \  
gradle -q copyJars --no-daemon; \  
mkdir -p /opt/jars; \  
mv build/jars/*.jar /opt/jars; \  
mv build/libs/*.jar /opt/jars; \  
gradle -q printJarsJson --no-daemon;  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  
  
# Make a directory to store compiled classes.  
RUN mkdir -p /workspace/groovy/classes  

