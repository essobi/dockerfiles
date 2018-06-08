FROM alpine:3.4 as builder  
  
RUN apk --no-cache add g++ scons curl-dev boost-dev bash  
  
ADD . /opt/src  
RUN cd /opt/src && scons && scons check=1  
RUN strip /opt/src/smtp-http-proxy  
  
FROM alpine:3.4  
RUN apk --no-cache add \  
boost \  
boost-program_options \  
libcurl \  
libstdc++ \  
libcrypto1.0 \  
libssl1.0 \  
zlib \  
;  
COPY \--from=builder /opt/src/smtp-http-proxy /opt/src/smtp-http-proxy  
ENTRYPOINT ["/opt/src/smtp-http-proxy"]  
CMD ["--help"]  

