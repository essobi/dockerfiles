#Dockerfile-latest  
FROM alpine:latest  
  
ENV BUILDPKGS "git gcc libc-dev make vde2-dev libpcap-dev linux-headers
readline-dev cmake autoconf automake alpine-sdk"  
ENV RUNPKGS "mc"  
RUN apk --update --no-cache add $RUNPKGS && \  
apk --no-cache add --virtual build-dependencies $BUILDPKGS && \  
\  
mkdir /usr/src && cd /usr/src && \  
git clone https://github.com/hercules-390/hyperion.git && \  
cd hyperion && \  
./1Stop && \  
cd /usr/src/x86_64/hyperion && \  
make install && \  
\  
#apk del build-dependencies && \  
#rm -rf /var/cache/apk/* && \  
mkdir /machines  
  
#ENV PATH /usr/src/simh/BIN:$PATH  
#EXPOSE 2323-2326  
ENTRYPOINT ["busybox", "sh"]  

