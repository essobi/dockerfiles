FROM centos:7.4.1708 as builder  
  
# Whitespace separated list of RPMs to install:  
ARG \  
PACKAGES=yum  
  
ENV \  
LANG='C' \  
LANGUAGE='C' \  
LC_ALL='C'  
COPY yum.conf /etc  
  
RUN mkdir -p /target  
RUN rpm --root /target --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7  
RUN yum --installroot=/target --releasever=/ install ${PACKAGES}  
# ./bin/image_size: 169 MB  
RUN rm -rf
/target/usr/{{lib,share}/locale,{lib,lib64}/gconv,bin/localedef,sbin/build-
locale-archive}  
RUN rm -rf /target/usr/share/{man,doc,info,gnome/help}  
RUN rm -rf /target/usr/share/cracklib  
RUN rm -rf /target/usr/share/i18n  
RUN rm -rf /target/var/cache/yum  
RUN mkdir -p --mode=0755 /target/var/cache/yum  
RUN rm -rf /target/sbin/sln  
RUN rm -rf /target/etc/ld.so.cache /target/var/cache/ldconfig  
RUN mkdir -p --mode=0755 /target/var/cache/ldconfig  
RUN cp -a {,/target}/etc/yum.conf  
# ./bin/image_size: 95 MB  
FROM scratch  
  
MAINTAINER Ergomentum <build@ergomentum.org>  
  
LABEL \  
vendor="Ergomentum" \  
license="Apache 2.0"  
  
ENV \  
LANG='C' \  
LANGUAGE='C' \  
LC_ALL='C'  
COPY \  
\--from=builder /target .  
  
CMD \  
["bash"]  

