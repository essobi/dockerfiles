FROM debian:jessie  
MAINTAINER Carlos Kazuo  
  
RUN echo "deb http://ftp.de.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y openjdk-8-jre-headless wget  
  
# Supported by mantainer: https://github.com/validator/validator/issues/304  
RUN wget https://sideshowbarker.net/releases/jar/vnu.jar && java -jar vnu.jar
--help  
  
RUN apt-get -y autoclean \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
EXPOSE 8888  
CMD ["java", "-cp", "/vnu.jar", "nu.validator.servlet.Main", "8888"]  

