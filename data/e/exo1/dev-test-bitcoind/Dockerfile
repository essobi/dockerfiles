FROM exo1/dev-base-1:latest  
MAINTAINER Max Kaye <max@exo1.tech>  
  
ARG USER_ID  
ARG GROUP_ID  
  
ENV SVST_USER svst  
ENV TERM xterm  
ENV HOME /bitcoin  
  
# add user with specified (or default) user/group ids  
ENV USER_ID ${USER_ID:-1000}  
ENV GROUP_ID ${GROUP_ID:-1000}  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -g ${GROUP_ID} bitcoin \  
&& useradd -u ${USER_ID} -g bitcoin -s /bin/bash -m -d /bitcoin bitcoin  
  
# Install Bitcoind  
WORKDIR /root  
  
ADD files/configure-bitcoin-nulldata.sh /root  
ADD files/build-bitcoin-nulldata.sh /root  
  
RUN git clone https://gitlab.com/exo-one/bitcoin-nulldata --depth=1 \  
&& /root/configure-bitcoin-nulldata.sh \  
&& /root/build-bitcoin-nulldata.sh \  
&& rm -r /root/bitcoin-nulldata  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
wget  
RUN wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y \  
ca-certificates \  
wget \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD ./bin /usr/local/bin  
  
# add here to prevent rebuilding image much  
RUN cd /root/bitcoin-nulldata && make clean  
  
VOLUME ["/bitcoin"]  
  
EXPOSE 8332 8333 18332 18333  
WORKDIR /bitcoin  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
ARG whichnet=""  
ENV WHICHNET ${whichnet}  
  
CMD ["sh", "-c", "btc_oneshot $WHICHNET"]  

