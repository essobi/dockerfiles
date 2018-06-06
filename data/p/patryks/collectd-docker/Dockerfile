FROM debian:jessie  
  
ENV GOLANG_VERSION "1.6"  
ENV GOLANG_DOWNLOAD_URL "https://golang.org/dl/go${GOLANG_VERSION}.linux-
amd64.tar.gz"  
ENV GOLANG_DOWNLOAD_SHA256
"5470eac05d273c74ff8bac7bef5bad0b5abbd1c4052efbdbc8db45332e836b0b"  
ENV GOLANG_DOWNLOAD_DESTINATION "/tmp/go${GOLANG_VERSION}.linux-amd64.tar.gz"  
ENV GOPATH "/go"  
ENV PATH "${GOPATH}/bin:/usr/local/go/bin:${PATH}"  
  
COPY collector /go/src/github.com/patryk-s/collectd-docker/collector  
COPY docker/run.sh /run.sh  
COPY docker/collectd.conf.tpl /etc/collectd/collectd.conf.tpl  
COPY docker/stunnel.conf.templ /etc/collectd/stunnel.conf.templ  
  
RUN echo "APT::Install-Recommends false;" >>
/etc/apt/apt.conf.d/recommends.conf && \  
echo "APT::Install-Suggests false;" >> /etc/apt/apt.conf.d/recommends.conf &&
\  
echo "APT::AutoRemove::RecommendsImportant false;" >>
/etc/apt/apt.conf.d/recommends.conf && \  
echo "APT::AutoRemove::SuggestsImportant false;" >>
/etc/apt/apt.conf.d/recommends.conf  
  
RUN echo "deb http://pkg.ci.collectd.org/deb jessie master" >>
/etc/apt/sources.list \  
&& gpg --recv-keys \--keyserver pool.sks-keyservers.net 3994D24FB8543576 \  
&& gpg --export -a 3994D24FB8543576 | apt-key add -  
  
RUN apt-get update && \  
apt-get install -y collectd gettext stunnel4 git curl ca-certificates && \  
curl -sL "${GOLANG_DOWNLOAD_URL}" > "${GOLANG_DOWNLOAD_DESTINATION}" && \  
echo "${GOLANG_DOWNLOAD_SHA256} ${GOLANG_DOWNLOAD_DESTINATION}" | sha256sum -c
&& \  
tar -C /usr/local -xzf "${GOLANG_DOWNLOAD_DESTINATION}" && \  
rm "${GOLANG_DOWNLOAD_DESTINATION}" && \  
rm -rf /var/lib/apt/lists/* && \  
go get github.com/docker-infra/reefer && \  
go get github.com/tools/godep && \  
cd /go/src/github.com/patryk-s/collectd-docker/collector && \  
godep restore && \  
go get github.com/patryk-s/collectd-docker/collector/... && \  
cp /go/bin/collectd-docker-collector /usr/bin/collectd-docker-collector && \  
cp /go/bin/reefer /usr/bin/reefer && \  
apt-get remove -y git curl ca-certificates && \  
apt-get autoremove -y && \  
cd / && \  
rm -rf /go /usr/local/go  
  
ENTRYPOINT ["/run.sh"]  

