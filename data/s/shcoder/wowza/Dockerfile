FROM shcoder/alpine:glibc.supervisor  
  
MAINTAINER shcoder.alex@gmail.com  
  
ENV WOWZA_VERSION=4.5.0 \  
WOWZA_USER_NAME=admin \  
WOWZA_USER_PASSWORD=admin \  
WOWZA_PUBLISH_USER_NAME=admin \  
WOWZA_PUBLISH_USER_PASSWORD=admin \  
WOWZA_LICENSE=ET2A4-ntGJH-vjEM3-YbQY4-d6T9V-BVvVF-7mZxjdWappYK  
  
ADD prepare.sh /tmp/  
ADD bin/wowza/start.sh /opt/wowza/  
ADD entrypoint.sh /sbin/  
  
RUN chmod 755 /sbin/entrypoint.sh \  
/opt/wowza/start.sh && \  
/tmp/prepare.sh  
  
WORKDIR /usr/local/WowzaStreamingEngine  
  
EXPOSE 1935/tcp 8086/tcp 8087/tcp 8088/tcp  
  
CMD ["/sbin/entrypoint.sh"]

