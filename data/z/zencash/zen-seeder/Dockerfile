FROM zencash/gosu-base:1.10  
MAINTAINER cronicc@protonmail.com  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install
apt-utils \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install
git build-essential libboost-all-dev libssl-dev ca-certificates wget \  
&& git clone -b master --single-branch https://github.com/ZencashOfficial/zen-
seeder.git /root/seeder \  
&& cd /root/seeder \  
&& make \  
&& install -m 755 dnsseed /usr/local/bin/dnsseed-avx \  
&& cd \  
&& rm -rf /root/seeder \  
&& git clone -b portable --single-branch
https://github.com/ZencashOfficial/zen-seeder.git /root/seeder \  
&& cd /root/seeder \  
&& make \  
&& install -m 755 dnsseed /usr/local/bin \  
&& cd \  
&& rm -rf /root/seeder \  
&& DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove git build-
essential libboost-all-dev libssl-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# grab tini for signal processing and zombie killing  
ENV TINI_VERSION v0.15.0  
RUN set -x \  
&& wget -O /usr/local/bin/tini
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini" \  
&& wget -O /usr/local/bin/tini.asc
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
6380DC428747F6C393FEACA59A84159D7001A4E5 \  
&& gpg --batch --verify /usr/local/bin/tini.asc /usr/local/bin/tini \  
&& rm -r "$GNUPGHOME" /usr/local/bin/tini.asc \  
&& chmod +x /usr/local/bin/tini \  
&& tini -h  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
# default dns seeder ports  
EXPOSE 5353/tcp 5353/udp  
  
VOLUME /mnt/seeder  
  
WORKDIR /mnt/seeder  
  
CMD ["zen-dnsseed"]  

