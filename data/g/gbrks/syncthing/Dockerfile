FROM alpine:latest  
MAINTAINER Gavin Brooks <gavin@brks.io>  
  
ENV VERSION v0.13.7  
ENV RELEASE syncthing-linux-amd64-$VERSION  
  
# Add user to run syncthing as, must exist on host and have access to files  
RUN adduser -D -u 1000 syncthing users  
  
# Add dependencies  
RUN apk add --update ca-certificates wget && \  
  
# Add glibc  
# wget "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk" && \  
# apk add --allow-untrusted glibc-2.21-r2.apk && \  
wget --no-check-certificate -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget --no-check-certificate https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk && \  
apk add glibc-2.23-r3.apk && \  
  
# Download from release from Github  
wget --no-check-certificate -O /$RELEASE.tar.gz \  
https://github.com/syncthing/syncthing/releases/download/$VERSION/$RELEASE.tar.gz
&& \  
tar zxf /$RELEASE.tar.gz -C /usr/local && \  
ln -s /usr/local/$RELEASE/syncthing /usr/local/bin && \  
  
# Modify ownership to permit syncthing updating via a userspace run binary  
chown -R syncthing:syncthing /usr/local/$RELEASE/ && \  
chown -R syncthing:syncthing /usr/local/bin && \  
  
  
# Clean up  
rm /$RELEASE.tar.gz && \  
rm -rf /var/cache/apk/*  
  
VOLUME /config  
  
EXPOSE 8384 22000 21025/udp  
  
USER syncthing  
  
CMD ["-no-browser", "-no-restart", "-gui-address=0.0.0.0:8384",
"-home=/config"]  
  
ENTRYPOINT ["/usr/local/bin/syncthing"]  

