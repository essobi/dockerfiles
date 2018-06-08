FROM ubuntu:16.04  
MAINTAINER Tim Haak <tim@haak.co>  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
TERM="xterm" \  
PLEX_TYPE_FLAG="-p"  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup &&\  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
apt-get -q update && \  
apt-get -qy dist-upgrade && \  
apt-get install -qy \  
iproute2 \  
ca-certificates \  
ffmpeg \  
git \  
jq \  
openssl \  
xmlstarlet \  
curl \  
sudo \  
wget \  
&& \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
ARG PLEX_PASS='false'  
ARG PLEX_TOKEN=''  
RUN if [ "${PLEX_PASS}" = "true" ]; then PLEX_TYPE_FLAG="--
token=${PLEX_TOKEN}" ; fi && \  
git clone \--depth 1 https://github.com/mrworf/plexupdate.git /plexupdate && \  
/plexupdate/plexupdate.sh ${PLEX_TYPE_FLAG} -a -d && \  
apt-get -y purge git &&\  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
VOLUME ["/config","/data"]  
  
ENV RUN_AS_ROOT="true" \  
CHANGE_DIR_RIGHTS="false" \  
CHANGE_CONFIG_DIR_OWNERSHIP="true" \  
HOME="/config" \  
PLEX_DISABLE_SECURITY=1  
EXPOSE 32400 1900/udp 3005 5353/udp 8324 32410/udp 32412/udp 32413/udp
32414/udp 32469  
COPY ./Preferences.xml /Preferences.xml  
COPY ./start.sh /start.sh  
  
CMD ["/start.sh"]  

