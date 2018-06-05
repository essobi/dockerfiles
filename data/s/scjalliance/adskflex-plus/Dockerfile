FROM scjalliance/adskflex  
MAINTAINER dusty.wilson@scjalliance.com  
  
RUN yum -y update \  
&& yum -y install \  
git \  
&& yum clean all  
  
# install go  
RUN curl $(curl https://golang.org/dl/ 2>/dev/null | grep .linux-amd64.tar.gz
| head -n1 | sed -r 's/^.*"(.*.linux-amd64.tar.gz)".*/\1/') > /tmp/go.tgz && \  
tar -C /usr/local -zxf /tmp/go.tgz && \  
rm /tmp/go.tgz  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin"  
  
# build weblm  
RUN go get github.com/scjalliance/weblm  
RUN go install github.com/scjalliance/weblm  
  
# add weblm port  
EXPOSE 7259  
# setup init script  
COPY plusrun.sh /opt/  
  
# setup init  
ENTRYPOINT ["/opt/plusrun.sh"]  

