FROM alpine:edge  
LABEL maintainer="https://keybase.io/tcely"  
  
RUN apk --update upgrade && \  
apk add ca-certificates less man zstd zstd-doc && \  
rm -rf /var/cache/apk/*  
  
ENV PAGER less  
ENTRYPOINT ["/usr/bin/zstd"]  
CMD ["--help"]  

