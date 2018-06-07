FROM frolvlad/alpine-glibc:alpine-3.4  
# Set environment  
ENV JAVA_HOME /usr/lib/jvm/jre  
ENV PATH $PATH:$JAVA_HOME/bin  
  
RUN apk add --no-cache --virtual=build-dependencies wget ca-certificates \  
&& mkdir /usr/lib/jvm \  
&& cd /usr/lib/jvm \  
&& wget -q --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" http://download.oracle.com/otn-
pub/java/jdk/8u152-b16/aa0333dd3019491ca4f6ddbe78cdb6d0/server-
jre-8u152-linux-x64.tar.gz -O - | gunzip | tar x \  
&& ln -s /usr/lib/jvm/jdk1.8.0_152 /usr/lib/jvm/jre \  
&& apk del build-dependencies \  
&& rm -rf /tmp/*  

