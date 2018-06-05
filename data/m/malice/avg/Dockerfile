FROM debian:jessie  
  
LABEL maintainer "https://github.com/blacktop"  
  
ENV GO_VERSION 1.8.3  
# Install Requirements  
COPY . /go/src/github.com/malice-plugins/malice-avg  
RUN buildDeps='ca-certificates \  
build-essential \  
mercurial \  
git-core \  
unzip \  
curl' \  
&& apt-get update -qq \  
&& apt-get install -yq $buildDeps libc6-i386 --no-install-recommends \  
&& echo "===> Install AVG..." \  
&& curl -Ls
http://download.avgfree.com/filedir/inst/avg2013flx-r3118-a6926.i386.deb >
/tmp/avg.deb \  
&& dpkg -i /tmp/avg.deb \  
&& /etc/init.d/avgd restart \  
&& avgcfgctl -w UpdateVir.sched.Task.Disabled=true \  
&& avgcfgctl -w Default.setup.daemonize=false \  
&& echo "===> Install Go..." \  
&& cd /tmp \  
&& curl -Ls https://storage.googleapis.com/golang/go$GO_VERSION.linux-
amd64.tar.gz > /tmp/go.tar.gz \  
&& tar -C /usr/local -xzf /tmp/go.tar.gz \  
&& export PATH=$PATH:/usr/local/go/bin \  
&& echo "===> Building avscan Go binary..." \  
&& cd /go/src/github.com/malice-plugins/malice-avg \  
&& export GOPATH=/go \  
&& go version \  
&& go get \  
&& go build -ldflags "-X main.Version=$(cat VERSION) -X main.BuildTime=$(date
-u +%Y%m%d)" -o /bin/avscan \  
&& echo "===> Clean up unnecessary files..." \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /go /usr/local/go  
  
# Update AVG Definitions  
RUN mkdir -p /opt/malice && /etc/init.d/avgd restart && avgupdate  
  
# Add EICAR Test Virus File to malware folder  
ADD http://www.eicar.org/download/eicar.com.txt /malware/EICAR  
  
WORKDIR /malware  
  
ENTRYPOINT ["/bin/avscan"]  
CMD ["--help"]  

