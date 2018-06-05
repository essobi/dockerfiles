FROM debian:jessie  
  
LABEL maintainer "https://github.com/blacktop"  
  
LABEL malice.plugin.repository = "https://github.com/malice-
plugins/fsecure.git"  
LABEL malice.plugin.category="av"  
LABEL malice.plugin.mime="*"  
LABEL malice.plugin.docker.engine="*"  
  
ENV FSECURE_VERSION 11.10.68  
# Install Requirements  
RUN buildDeps='ca-certificates wget rpm' \  
&& apt-get update -qq \  
&& apt-get install -yq $buildDeps lib32stdc++6 psmisc \  
&& echo "===> Install F-Secure..." \  
&& cd /tmp \  
&& wget -q
https://download.f-secure.com/corpro/ls/trial/fsls-${FSECURE_VERSION}-rtm.tar.gz
\  
&& tar zxvf fsls-${FSECURE_VERSION}-rtm.tar.gz \  
&& cd fsls-${FSECURE_VERSION}-rtm \  
&& chmod a+x fsls-${FSECURE_VERSION} \  
&& ./fsls-${FSECURE_VERSION} \--auto standalone lang=en --command-line-only \  
&& fsav --version \  
&& echo "===> Update F-Secure..." \  
&& cd /tmp \  
&& wget -q http://download.f-secure.com/latest/fsdbupdate9.run \  
&& mv fsdbupdate9.run /opt/f-secure/ \  
&& echo "===> Clean up unnecessary files..." \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
# Update F-Secure  
RUN echo "===> Update F-Secure Database..." \  
&& /etc/init.d/fsaua start \  
&& /etc/init.d/fsupdate start \  
&& /opt/f-secure/fsav/bin/dbupdate /opt/f-secure/fsdbupdate9.run; exit 0  
  
ENV GO_VERSION 1.8.3  
# Install Go binary  
COPY . /go/src/github.com/malice-plugins/fsecure  
RUN buildDeps='ca-certificates \  
build-essential \  
mercurial \  
git-core \  
wget' \  
&& apt-get update -qq \  
&& apt-get install -yq $buildDeps \--no-install-recommends \  
&& echo "===> Install Go..." \  
&& ARCH="$(dpkg --print-architecture)" \  
&& wget -q
https://storage.googleapis.com/golang/go$GO_VERSION.linux-$ARCH.tar.gz \  
-O /tmp/go.tar.gz \  
&& tar -C /usr/local -xzf /tmp/go.tar.gz \  
&& export PATH=$PATH:/usr/local/go/bin \  
&& echo "===> Building avscan Go binary..." \  
&& cd /go/src/github.com/malice-plugins/fsecure \  
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
RUN mkdir -p /opt/malice  
COPY update.sh /opt/malice/update  
  
WORKDIR /malware  
  
ENTRYPOINT ["/bin/avscan"]  
CMD ["--help"]  
  
# https://download.f-secure.com/corpro/ls/trial/fsls-11.10.68-rtm.tar.gz  

