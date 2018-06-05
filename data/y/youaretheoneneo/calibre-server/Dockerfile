FROM alpine  
  
MAINTAINER YouAreTheOneNeo <contact@youaretheoneneo.com>  
  
ENV GLIBC_VERSION 2.26-r0  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/opt/calibre/lib  
ENV PATH $PATH:/opt/calibre/bin  
ENV CALIBRE_INSTALLER_SOURCE_CODE_URL
https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-
installer.py  
  
# Download and install glibc  
RUN apk add --update curl && \  
curl -Lo /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
curl -Lo glibc.apk "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" && \  
curl -Lo glibc-bin.apk "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk" && \  
apk add glibc-bin.apk glibc.apk && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
apk del curl && \  
rm -rf glibc.apk glibc-bin.apk /var/cache/apk/*  
  
# Download and install calibre and dependencies  
RUN apk update && \  
apk add --no-cache --upgrade \  
bash \  
ca-certificates \  
gcc \  
mesa-gl \  
python \  
qt5-qtbase-x11 \  
wget \  
xdg-utils \  
xz && \  
wget -O- ${CALIBRE_INSTALLER_SOURCE_CODE_URL} | python -c "import sys;
main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read());
main(install_dir='/opt', isolated=True)" && \  
rm -rf /tmp/calibre-installer-cache && \  
mkdir /config  
  
# Volumes and ports  
  
VOLUME /config  
  
EXPOSE 8080  
  
# Run calibre server  
  
CMD ["/opt/calibre/calibre-server","\--enable-local-write","/config"]  

