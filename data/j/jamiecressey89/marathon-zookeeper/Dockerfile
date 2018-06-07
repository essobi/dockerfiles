FROM openjdk:8-jre-alpine  
  
ARG DISTRO_NAME=zookeeper-3.5.2-alpha  
  
ENV ZOO_USER=zookeeper \  
ZOO_CONF_DIR=/conf \  
ZOO_DATA_DIR=/data \  
ZOO_DATA_LOG_DIR=/datalog \  
ZOO_TICK_TIME=2000 \  
ZOO_INIT_LIMIT=5 \  
ZOO_SYNC_LIMIT=2  
  
COPY docker-entrypoint.sh /  
COPY manage_members.py /  
  
# Install required packages  
RUN apk add \--no-cache \  
bash \  
su-exec \  
python \  
py-pip \  
&& set -x \  
&& adduser -D "$ZOO_USER" \  
&& mkdir -p "$ZOO_DATA_LOG_DIR" "$ZOO_DATA_DIR" "$ZOO_CONF_DIR" \  
&& chown "$ZOO_USER:$ZOO_USER" "$ZOO_DATA_LOG_DIR" "$ZOO_DATA_DIR"
"$ZOO_CONF_DIR" \  
&& apk add \--no-cache --virtual .build-deps \  
gnupg \  
&& wget
"http://www.apache.org/dist/zookeeper/$DISTRO_NAME/$DISTRO_NAME.tar.gz" \  
&& wget -q
"http://www.apache.org/dist/zookeeper/$DISTRO_NAME/$DISTRO_NAME.tar.gz.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& tar -xzf "$DISTRO_NAME.tar.gz" \  
&& mv "$DISTRO_NAME/conf/"* "$ZOO_CONF_DIR" \  
&& rm -r "$GNUPGHOME" "$DISTRO_NAME.tar.gz" "$DISTRO_NAME.tar.gz.asc" \  
&& apk del .build-deps \  
&& pip install requests -U \  
&& ln -s /manage_members.py /etc/periodic/15min/  
  
WORKDIR $DISTRO_NAME  
  
VOLUME ["$ZOO_DATA_DIR", "$ZOO_DATA_LOG_DIR"]  
  
ENV PATH=$PATH:/$DISTRO_NAME/bin \  
ZOOCFGDIR=$ZOO_CONF_DIR  
  
EXPOSE 2181 2888 3888 8080  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["zkServer.sh", "start-foreground"]  

