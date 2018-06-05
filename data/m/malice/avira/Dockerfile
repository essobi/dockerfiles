FROM ubuntu:xenial  
  
LABEL maintainer "https://github.com/blacktop"  
  
LABEL malice.plugin.repository = "https://github.com/malice-plugins/avira.git"  
LABEL malice.plugin.category="av"  
LABEL malice.plugin.mime="*"  
LABEL malice.plugin.docker.engine="*"  
  
RUN buildDeps='ca-certificates file unzip curl' \  
&& dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -yq $buildDeps libc6-i386 \  
&& echo "===> Install Avira..." \  
&& curl -sSL "http://professional.avira-
update.com/package/scancl/linux_glibc22/en/scancl-linux_glibc22.tar.gz" \  
| tar -xzf - -C /tmp \  
&& mv /tmp/scancl* /opt/avira \  
&& curl -sSL -o /tmp/fusebundlegen.zip "http://install.avira-
update.com/package/fusebundlegen/linux_glibc22/en/avira_fusebundlegen-
linux_glibc22-en.zip" \  
&& cd /tmp && unzip /tmp/fusebundlegen.zip \  
&& /tmp/fusebundle.bin \  
&& mv install/fusebundle-linux_glibc22-int.zip /opt/avira \  
&& cd /opt/avira && unzip fusebundle-linux_glibc22-int.zip \  
&& echo "===> Clean up unnecessary files..." \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
ENV GO_VERSION 1.8.3  
COPY . /go/src/github.com/malice-plugins/avira  
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
&& cd /go/src/github.com/malice-plugins/avira \  
&& export GOPATH=/go \  
&& go version \  
&& go get \  
&& go build -ldflags "-X main.Version=$(cat VERSION) -X main.BuildTime=$(date
-u +%Y%m%d)" -o /bin/avscan \  
&& echo "===> Clean up unnecessary files..." \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /go /usr/local/go  
  
ARG AVIRA_KEY  
  
# COPY hbedv.key /opt/avira  
RUN if [ "x$AVIRA_KEY" != "x" ]; then \  
echo "===> Adding Avira License Key..."; \  
mkdir -p /opt/avira; \  
echo -n "$AVIRA_KEY" | base64 -d > /opt/avira/hbedv.key ; \  
fi  
  
# Add EICAR Test Virus File to malware folder  
ADD http://www.eicar.org/download/eicar.com.txt /malware/EICAR  
RUN mkdir -p /opt/malice  
COPY update.sh /opt/malice/update  
  
WORKDIR /malware  
  
ENTRYPOINT ["/bin/avscan"]  
CMD ["--help"]  

