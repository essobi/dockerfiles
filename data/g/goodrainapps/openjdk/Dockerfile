FROM openjdk:8u131-jdk-alpine  
MAINTAINER zhouyq@goodrain.com  
  
# china repositories mirror  
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g'
/etc/apk/repositories  
  
# modify timezone and install the necessary software  
RUN apk add --no-cache tzdata libc6-compat libstdc++ tar sed wget curl bash
su-exec netcat-openbsd && \  
sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd && \  
ln -s /lib /lib64 && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone && \  
date && apk del --no-cache tzdata && \  
sed -i -r 's#^(securerandom.source)=.*#\1=file:/dev/./urandom/#'
$JAVA_HOME/jre/lib/security/java.security  
  
# add pinpoint apm agent  
ENV PINPOINT_AGETN_VERSION="1.7.2"  
ENV PINPOINT_AGENT_PATH="/usr/local/pinpoint-agent"  
RUN mkdir -pv $PINPOINT_AGENT_PATH \  
&& curl -ks https://pkg.goodrain.com/apps/pinpoint/pinpoint-
agent-${PINPOINT_AGETN_VERSION}-SNAPSHOT.tar.gz | tar xz -C
/usr/local/pinpoint-agent  
  
# add setmem.sh  
RUN mkdir -pv /opt/goodrain/java/  
COPY setmem.sh /opt/goodrain/java/setmem.sh  
  
ENV LANG en_US.utf8  

