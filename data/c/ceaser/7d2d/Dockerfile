FROM dstacademy/steamcmd:latest  
MAINTAINER Ceaser Larry <ceaser.larry@gmail.com>  
  
# Set build arguments.  
ARG DEB_PROXY  
ENV DEB_PROXY ${DEB_PROXY}  
ARG SD2D_HOME  
ENV SD2D_HOME ${SD2d_HOME:-"/opt/7d2d"}  
ARG SD2D_BRANCH  
ENV SD2D_BRANCH ${SD2D_BRANCH}  
ARG SD2D_BRANCH_PASSWORD  
ENV SD2D_BRANCH_PASSWORD ${SD2D_BRANCH_PASSWORD}  
  
# Optional APT Proxy  
RUN [ -z "$DEB_PROXY" ] || \  
echo "Acquire::http::Proxy \"$DEB_PROXY\";" > /etc/apt/apt.conf.d/01proxy && \  
echo "Acquire::https::Proxy false;" >> /etc/apt/apt.conf.d/01proxy  
  
# Install dependencies.  
RUN set -x \  
&& dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
lib32stdc++6 \  
libcurl4-gnutls-dev:i386 \  
netcat \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/apt/apt.conf.d/01proxy  
  
# Install 7 Days To Die  
RUN set -x \  
&& mkdir -p $SD2D_HOME \  
&& chown $STEAM_USER:$STEAM_USER $SD2D_HOME \  
&& sync \  
&& gosu $STEAM_USER steamcmd \  
+@ShutdownOnFailedCommand 1 \  
+login anonymous \  
+force_install_dir $SD2D_HOME \  
+app_update 294420 \  
$([ -n "$SD2D_BRANCH" ] && printf %s "-beta $SD2D_BRANCH") \  
$([ -n "$SD2D_BRANCH_PASSWORD" ] && printf %s "-betapassword
$SD2D_BRANCH_PASSWORD") \  
validate \  
+quit \  
&& rm -rf $STEAM_HOME/Steam/logs $STEAM_HOME/Steam/appcache/httpcache \  
&& find $STEAM_HOME/package -type f ! -name "steam_cmd_linux.installed" !
-name "steam_cmd_linux.manifest" -delete  
  
# Copy entrypoint script.  
COPY /docker-entrypoint.sh /  
  
# Set up healthcheck.  
HEALTHCHECK \--interval=5m --timeout=30s --retries=3 CMD nc -z 127.0.0.1 26900  
  
# Expose default server port.  
EXPOSE 26900/tcp  
EXPOSE 26900-26902/udp  
EXPOSE 8080-8082/tcp  
  
# Set up a volume for configuration files and game save.  
RUN mkdir /data  
VOLUME ["/data"]  
  
# Set entrypoint and default command.  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["startserver.sh", "-configfile=/data/serverconfig.xml"]  

