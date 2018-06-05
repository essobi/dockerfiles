FROM alpine:3.2  
# can not derive from google/cadvisor directly,  
# because it's not an alpine image as claimed in this Dockerfile  
# https://github.com/google/cadvisor/blob/master/deploy/Dockerfile  
MAINTAINER erhankesken@gmail.com  
  
ENV GOPATH=/usr/local/lib/go  
ENV CADVISOR_PATH=$GOPATH/src/github.com/google/cadvisor  
ADD . $CADVISOR_PATH  
  
# from https://github.com/google/cadvisor/blob/master/deploy/Dockerfile  
RUN apk add --update ca-certificates device-mapper && \  
wget https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/8/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk && \  
wget https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/8/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-
bin-2.21-r2.apk && \  
apk add --allow-untrusted glibc-2.21-r2.apk glibc-bin-2.21-r2.apk && \  
apk add zfs-utils --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \  
/usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
rm -rf /var/cache/apk/*  
  
RUN apk add --update alpine-sdk go linux-headers && \  
go get github.com/tools/godep && \  
ln -s $GOPATH/bin/godep /usr/local/bin/godep && \  
cd $CADVISOR_PATH && \  
godep go build . && \  
apk del alpine-sdk go linux-headers && \  
rm -rf /var/cache/apk/*  
RUN ln -s $CADVISOR_PATH/cadvisor /usr/local/bin/cadvisor  
  
EXPOSE 8080  
CMD ["/usr/local/bin/cadvisor", "-logtostderr"]  
  

