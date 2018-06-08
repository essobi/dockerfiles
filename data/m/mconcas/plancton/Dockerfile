FROM alpine:3.5  
LABEL maintainer mconcas@cern.ch  
ARG BRANCH=master  
RUN apk add --update py-pip curl unzip && \  
curl -LOk https://github.com/mconcas/plancton/archive/$BRANCH.zip && \  
unzip $BRANCH.zip && \  
cd plancton-$BRANCH && \  
pip install -e . && \  
apk del unzip && \  
rm -f ../$BRANCH.zip && \  
rm -Rf /var/cache/apk/*  
  
COPY entrypoint.sh /tmp/entrypoint.sh  
  
HEALTHCHECK \--interval=1m --timeout=5s \  
CMD stat /var/run/docker.sock && \  
stat /var/run/plancton.pid && \  
planctonctl status && \  
kill -0 `cat /var/run/plancton.pid`  
  
ENTRYPOINT [ "/tmp/entrypoint.sh" ]  

