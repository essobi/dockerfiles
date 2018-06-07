FROM alpine:latest  
COPY libfaketime /libfaketime  
RUN apk add --update alpine-sdk  
RUN cd /libfaketime; make; make install; rm -Rf /libfaketime  
RUN apk del alpine-sdk  
#ENV LD_PRELOAD=/usr/local/lib/faketime/libfaketime.so.1  
ENV FAKETIME_NO_CACHE=1  
ENV DONT_FAKE_MONOTONIC=1  
# FAKETIME='+15d' sh -c 'while true; do date; sleep 1; done'  

