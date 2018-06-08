FROM docker.io/centos:latest  
  
USER root  
  
RUN yum update -y && \  
yum install -y --setopt=tsflags=nodocs git yum-utils unzip golang bzr gettext
&& \  
yum -y clean all && \  
rm -rf /var/cache/yum  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
ENV BZR_LOG /clair/bzr/bzr.log  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && \  
chmod -R 770 "$GOPATH" && \  
mkdir -p $GOPATH/src/github.com/coreos && \  
cd /$GOPATH/src/github.com/coreos && \  
git clone -b release-2.0 https://github.com/coreos/clair.git && \  
go install github.com/coreos/clair/cmd/clair && \  
mkdir /clair && \  
mkdir /clair/config && \  
touch /clair/config/config.yaml && \  
mkdir /clair/bzr && \  
touch /clair/bzr/bzr.log && \  
mkdir /clair/bin && \  
chmod 770 /clair && \  
chmod 770 /clair/bzr && \  
chmod 660 /clair/bzr/bzr.log && \  
cp /go/bin/clair /clair/bin/  
  
ADD config/config.yaml.template /clair/config/  
ADD scripts/run-clair.sh /clair/bin/  
  
RUN chmod 660 /clair/config/config.yaml.template && \  
chmod 660 /clair/config/config.yaml && \  
chmod 660 /clair/bin/run-clair.sh && \  
chmod a+x /clair/bin/run-clair.sh && \  
chmod g=u /etc/passwd  
  
ENTRYPOINT ["/clair/bin/run-clair.sh"]  
  

