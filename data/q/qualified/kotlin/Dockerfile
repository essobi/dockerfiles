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
wget -q -O gradle.zip
"https://services.gradle.org/distributions/gradle-4.7-bin.zip"; \  
wget -q -O gradle.sha256
"https://services.gradle.org/distributions/gradle-4.7-bin.zip.sha256"; \  
echo "$(cat gradle.sha256 | tr -d '\n') *gradle.zip" | sha256sum -c -; \  
\  
unzip gradle.zip; \  
rm gradle.zip gradle.sha256; \  
mkdir /opt; \  
mv gradle-4.7 /opt/gradle/; \  
wget -q -O kotlinc.zip
"https://github.com/JetBrains/kotlin/releases/download/v1.2.41/kotlin-
compiler-1.2.41.zip"; \  
unzip kotlinc.zip; \  
rm kotlinc.zip; \  
mv kotlinc /opt/kotlinc;  
  
ENV PATH=/opt/kotlinc/bin:/opt/gradle/bin:$PATH  
  
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
RUN mkdir -p /workspace/kotlin/classes  

