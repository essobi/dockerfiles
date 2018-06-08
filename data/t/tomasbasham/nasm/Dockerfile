FROM alpine:3.4  
LABEL com.tomasbasham.maintainer "Tomas Basham <me@tomasbasham.co.uk>" \  
com.tomasbasham.version "2.11.08-r0" \  
com.tomasbasham.description "Netwide Assembler"  
  
ENV VERSION 2.11.08-r0  
  
# Install qemu  
RUN apk add --no-cache nasm=${VERSION} \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["/usr/bin/nasm"]  
CMD ["-h"]  

