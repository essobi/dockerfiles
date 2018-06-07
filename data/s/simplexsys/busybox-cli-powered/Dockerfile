FROM progrium/busybox  
MAINTAINER qsys <kurt.sys@gmail.com>  
  
RUN opkg-install curl bash ca-certificates  
RUN for cert in `ls -1 /etc/ssl/certs/*.crt | grep -v /etc/ssl/certs/ca-
certificates.crt`; do cat "$cert" >> /etc/ssl/certs/ca-certificates.crt; done  

