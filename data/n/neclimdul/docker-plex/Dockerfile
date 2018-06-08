FROM phusion/baseimage  
MAINTAINER James Gilliland <neclimdul@gmail.com>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
VOLUME ["/config","/data"]  
EXPOSE 32400  
HEALTHCHECK \--interval=60s --timeout=2s --start-period=120s \  
CMD curl -L 'http://localhost:32400/web/index.html'  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
TERM="xterm" \  
RUN_AS_ROOT="false" \  
CHANGE_DIR_RIGHTS="false" \  
CHANGE_CONFIG_DIR_OWNERSHIP="true" \  
PLEX_HOME="/config" \  
PLEX_DISABLE_SECURITY=1 \  
PLEX_URL="https://nerdpalace.net/plexpass.json"  
ENV buildDeps="jq wget"  
ADD install.sh /install.sh  
  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup \  
&& echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache \  
&& apt-get -qq update \  
&& apt-get -qqy dist-upgrade \  
&& apt-get install -qqy \  
iproute2 \  
ca-certificates \  
openssl \  
xmlstarlet \  
curl \  
$buildDeps \  
&& sh /install.sh \  
&& apt-get purge -qy $buildDeps \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
rm -rf /tmp/*  
  
ADD Preferences.xml /Preferences.xml  
  
RUN mkdir /etc/service/plex  
COPY plex.sh /etc/service/plex/run  
RUN chmod +x /etc/service/plex/run  
  
RUN mkdir -p /etc/my_init.d  
COPY bootstrap.sh /etc/my_init.d/bootstrap.sh  
RUN chmod +x /etc/my_init.d/bootstrap.sh  

