FROM alpine:3.5  
  
RUN apk add --virtual build-dependencies --no-cache openssl-dev gcc make musl-
dev git binutils \  
&& apk add --no-cache openssl \  
&& mkdir -p /usr/local/src/eschalot /usr/local/lib/eschalot \  
&& cd /usr/local/src/eschalot \  
&& git clone https://github.com/ReclaimYourPrivacy/eschalot.git
/usr/local/src/eschalot \  
&& make clean all install \  
&& cp *.txt /usr/local/lib/eschalot \  
&& apk del build-dependencies \  
&& rm -rf /usr/local/src/eschalot  
  
ENTRYPOINT ["/usr/local/bin/eschalot"]

