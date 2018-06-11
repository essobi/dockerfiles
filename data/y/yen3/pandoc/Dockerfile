FROM alpine as builder  
  
ARG VERSION=2.0.2  
RUN apk add --no-cache --virtual .build-deps ca-certificates wget \  
&& wget
https://github.com/jgm/pandoc/releases/download/${VERSION}/pandoc-${VERSION}-linux.tar.gz
\  
&& tar xf pandoc-${VERSION}-linux.tar.gz \  
&& cp pandoc-${VERSION}/bin/* /usr/bin/ \  
&& apk del .build-deps  
  
FROM scratch  
  
WORKDIR "/data"  
  
COPY \--from=builder /usr/bin/pandoc /pandoc  
  
CMD ["-h"]  
  
ENTRYPOINT ["/pandoc"]  

