FROM alpine:3.3  
MAINTAINER Anders Brujordet  
  
ENV LC_ALL="en_US.UTF-8" \  
LANG="en_US.UTF-8" \  
LANGUAGE="en_US.UTF-8"  
ADD "https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64"
/usr/local/bin/gosu  
COPY bashrc /root/.bashrc  
COPY runner /usr/local/bin/runner  
COPY installer /usr/local/bin/installer  
  
RUN apk -U add bash && \  
chmod +x /usr/local/bin/gosu && \  
mkdir /opt /build && \  
ln -sfn /bin/bash /bin/sh && \  
echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
installer -c apk "shadow@testing"  
  
VOLUME /config /data  
  
ENTRYPOINT [ "/usr/local/bin/runner" ]  
  
CMD [ "bash" ]  

