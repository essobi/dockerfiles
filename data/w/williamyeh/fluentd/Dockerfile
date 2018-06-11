# Fluentd (td-agent version) for Debian jessie  
#  
# URL: https://github.com/William-Yeh/docker-fluentd  
#  
# Reference:  
# - http://docs.fluentd.org/articles/install-by-deb  
# - http://docs.treasuredata.com/articles/td-agent  
# - http://packages.treasuredata.com.s3.amazonaws.com/  
#  
# Also installed plugins:  
# - https://github.com/tagomoris/fluent-plugin-secure-forward  
# - https://github.com/y-ken/fluent-plugin-watch-process  
# - https://github.com/frsyuki/fluent-plugin-multiprocess  
# - https://github.com/kiyoto/fluent-plugin-docker-metrics  
# - https://github.com/uken/fluent-plugin-elasticsearch  
# - https://github.com/htgc/fluent-plugin-kafka/  
#  
# Version 0.2  
#  
# pull base image  
FROM debian:jessie  
MAINTAINER William Yeh <william.pjyeh@gmail.com>  
  
  
ENV EMBEDDED_BIN /opt/td-agent/embedded/bin  
ENV FLUENT_GEM $EMBEDDED_BIN/fluent-gem  
#ENV FLUENT_GEM /opt/td-agent/embedded/bin/fluent-gem  
ENV DEB_FILE
http://packages.treasuredata.com.s3.amazonaws.com/2/debian/wheezy/pool/contrib/t/td-
agent/td-agent_2.1.4-0_amd64.deb  
  
  
  
# echo "==> Download & install..." && \  
# curl -o install.sh -L http://toolbelt.treasuredata.com/sh/install-debian-
wheezy-td-agent2.sh && \  
# chmod a+x install.sh && \  
# sed -i 's/^sudo -k/#sudo -k/' install.sh && \  
# sed -i 's/^sudo sh/sh/' install.sh && \  
# ./install.sh && \  
# rm install.sh && \  
RUN apt-get update && \  
echo "==> Install curl & helper tools..." && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y -q --no-install-recommends curl && \  
\  
\  
\  
echo "==> Download & install..." && \  
cd /opt && \  
curl -o td-agent.deb -L $DEB_FILE && \  
dpkg -i td-agent.deb && \  
rm *.deb && \  
\  
\  
\  
echo "==> Configure..." && \  
ulimit -n 65536 && \  
mkdir -p /data && \  
mv /etc/td-agent/td-agent.conf /etc/td-agent/td-agent.conf.bak && \  
\  
\  
\  
echo "===> Install other plugins (may need to compile)..." && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y -q gcc make libcurl4-gnutls-dev && \  
$FLUENT_GEM install \  
fluent-plugin-secure-forward \  
fluent-plugin-watch-process \  
fluent-plugin-multiprocess \  
fluent-plugin-docker-metrics \  
fluent-plugin-elasticsearch \  
\--no-rdoc --no-ri && \  
\  
\  
\  
echo "==> Clean up..." && \  
apt-get remove -y --auto-remove curl gcc make ruby-dev libgssglue1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
#RUN $FLUENT_GEM install \  
# fluent-plugin-kafka \  
# --no-rdoc --no-ri  
# configure  
VOLUME [ "/etc/td-agent", "/data" ]  
WORKDIR /etc/td-agent  
ENV LD_PRELOAD /opt/td-agent/embedded/lib/libjemalloc.so  
  
  
# Fluentd ports  
# - 24224: in_forward (TCP input)  
# - 9880: in_http (HTTP input via POST)  
# - 24230: debug_agent  
# - 24220: monitor_agent (monitoring agent)  
EXPOSE 24224 9880 24230  
# for convenience  
ENV PATH /opt:$EMBEDDED_BIN:$PATH  
COPY usage.sh /opt/  
COPY start /opt/  
COPY td-agent.conf /etc/td-agent/  
COPY httppost-to-stdout.conf /etc/td-agent/  
COPY httppost-to-file.conf /etc/td-agent/  
RUN date '+%Y-%m-%dT%H:%M:%S%:z' > /var/log/DOCKER_BUILD_TIME  
  
# Define default command.  
CMD ["usage.sh"]  

