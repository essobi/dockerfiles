FROM java:openjdk-8-jdk-alpine  
MAINTAINER yongseoklee <yongseokleecom@gmail.com>  
  
RUN apk --update add --no-cache wget zip unzip bash tzdata && rm -rf
/var/cache/apk/*  
  
# Build Arugments  
ARG YONA_VERSION=1.9.1  
# Yona download & install  
RUN \  
mkdir -p /opt \  
&& wget -O /opt/yona.zip https://github.com/yona-
projects/yona/releases/download/v${YONA_VERSION}/yona-v${YONA_VERSION}-h2.bin.zip
\  
&& unzip /opt/yona.zip -d /opt \  
&& rm /opt/yona.zip \  
&& mv /opt/yona-${YONA_VERSION} /opt/yona  
  
# Add entrypoint  
ADD entrypoint.sh /opt/yona/bin/entrypoint.sh  
RUN chmod +x /opt/yona/bin/entrypoint.sh  
  
# Yona data  
VOLUME /yona  
  
# Enviroment Variables  
ENV JAVA_OPTS "-Xms1024m -Xmx1024m"  
ENV TZ "Asia/Seoul"  
# Yona HTTP port  
EXPOSE 9000  
ENTRYPOINT ["/opt/yona/bin/entrypoint.sh"]

