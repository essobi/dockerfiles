FROM ubuntu:xenial  
  
LABEL maintainer "https://github.com/blacktop"  
  
LABEL malice.plugin.repository = "https://github.com/malice-plugins/avast.git"  
LABEL malice.plugin.category="av"  
LABEL malice.plugin.mime="*"  
LABEL malice.plugin.docker.engine="*"  
  
# ENV AVAST_VERSION 2.1.2-1  
# Install Avast AV  
COPY license.avastlic /etc/avast/license.avastlic  
RUN apt-get update -qq \  
&& apt-get install -yq ca-certificates --no-install-recommends \  
&& echo "===> Install Avast..." \  
&& echo 'deb http://deb.avast.com/lin/repo debian release' >>
/etc/apt/sources.list \  
&& apt-key adv --fetch-keys
http://files.avast.com/files/resellers/linux/avast.gpg \  
&& apt-get update -q && apt-get install -y avast-fss \  
&& chown avast:avast /etc/avast/license.avastlic \  
# patch update script  
&& download='DOWNLOAD="curl -L -s --connect-timeout 5 -f"' \  
&& download_fix='DOWNLOAD="curl -L -s -f"' \  
&& sed -i "s|$download|$download_fix|g" /var/lib/avast/Setup/avast.setup \  
&& echo "===> Clean up unnecessary files..." \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/*  
  
# Update Avast Definitions  
RUN mkdir -p /opt/malice && echo "===> Update Avast..." &&
/var/lib/avast/Setup/avast.vpsupdate  
  
ENV GO_VERSION 1.8.3  
# Install Go binary  
COPY . /go/src/github.com/maliceio/malice-avast  
RUN buildDeps='build-essential \  
mercurial \  
git-core \  
wget' \  
&& apt-get update -qq \  
&& apt-get install -yq $buildDeps \--no-install-recommends \  
&& echo "===> Install Go..." \  
&& ARCH="$(dpkg --print-architecture)" \  
&& wget -q
https://storage.googleapis.com/golang/go$GO_VERSION.linux-$ARCH.tar.gz -O
/tmp/go.tar.gz \  
&& tar -C /usr/local -xzf /tmp/go.tar.gz \  
&& export PATH=$PATH:/usr/local/go/bin \  
&& echo "===> Building avscan Go binary..." \  
&& cd /go/src/github.com/maliceio/malice-avast \  
&& export GOPATH=/go \  
&& go version \  
&& go get \  
&& go build -ldflags "-X main.Version=$(cat VERSION) -X main.BuildTime=$(date
-u +%Y%m%d)" -o /bin/avscan \  
&& echo "===> Clean up unnecessary files..." \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /go /usr/local/go  
  
# Add EICAR Test Virus File to malware folder  
ADD http://www.eicar.org/download/eicar.com.txt /malware/EICAR  
  
WORKDIR /malware  
  
ENTRYPOINT ["/bin/avscan"]  
CMD ["--help"]  
  
# NOTE: https://www.avast.com/en-us/faq.php?article=AVKB131  
# NOTE: To Update run - /var/lib/avast/Setup/avast.vpsupdate  
# http://files.avast.com/lin/repo/pool/avast_2.1.2-1_amd64.deb  
# http://files.avast.com/lin/repo/pool/avast-fss_1.0.11-1_amd64.deb  
# https://www.avast.com/registration-free-antivirus.php  

