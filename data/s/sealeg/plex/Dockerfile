FROM centos:7  
MAINTAINER Giles Thomas <giles@lemonman.org.uk>  
  
ENV PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR /data  
ENV PLEX_MEDIA_SERVER_HOME /usr/lib/plexmediaserver  
ENV PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS 6  
ENV PLEX_MEDIA_SERVER_TMPDIR /tmp  
  
ENV GOSU_VERSION 1.9  
RUN yum -y update \  
&& yum -y install wget \  
&& wget -O /tmp/plexmediaserver.rpm "https://downloads.plex.tv/plex-media-
server/1.0.3.2461-35f0caa/plexmediaserver-1.0.3.2461-35f0caa.x86_64.rpm" \  
&& yum -y install /tmp/plexmediaserver.rpm \  
&& rm -f /tmp/plexmediaserver.rpm \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-
amd64.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net \  
\--recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& yum -y remove wget \  
&& yum clean all  
  
EXPOSE 32400  
COPY entrypoint.sh /  
RUN chmod u+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

