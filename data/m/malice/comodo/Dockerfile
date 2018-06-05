FROM ubuntu:precise  
  
LABEL maintainer "https://github.com/blacktop"  
  
LABEL malice.plugin.repository = "https://github.com/malice-
plugins/comodo.git"  
LABEL malice.plugin.category="av"  
LABEL malice.plugin.mime="*"  
LABEL malice.plugin.docker.engine="*"  
  
RUN buildDeps='ca-certificates \  
build-essential \  
gdebi-core \  
libssl-dev \  
mercurial \  
git-core \  
wget' \  
&& apt-get update -qq \  
&& apt-get install -yq $buildDeps \  
&& echo "===> Install Comodo..." \  
&& cd /tmp \  
&& wget http://download.comodo.com/cis/download/installs/linux/cav-
linux_x64.deb \  
&& DEBIAN_FRONTEND=noninteractive gdebi -n cav-linux_x64.deb \  
&& DEBIAN_FRONTEND=noninteractive /opt/COMODO/post_setup.sh \  
&& echo "===> Clean up unnecessary files..." \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /go /usr/local/go  
  
ENV GO_VERSION 1.8.3  
COPY . /go/src/github.com/malice-plugins/comodo  
RUN buildDeps='ca-certificates \  
build-essential \  
gdebi-core \  
libssl-dev \  
mercurial \  
git-core \  
wget' \  
&& apt-get update -qq \  
&& apt-get install -yq $buildDeps \  
&& echo "===> Install Go..." \  
&& ARCH="$(dpkg --print-architecture)" \  
&& wget https://storage.googleapis.com/golang/go$GO_VERSION.linux-$ARCH.tar.gz
-O /tmp/go.tar.gz \  
&& tar -C /usr/local -xzf /tmp/go.tar.gz \  
&& export PATH=$PATH:/usr/local/go/bin \  
&& echo "===> Building avscan Go binary..." \  
&& cd /go/src/github.com/malice-plugins/comodo \  
&& export GOPATH=/go \  
&& go version \  
&& go get \  
&& go build -ldflags "-X main.Version=$(cat VERSION) -X main.BuildTime=$(date
-u +%Y%m%d)" -o /bin/avscan \  
&& echo "===> Clean up unnecessary files..." \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /go /usr/local/go  
  
# Update Comodo definitions  
RUN mkdir -p /opt/malice  
ADD http://download.comodo.com/av/updates58/sigs/bases/bases.cav
/opt/COMODO/scanners/bases.cav  
  
# Add EICAR Test Virus File to malware folder  
ADD http://www.eicar.org/download/eicar.com.txt /malware/EICAR  
  
WORKDIR /malware  
  
ENTRYPOINT ["/bin/avscan"]  
CMD ["--help"]  

