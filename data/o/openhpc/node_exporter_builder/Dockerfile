FROM centos:latest  
LABEL name="Node Exporter Builder" \  
vendor="Prometheus" \  
version="2" \  
maintainer="gaojingan@gmail.com"  
  
VOLUME ["/export"]  
COPY compile.sh /usr/local/bin/compile.sh  
  
ENV GOLANG_VERSION 1.9  
ENV GOLANG_DOWNLOAD_URL=https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz \  
GOLANG_DOWNLOAD_SHA256='d70eadefce8e160638a9a6db97f7192d8463069ab33138893ad3bf31b0650a79'  
RUN yum -y install bash git curl environment-modules make gcc \  
&& yum clean all \  
&& curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz \  
&& mkdir -p /go/src \  
&& mkdir -p /go/bin \  
&& mkdir -p /go/pkg \  
&& chmod +x /usr/local/bin/compile.sh  
  
ADD golang.module /etc/modulefiles/golang/$GOLANG_VERSION  
  
ENTRYPOINT ["/usr/local/bin/compile.sh"]  

