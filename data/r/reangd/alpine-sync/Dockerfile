FROM reangd/alpine-base:latest  
  
  
RUN GLIBC_VERSION="2.23-r3" && \  
curl -Ls -o /etc/apk/keys/sgerrand.rsa.pub https://github.com/sgerrand/alpine-
pkg-glibc/releases/download/2.23-r3/sgerrand.rsa.pub && \  
curl -Ls -o /tmp/glibc-${GLIBC_VERSION}.apk
https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \  
curl -Ls -o /tmp/glibc-bin-${GLIBC_VERSION}.apk
https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk && \  
apk add \--no-cache /tmp/glibc-${GLIBC_VERSION}.apk /tmp/glibc-
bin-${GLIBC_VERSION}.apk && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \  
rm /tmp/* && \  
\  
curl -sSL https://download-cdn.resilio.com/stable/linux-x64/resilio-
sync_x64.tar.gz | tar xz -C /usr/bin/ && \  
rm /usr/bin/LICENSE.TXT  
  
  
EXPOSE 80  
COPY root /  
VOLUME ["/storage"]  

