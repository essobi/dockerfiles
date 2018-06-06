FROM centos:7  
MAINTAINER Jonathan Meyer <jon@gisjedi.com>  
  
ENV GOSU_VERSION="1.7"  
ENV
GOSU_DOWNLOAD_ROOT="https://github.com/tianon/gosu/releases/download/$GOSU_VERSION"  
ENV GOSU_DOWNLOAD_KEY="0x036A9C25BF357DD4"  
ENV GOSU_ENTRYPOINT_VERSION="1.0.0"  
ENV GOSU_ENTRYPOINT_DOWNLOAD="https://github.com/gisjedi/gosu-
entrypoint/releases/download/$GOSU_ENTRYPOINT_VERSION/gosu-entrypoint.sh"  
RUN set -x \  
&& gpg-agent --daemon \  
&& gpg --keyserver pgp.mit.edu --recv-keys $GOSU_DOWNLOAD_KEY \  
&& echo "trusted-key $GOSU_DOWNLOAD_KEY" >> /root/.gnupg/gpg.conf \  
&& curl -sSL "$GOSU_DOWNLOAD_ROOT/gosu-amd64" > gosu \  
&& curl -sSL "$GOSU_DOWNLOAD_ROOT/gosu-amd64.asc" > gosu.asc \  
&& gpg --verify gosu.asc \  
&& rm -f gosu.asc \  
&& mv gosu /usr/bin/gosu \  
&& chmod +x /usr/bin/gosu \  
&& rm -rf /root/.gnupg \  
&& curl -sSL "$GOSU_ENTRYPOINT_DOWNLOAD" > /gosu-entrypoint.sh \  
&& chmod +x /gosu-entrypoint.sh  
  
# Specify any standard chown format (uid, uid:gid), default to root:root  
ENV GOSU_USER 0:0  
# Specify any space delimited directories that should be chowned to GOSU_USER  
#ENV GOSU_CHOWN /tmp  
ENTRYPOINT ["/gosu-entrypoint.sh"]  

