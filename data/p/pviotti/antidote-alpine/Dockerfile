FROM bitwalker/alpine-erlang:19.3  
  
ENV HANDOFF_PORT="8099" \  
PB_PORT="8087" \  
PB_IP="0.0.0.0" \  
PBSUB_PORT="8086" \  
LOGREADER_PORT="8085" \  
RING_STATE_DIR="data/ring" \  
PLATFORM_DATA_DIR="data" \  
NODE_NAME="antidote@127.0.0.1" \  
SHORT_NAME="false" \  
ANTIDOTE_REPO="https://github.com/SyncFree/antidote.git" \  
ANTIDOTE_BRANCH="master"  
  
RUN set -xe \  
&& apk --no-cache --update upgrade busybox musl \  
&& apk --no-cache add bash coreutils git curl build-base \  
&& apk --no-cache add iptables \  
&& cd /tmp \  
&& git clone $ANTIDOTE_REPO \  
&& cd antidote \  
&& git checkout $ANTIDOTE_BRANCH \  
&& make rel \  
&& cp -R _build/default/rel/antidote /opt/ \  
&& sed -e '$i,{kernel, [{inet_dist_listen_min, 9100}, {inet_dist_listen_max,
9100}]}' /tmp/antidote/_build/default/rel/antidote/releases/0.0.1/sys.config >
/opt/antidote/releases/0.0.1/sys.config \  
&& sed -i '7i{ring_creation_size, 8},' /opt/antidote/releases/0.0.1/sys.config
\  
&& apk del git curl \  
&& rm -rf /tmp/antidote /var/cache/apk/*  
  
ADD ./start_and_attach.sh /opt/antidote/  
ADD ./entrypoint.sh /  
  
RUN chmod a+x /opt/antidote/start_and_attach.sh \  
&& chmod a+x /entrypoint.sh  
  
# Distributed Erlang Port Mapper  
EXPOSE 4368  
# Ports for Antidote  
EXPOSE 8085 8086 8087 8099  
# Antidote RPC  
EXPOSE 9100  
  
VOLUME /opt/antidote/data  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/opt/antidote/start_and_attach.sh"]  

