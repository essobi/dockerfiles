FROM alpine:3.6 AS builder  
MAINTAINER Ray Tsang  
  
RUN apk add --update alpine-sdk openssl-dev  
RUN apk add --no-cache git  
  
RUN git clone https://github.com/giltene/wrk2.git  
ENV LDFLAGS -static-libgcc  
ENV CFLAGS -static-libgcc  
RUN cd wrk2 && make -j2  
  
FROM alpine:3.6  
RUN apk add --update openssl && apk --no-cache add ca-certificates  
COPY \--from=builder /wrk2/wrk /bin  
ENTRYPOINT ["wrk"]  

