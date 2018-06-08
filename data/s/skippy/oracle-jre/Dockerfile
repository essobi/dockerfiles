# heavily influenced by
https://registry.hub.docker.com/u/errordeveloper/oracle-jre/  
# just keeping it more up-to-date  
FROM gliderlabs/alpine:3.1  
MAINTAINER Adam Greene <adam.greene@gmail.com>  
  
RUN apk-install curl ca-certificates  
  
ENV JAVA_HOME /usr/jdk1.8.0_40  
ENV JAVA_SHA256
117c7d970b6f74de1ee7b9db20f4f16a7b5d2ec364806d7d375d85dd54b48bc8  
  
RUN curl \  
\--silent \  
\--location \  
\--retry 3 \  
\--cacert /etc/ssl/certs/ca-certificates.crt \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
\--output /tmp/server-jre-8u40-linux-x64.tar.gz \  
"http://download.oracle.com/otn-pub/java/jdk/8u40-b26/server-
jre-8u40-linux-x64.tar.gz" \  
&& echo "${JAVA_SHA256} /tmp/server-jre-8u40-linux-x64.tar.gz" > /tmp/server-
jre-8u40-linux-x64.sha256 \  
&& sha256sum -c /tmp/server-jre-8u40-linux-x64.sha256 \  
&& gunzip -c /tmp/server-jre-8u40-linux-x64.tar.gz \  
| tar x -C /usr/ \  
&& ln -s $JAVA_HOME /usr/java \  
&& rm -rf $JAVA_HOME/man \  
&& rm -rf /tmp/*  
  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
ENTRYPOINT [ "java" ]  
CMD [ "-version" ]  

