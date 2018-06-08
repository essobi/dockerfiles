FROM openjdk:8-jre-alpine  
  
MAINTAINER Irvin Capagcuan <irvin@capagcuan.org>  
  
ENV SONARLINT_HOME=/opt/sonarlint \  
SONARLINT_VERSION=2.1.0.566 \  
PATH=/opt/sonarlint/bin/:$PATH  
  
RUN apk update && apk add wget unzip  
  
RUN mkdir -p ${SONARLINT_HOME} \  
&& wget -O /tmp/sonarlint.zip
https://bintray.com/sonarsource/Distribution/download_file?file_path=sonarlint-
cli%2Fsonarlint-cli-${SONARLINT_VERSION}.zip \  
&& cd /tmp \  
&& unzip sonarlint.zip \  
&& mv /tmp/sonarlint-cli-${SONARLINT_VERSION}/* ${SONARLINT_HOME} \  
&& chmod -R +x ${SONARLINT_HOME} \  
&& rm -rf /tmp/sonarlint.zip  
  
VOLUME /root/.sonarlint  
  
VOLUME /app  
  
WORKDIR /app  
  
ENTRYPOINT ["sonarlint"]  

