FROM ubuntu:xenial  
  
LABEL maintainer "https://github.com/blacktop"  
  
LABEL malice.plugin.repository = "https://github.com/malice-plugins/zoner.git"  
LABEL malice.plugin.category="av"  
LABEL malice.plugin.mime="*"  
LABEL malice.plugin.docker.engine="*"  
  
ARG ZONE_KEY  
ENV ZONE 1.3.0  
RUN buildDeps='ca-certificates wget build-essential' \  
&& apt-get update -qq \  
&& apt-get install -yq $buildDeps libc6-i386 \  
&& echo "===> Install Zoner AV..." \  
&& wget -q -P /tmp
http://update.zonerantivirus.com/download/zav-${ZONE}-ubuntu-amd64.deb \  
&& dpkg -i /tmp/zav-${ZONE}-ubuntu-amd64.deb; \  
if [ "x$ZONE_KEY" != "x" ]; then \  
echo "===> Updating License Key..."; \  
sed -i "s/UPDATE_KEY.*/UPDATE_KEY = ${ZONE_KEY}/g" /etc/zav/zavd.conf; \  
fi \  
&& echo "===> Clean up unnecessary files..." \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV GO_VERSION 1.8.3  
COPY . /go/src/github.com/malice-plugins/zoner  
RUN buildDeps='ca-certificates \  
build-essential \  
gdebi-core \  
libssl-dev \  
mercurial \  
git-core \  
wget' \  
&& apt-get update -qq \  
&& apt-get install -yq $buildDeps libc6-i386 \  
&& set -x \  
&& echo "===> Install Go..." \  
&& ARCH="$(dpkg --print-architecture)" \  
&& wget -q
https://storage.googleapis.com/golang/go$GO_VERSION.linux-$ARCH.tar.gz -O
/tmp/go.tar.gz \  
&& tar -C /usr/local -xzf /tmp/go.tar.gz \  
&& export PATH=$PATH:/usr/local/go/bin \  
&& echo "===> Building avscan Go binary..." \  
&& cd /go/src/github.com/malice-plugins/zoner \  
&& export GOPATH=/go \  
&& go version \  
&& go get \  
&& go build -ldflags "-X main.Version=$(cat VERSION) -X main.BuildTime=$(date
-u +%Y%m%d)" -o /bin/avscan \  
&& echo "===> Clean up unnecessary files..." \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /go /usr/local/go  
  
RUN mkdir -p /opt/malice  
RUN if [ "x$ZONE_KEY" != "x" ]; then \  
echo "===> Update zoner definitions..."; \  
/etc/init.d/zavd update; \  
fi  
  
# Add EICAR Test Virus File to malware folder  
ADD http://www.eicar.org/download/eicar.com.txt /malware/EICAR  
  
WORKDIR /malware  
  
ENTRYPOINT ["/bin/avscan"]  
CMD ["--help"]  
  
# CMD /etc/init.d/zavd start --no-daemon && zavcli --no-show=clean,nonstandard
--color /malware  

