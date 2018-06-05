FROM bytesized/base  
MAINTAINER maran@bytesized-hosting.com  
  
ENV VERSION v0.14.6  
ENV RELEASE syncthing-linux-amd64-$VERSION  
  
RUN apk add --update ca-certificates wget && wget --no-check-certificate -O
/etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && wget --no-check-certificate
https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk  
RUN apk add glibc-2.23-r3.apk  
RUN wget --no-check-certificate -O /$RELEASE.tar.gz
https://github.com/syncthing/syncthing/releases/download/$VERSION/$RELEASE.tar.gz
&& \  
tar zxf /$RELEASE.tar.gz -C /usr/local && \  
ln -s /usr/local/$RELEASE/syncthing /usr/local/bin  
  
RUN chown -R bytesized /usr/local/$RELEASE/ && chown -R bytesized
/usr/local/bin  
RUN rm /$RELEASE.tar.gz && rm -rf /var/cache/apk/*  
  
COPY static/ /  
  
VOLUME /config /data /media  
  
EXPOSE 8384 22000 21025/udp  

