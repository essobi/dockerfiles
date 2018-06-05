FROM alpine:3.4  
MAINTAINER ATSD Developers <dev-atsd@axibase.com>  
  
ENV CADVISOR_VERSION "v0.24.0-alpha1.45+3096281db66ef9"  
ENV GLIBC_VERSION "2.23-r3"  
  
RUN apk --no-cache add ca-certificates wget device-mapper && \  
apk --no-cache add zfs --repository
http://dl-3.alpinelinux.org/alpine/edge/main/ && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \  
wget https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk && \  
apk add glibc-${GLIBC_VERSION}.apk glibc-bin-${GLIBC_VERSION}.apk && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
rm -rf /var/cache/apk/*  
  
# Grab cadvisor from the staging directory.  
RUN wget -O /usr/bin/cadvisor
https://github.com/axibase/cadvisor/releases/download/${CADVISOR_VERSION}/cadvisor
&& \  
chmod +x /usr/bin/cadvisor  
  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/cadvisor", "-logtostderr"]  

