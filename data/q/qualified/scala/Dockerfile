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
wget -q -O scala.tgz
"https://downloads.lightbend.com/scala/2.12.3/scala-2.12.3.tgz"; \  
mkdir -p /opt/scala; \  
tar zxf scala.tgz -C /opt/scala --strip-components=1; \  
rm scala.tgz;  
  
ENV PATH=/opt/scala/bin:/opt/gradle/bin:$PATH  
  
COPY rootfs/runner /runner  
RUN set -ex; \  
cd /runner/io.qualified.junit5; \  
gradle -q build --no-daemon; \  
gradle -q dependencies --no-daemon; \  
gradle -q copyJars --no-daemon; \  
mkdir -p /opt/jars; \  
mv build/jars/*.jar /opt/jars; \  
mv build/libs/*.jar /opt/jars; \  
gradle -q printJarsJson --no-daemon; \  
cd /runner; \  
scalac -cp /opt/jars/scalatest-app_2.12-3.0.4.jar CodewarsReporter.scala;  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  
WORKDIR /workspace  
  
# Make a directory to store compiled classes.  
RUN mkdir -p /workspace/scala/classes  

