FROM java:8-alpine  
  
MAINTAINER Luciano Mores <leslau@gmail.com>  
  
ENV GROOVY_VERSION 2.4.7  
RUN apk upgrade --update && \  
apk add --no-cache --virtual=build-dependencies curl ca-certificates wget
unzip && \  
wget -q -O /tmp/groovy.zip
"https://bintray.com/artifact/download/groovy/maven/apache-groovy-
binary-${GROOVY_VERSION}.zip" && \  
unzip -o -d "/tmp" "/tmp/groovy.zip" && \  
mv "/tmp/groovy-${GROOVY_VERSION}" "/usr/share/groovy" && \  
apk del build-dependencies && \  
rm -rf /tmp/* /var/cache/apk/*  
  
#Add fixed startGroovy to work with busybox  
ADD startGroovy /usr/share/groovy/bin/  
  
ENV GROOVY_HOME "/usr/share/groovy"  
ENV PATH "$PATH:/usr/share/groovy/bin"  
ENTRYPOINT [ "groovy" ]  
CMD [ "-v" ]  

