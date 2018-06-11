FROM docker:1.12  
ENV GOPATH /go  
ENV SRCPATH ${GOPATH}/src/github.com/adnanh  
ENV WEBHOOK_VERSION 2.4.0  
ENV JQ_VERSION 1.5  
ENV VDOCKER_VERSION 0.0.4  
RUN apk add --update -t build-deps curl git go libc-dev gcc libgcc && \  
apk add --update bash tar xz bzip2 && \  
curl -L -o /tmp/webhook-${WEBHOOK_VERSION}.tar.gz
https://github.com/adnanh/webhook/archive/${WEBHOOK_VERSION}.tar.gz && \  
mkdir -p ${SRCPATH} && tar -xvzf /tmp/webhook-${WEBHOOK_VERSION}.tar.gz -C
${SRCPATH} && \  
mv -f ${SRCPATH}/webhook-* ${SRCPATH}/webhook && \  
cd ${SRCPATH}/webhook && go get -d && go build -o /usr/local/bin/webhook && \  
curl -L -o /usr/bin/jq
https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64
&& \  
chmod a+x /usr/bin/jq && \  
curl -L -o /usr/bin/vdocker
https://github.com/wpalmer/vdocker/releases/download/v${VDOCKER_VERSION}/vdocker.sh
&& \  
chmod a+x /usr/bin/vdocker && \  
apk del --purge build-deps && \  
rm -rf /var/cache/apk/* && \  
rm -rf ${GOPATH}  
  
EXPOSE 9000  
ENTRYPOINT ["/usr/local/bin/webhook"]  
RUN apk add --update git openssh-client \  
&& mkdir -p /etc/ssh \  
&& { \  
echo -n 'github.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9' \  
&& echo -n 'tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pL' \  
&& echo -n 'lVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFz' \  
&& echo -n 'LQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFI' \  
&& echo -n 'mWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eO' \  
&& echo -n 'zQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqn' \  
&& echo 'TWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==' \  
; } > /etc/ssh/ssh_known_hosts  
  

