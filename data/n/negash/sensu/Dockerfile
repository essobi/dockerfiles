FROM ruby:alpine  
MAINTAINER Negash <i@negash.ru>  
  
RUN apk add --update build-base curl bash && rm -rf /var/cache/apk/*  
# install sensu-core  
RUN gem install sensu  
  
COPY bin /bin/  
RUN chmod +x /bin/install  
RUN chmod +x /bin/start  
  
ENV DEFAULT_PLUGINS_REPO=sensu-plugins \  
DEFAULT_PLUGINS_VERSION=master \  
  
#Common Config  
RUNTIME_INSTALL='' \  
LOG_LEVEL=warn \  
CONFIG_DIR=/etc/sensu/conf.d \  
CHECK_DIR=/etc/sensu/check.d \  
EXTENSION_DIR=/etc/sensu/extensions \  
HANDLERS_DIR=/etc/sensu/handlers\  
  
#Config for gathering host metrics  
HOST_DEV_DIR=/dev \  
HOST_PROC_DIR=/proc \  
HOST_SYS_DIR=/sys  
  
EXPOSE 4567  
VOLUME ["/etc/sensu"]  
  
ENTRYPOINT ["/bin/start"]

