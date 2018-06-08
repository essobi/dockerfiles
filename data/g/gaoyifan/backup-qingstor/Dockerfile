FROM ustclug/centos:7  
MAINTAINER Yifan Gao "git@gaoyifan.com"  
ENV CACHE_DIR="/etc/docker-backup"  
ENV TEMPLATES_DIR="${CACHE_DIR}/templates" \  
ATTRIBUTE_FIX_LIST="${CACHE_DIR}/attribute_fix_list" \  
DEFAULT_ENV="${CACHE_DIR}/default_env" \  
BUILD_SCRIPT="${CACHE_DIR}/build.sh"  
COPY assets $CACHE_DIR  
  
COPY entrypoint/entrypoint.sh /sbin/entrypoint.sh  
  
RUN /sbin/entrypoint.sh build  
  
VOLUME /tmp/backup  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
  
CMD ["/usr/local/bin/backup.sh"]  

