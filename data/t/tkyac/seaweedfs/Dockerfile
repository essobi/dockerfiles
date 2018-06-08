FROM frolvlad/alpine-glibc:alpine-3.6  
# grab su-exec for easy step-down from root  
RUN apk add --no-cache 'su-exec>=0.2' ca-certificates  
  
RUN apk add --no-cache --virtual=.deps --update curl wget && \  
wget --no-verbose -P /tmp
https://github.com/chrislusf/seaweedfs/releases/download/0.76/linux_amd64.tar.gz
&& \  
tar -C /usr/bin/ -xzvf /tmp/linux_amd64.tar.gz && \  
apk del .deps && \  
rm -rf /tmp/*  
  
EXPOSE 8000  
EXPOSE 8001  
EXPOSE 9333  
ARG USER_ID=1000  
ARG GROUP_ID=500  
RUN addgroup -g $GROUP_ID docker && \  
adduser -D -u $USER_ID -G docker docker && \  
umask 0027  
RUN mkdir /data && chown docker:docker /data  
VOLUME /data  
WORKDIR /data  
USER $USER_ID  
CMD $USER_ID /usr/bin/weed server -dir=/data -filer -filer.port=8000
-master.port=9333 -volume.port=8001  

