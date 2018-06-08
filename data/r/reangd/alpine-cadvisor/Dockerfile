FROM reangd/alpine-base:latest  
  
ENV CADVISOR_OPTIONS="-logtostderr"  
  
RUN GLIBC_VERSION="2.23-r3" && \  
CADVISOR_VERSION="v0.26.1" && \  
apk add \--no-cache device-mapper findutils zfs thin-provisioning-tools && \  
\  
curl -Ls -o /usr/bin/cadvisor
https://github.com/google/cadvisor/releases/download/${CADVISOR_VERSION}/cadvisor
&& \  
chmod +x /usr/bin/cadvisor && \  
\  
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
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
rm /tmp/*  
  
EXPOSE 8080  
COPY root /  
  

