FROM debian:stretch-slim  
LABEL maintainer="Adam Dodman <adam.dodman@gmx.com>"  
  
ENV UID=901 GID=900  
ARG RADARR_TAG  
ARG RADARR_BRANCH=develop  
ARG TINI_VERSION=v0.16.1  
ARG SU_EXEC_VER=v0.2  
RUN apt-get update \  
&& apt-get install -y libmono-cil-dev mediainfo xmlstarlet curl jq \  
\  
&& if [ -z "$RADARR_TAG" ]; then \  
export RADARR_TAG="$(curl -fL
"http://radarr.aeonlucid.com/v1/update/${RADARR_BRANCH}?os=linux&version=0.0"
| jq -r '.updatePackage.version')"; \  
fi \  
&& mkdir -p /radarr \  
&& echo "Building Radarr $RADARR_TAG" \  
&& curl -fL
"https://github.com/Radarr/Radarr/releases/download/v${RADARR_TAG}/Radarr.${RADARR_BRANCH}.${RADARR_TAG}.linux.tar.gz"
\  
| tar xz -C /radarr --strip-components=1 \  
&& find /radarr -type f -exec chmod 644 {} + \  
&& find /radarr -type d -o -name '*.exe' -exec chmod 755 {} + \  
\  
&& apt-get remove -y curl jq openssl \  
&& apt-get autoremove -y  
  
VOLUME ["/config", "/media"]  
ENV XDG_CONFIG_HOME=/config  
  
EXPOSE 7878  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/sbin/tini  
ADD https://github.com/javabean/su-exec/releases/download/v0.2/su-exec.amd64
/sbin/su-exec  
COPY *.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/*.sh /sbin/tini /sbin/su-exec  
  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/entrypoint.sh"]  
CMD ["mono", "/radarr/Radarr.exe", "--no-browser", "--data=/config"]  

