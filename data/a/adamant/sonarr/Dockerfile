FROM debian:stretch-slim  
LABEL mainatiner="Adam Dodman <adam.dodman@gmx.com>"  
  
ENV SUID=906 SGID=900  
ARG SONARR_TAG  
ARG SONARR_BRANCH=master  
  
ARG TINI_VERSION=v0.16.1  
ARG SU_EXEC_VER=v0.3  
RUN apt-get update \  
&& apt-get install -y libmono-cil-dev mediainfo xmlstarlet curl jq \  
\  
&& curl -Lo /sbin/su-exec https://github.com/frebib/su-
exec/releases/download/${SU_EXEC_VER}/su-exec-$(uname -m) \  
&& curl -Lo /sbin/tini
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini \  
&& chmod 755 /sbin/su-exec /sbin/tini \  
&& if [ -z "$SONARR_TAG" ]; then \  
export SONARR_TAG="$(curl -fL
"http://services.sonarr.tv/v1/update/${SONARR_BRANCH}?os=linux" | jq -r
'.updatePackage.version')"; \  
fi \  
&& mkdir -p /sonarr \  
&& echo "Building Sonarr $SONARR_TAG" \  
&& curl -fL
"http://download.sonarr.tv/v2/master/mono/NzbDrone.${SONARR_BRANCH}.${SONARR_TAG}.mono.tar.gz"
\  
| tar xz -C /sonarr --strip-components=1 \  
&& find /sonarr -type f -exec chmod 644 {} + \  
&& find /sonarr -type d -o -name '*.exe' -exec chmod 755 {} + \  
\  
&& apt-get remove -y curl jq openssl \  
&& apt-get autoremove -y  
  
VOLUME ["/config", "/media"]  
ENV XDG_CONFIG_HOME=/config  
  
EXPOSE 8989  
COPY *.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/*.sh  
  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/entrypoint.sh"]  
CMD ["mono", "/sonarr/NzbDrone.exe", "--no-browser", "--data=/config"]  

