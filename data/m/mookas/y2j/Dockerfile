FROM alpine  
  
RUN true \  
&& apk add -U libc6-compat git tar wget \  
&& wget -qO /tmp/go.tgz https://storage.googleapis.com/golang/go1.7.3.linux-
amd64.tar.gz \  
&& mkdir -p /opt \  
&& tar xzf /tmp/go.tgz -C /opt \  
&& export PATH=$PATH:/opt/go/bin \  
&& export GOROOT=/opt/go \  
&& export GOPATH=/go \  
&& export GOBIN=/usr/local/bin \  
&& ln -s /lib /lib64 \  
&& mkdir -p ${GOPATH} \  
&& echo $PATH \  
&& go get github.com/echojc/y2j \  
&& apk del -r libc6-compat git tar wget \  
&& rm -r /opt /lib64 /go /tmp/go.tgz /var/cache/apk/* \  
&& true  
  
ENTRYPOINT []  
ENV DESTDIR=/usr/local/bin/  
# We do a `sleep 1` to make sure we give enough time for `docker cp` to start  
CMD echo docker cp $(hostname):/usr/local/bin/y2j ${DESTDIR} ; sleep 1  

