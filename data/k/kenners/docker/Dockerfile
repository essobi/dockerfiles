FROM alpine:3.2  
MAINTAINER kenners <knutenners+git@gmail.com>  
  
LABEL arch=x86_64 \  
java.version="7.91.2.6.3-r1" \  
java.vendor=OpenJDK \  
java.jvm=JRE \  
os=alpine  
  
RUN set -ex \  
&& packages='openjdk7-jre-base' \  
&& apk add --update ${packages} \  
\  
&& rm -rf /var/cache/apk/*  
  
CMD ["/usr/bin/java", "-version"]  
  

