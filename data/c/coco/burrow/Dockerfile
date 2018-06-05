FROM alpine:3.4  
ADD config/burrow.cfg /config/burrow.cfg  
ADD config/logging.cfg /config/logging.cfg  
ADD launch-burrow.sh /launch-burrow.sh  
  
RUN apk update \  
&& apk add bash \  
&& apk add git bzr \  
&& apk add go \  
&& apk add ca-certificates \  
&& apk add openssl \  
&& wget https://raw.githubusercontent.com/pote/gpm/v1.4.0/bin/gpm && chmod +x
gpm \  
&& export GOPATH=/gopath \  
&& export BURROW_REPO_PATH="github.com/linkedin/Burrow" \  
&& go get $BURROW_REPO_PATH \  
&& cd $GOPATH/src/${BURROW_REPO_PATH} \  
&& git checkout v0.1.1 \  
&& /gpm install \  
&& go install \  
&& mv $GOPATH/bin/Burrow / \  
&& apk del go git bzr \  
&& rm -rf $GOPATH /var/cache/apk/* /gpm \  
&& touch /burrow.out \  
&& ln -sf /proc/1/fd/1 /burrow.out  
  
CMD [ "/launch-burrow.sh" ]

