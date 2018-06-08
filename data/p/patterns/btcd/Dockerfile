FROM alpine  
  
LABEL maintainer="興怡"  
ENV GOPATH=/go \  
PROJ_DIR=github.com/btcsuite/btcd  
  
RUN apk add --no-cache git glide go musl-dev \  
&& mkdir -p $GOPATH/src && cd $GOPATH/src \  
&& git clone https://${PROJ_DIR} ${PROJ_DIR} \  
&& cd $PROJ_DIR \  
&& glide install \  
&& go install . ./cmd/... \  
&& apk del glide git go musl-dev \  
&& rm -rf /apk /tmp/* /var/cache/apk/* $GOPATH/src/*  
  
EXPOSE 8333 8334  
CMD ["/go/bin/btcd", "--help"]  
  

