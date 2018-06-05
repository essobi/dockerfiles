# AlpineLinux with a glibc-2.23-r1, Oracle Java jre8 and unlimited JCE policy
patch  
FROM anapsix/alpine-java:jre8  
  
MAINTAINER David Castellanos <davidcaste@gmail.com>  
  
# do all in one step  
RUN apk upgrade --update && \  
apk add --update curl unzip && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/unlimited_jce_policy.zip "http://download.oracle.com/otn-
pub/java/jce/8/jce_policy-8.zip" && \  
unzip -jo -d ${JAVA_HOME}/jre/lib/security /tmp/unlimited_jce_policy.zip && \  
apk del curl unzip && \  
rm -rf /tmp/* /var/cache/apk/*  

