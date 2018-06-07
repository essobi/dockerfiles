FROM debian:jessie  
  
MAINTAINER "Mikhail Stolyarov" <schnack.desu@gmail.com>  
  
#ARG port=8080  
ENV APP_VERSION=3.0 \  
APP_BUILD=4237 \  
APP_USER=upsource \  
APP_STATIC_DIR=/opt/upsource \  
APP_DYNAMIC_DIR=/var/opt/upsource \  
APP_LISTEN_PORT=${port:-8080}  
  
LABEL description="Upsource. Code Review and Repository Browsing. Browse your
source code repositories, share, discuss and review code that you and your
team create. Git, Mercurial, Subversion and Perforce are all supported." \  
version=$APP_VERSION \  
build=$APP_BUILD \  
url="https://www.jetbrains.com/upsource/"  
  
RUN apt-get update \  
&& apt-get install -y unzip \  
&& apt-get install -y wget \  
&& wget -q -P /tmp
https://download.jetbrains.com/upsource/upsource-${APP_VERSION}.${APP_BUILD}.zip
\  
&& mkdir -p $APP_STATIC_DIR \  
&& mkdir -p $APP_DYNAMIC_DIR \  
&& useradd -m -d $APP_DYNAMIC_DIR -s /usr/sbin/nologin -c "JetBrains" -U
$APP_USER \  
&& unzip /tmp/upsource-${APP_VERSION}.${APP_BUILD}.zip -d $APP_STATIC_DIR \  
&& mv ${APP_STATIC_DIR}/Upsource/* $APP_STATIC_DIR \  
&& apt-get purge -y unzip \  
&& apt-get purge -y wget \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf ${APP_STATIC_DIR}/Upsource /tmp/* /var/lib/apt/lists/* /var/tmp/* \  
&& ${APP_STATIC_DIR}/bin/upsource.sh configure \  
\--backups-dir=${APP_DYNAMIC_DIR}/backups \  
\--temp-dir=${APP_DYNAMIC_DIR}/temp \  
\--data-dir=${APP_DYNAMIC_DIR}/data \  
\--logs-dir=${APP_DYNAMIC_DIR}/logs \  
\--listen-port=$APP_LISTEN_PORT \  
&& chown -R ${APP_USER}:${APP_USER} $APP_STATIC_DIR \  
&& chown -R ${APP_USER}:${APP_USER} $APP_DYNAMIC_DIR  
  
USER $APP_USER  
  
WORKDIR $APP_STATIC_DIR  
  
EXPOSE $APP_LISTEN_PORT  
  
VOLUME ["$APP_DYNAMIC_DIR","$APP_STATIC_DIR/conf"]  
  
ENTRYPOINT ["bin/upsource.sh"]  
  
CMD ["run"]  

