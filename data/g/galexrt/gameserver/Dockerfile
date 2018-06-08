FROM fedora:25  
LABEL maintainer="Alexander Trost <galexrt@googlemail.com>"  
  
ENV DATA_PATH="/data"  
RUN dnf -q upgrade -y && \  
dnf install -y tar curl ca-certificates python glibc.i686 libstdc++.i686 \  
zlib.i686 libcurl.i686 ncurses-libs.i686 && \  
dnf clean all && \  
rm -rf /var/lib/dnf/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/locale/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME ["$DATA_PATH"]  
WORKDIR "$DATA_PATH"  
  
ENTRYPOINT ["/entrypoint.sh"]  

