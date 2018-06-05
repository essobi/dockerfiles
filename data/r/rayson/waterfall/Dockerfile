FROM openjdk:8-jre-alpine  
LABEL maintainer Yuxiang Zhu <vfreex@gmail.com>  
  
  
ARG WATERFALL_BUILD=124  
ARG WATERFALL_MODULES='cmd_alert cmd_find cmd_list cmd_send cmd_server
reconnect_yaml'  
  
LABEL \  
name=waterfall \  
build="$WATERFALL_BUILD" \  
maintainer='Yuxiang Zhu <vfreex@gmail.com>'  
  
ENV WATERFALL_WORKSPACE=/var/local/waterfall \  
WATERFALL_ROOT=/opt/waterfall \  
WATERFALL_USER=waterfall \  
WATERFALL_GROUP=waterfall \  
WATERFALL_BUILD="$WATERFALL_BUILD" \  
JAVA_OPTS='-Xms1G -Xmx2G'  
RUN \  
apk update \  
&& apk add \--virtual build-deps wget ca-certificates \  
# install Waterfall  
&& mkdir -p "$WATERFALL_ROOT" \  
&& wget -O "$WATERFALL_ROOT"/Waterfall.jar
"https://ci.destroystokyo.com/job/Waterfall/$WATERFALL_BUILD/artifact/Waterfall-
Proxy/bootstrap/target/Waterfall.jar" \  
# install Waterfall modules  
&& mkdir -p "$WATERFALL_ROOT"/modules \  
&& for module in $WATERFALL_MODULES; do \  
wget -O "$WATERFALL_ROOT"/modules/"$module".jar
"https://ci.destroystokyo.com/job/Waterfall/$WATERFALL_BUILD/artifact/Waterfall-
Proxy/module/${module/_/-}/target/$module.jar"; \  
done \  
# additional packages  
&& apk --no-cache add gettext \  
# create user and workspace  
&& addgroup -S "$WATERFALL_GROUP" \  
&& adduser -G "$WATERFALL_GROUP" -S "$WATERFALL_USER" \  
&& mkdir -p "$WATERFALL_WORKSPACE" \  
&& chown -R "$WATERFALL_USER":"$WATERFALL_GROUP" "$WATERFALL_WORKSPACE" \  
# install utils  
&& apk add su-exec tini \  
# clean up  
&& apk del build-deps \  
&& rm -rf /var/lib/apk/  
  
COPY files/ /  
  
WORKDIR "$WATERFALL_WORKSPACE"  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/sbin/entrypoint.sh"]  
CMD ["/usr/local/bin/waterfall"]  
VOLUME "$WATERFALL_WORKSPACE"  

