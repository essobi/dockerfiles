FROM centos:7  
LABEL maintainer="hermitmaster <hermitmaster@icloud.com>"  
  
ENV JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=144 \  
JAVA_VERSION_BUILD=01 \  
JAVA_URL_HASH=090f390dda5b47b9b721c7dfaa008135 \  
DOCKERIZE_VERSION=v0.5.0  
RUN yum update -y \  
&& yum install -y wget \  
&& wget -q
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& wget -q --no-cookies --no-check-certificate \  
\--header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_URL_HASH}/jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.rpm"
\  
&& yum localinstall -y
jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.rpm \  
&& rm -f jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.rpm \  
&& yum remove -y wget \  
&& yum clean all  
  
ENTRYPOINT ["dockerize", "--help"]

