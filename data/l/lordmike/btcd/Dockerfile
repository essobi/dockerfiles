FROM golang:alpine  
  
MAINTAINER Michael Bisbjerg <michael@mbwarez.dk>  
  
EXPOSE 8332 8333 8334 18332 18333 18334  
# Prepare environment, install btcd, remove all traces  
RUN mkdir /root/.btcd && \  
mkdir /root/.btcctl && \  
apk --update add git && \  
go get github.com/btcsuite/btcd/... && \  
apk del git && \  
rm -rf /var/cache/apk/*  
  
# Copy in scripts and config  
COPY base.conf /root/.btcd/btcd.conf  
COPY entry.sh /root/entry.sh  
WORKDIR /root  
  
VOLUME ["/root/.btcd", "/root/.btcctl"]  
  
ENTRYPOINT ["sh", "/root/entry.sh"]

