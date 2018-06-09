FROM dockercore/opensuse:12.3  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
# install dependencies  
RUN zypper -n in ca-certificates* curl git gzip rpm-build &&\  
zypper -n in libbtrfs-devel device-mapper-devel glibc-static libselinux-devel
selinux-policy selinux-policy-devel sqlite-devel tar  
  
# install go  
ENV GO_VERSION 1.6.3  
RUN curl -fSL "https://storage.googleapis.com/golang/go${GO_VERSION}.linux-
amd64.tar.gz" | tar xzC /usr/local  
ENV PATH $PATH:/usr/local/go/bin  
  
COPY build.sh /build.sh  
  
CMD ["/build.sh"]  

