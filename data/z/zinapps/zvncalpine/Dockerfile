FROM alpine  
MAINTAINER Sarfaraz Ali Khan <mrkhan1417@gmail.com>  
  
# Here we install GNU libc (aka glibc) and set C.UTF-8 locale as default.  
RUN ALPINE_GLIBC_BASE_URL="https://github.com/andyshinn/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.23-r3" && \  
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
apk add \--no-cache \--virtual=build-dependencies wget ca-certificates && \  
wget \  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
&& \  
apk add \--no-cache --allow-untrusted \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
\  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
\  
apk del glibc-i18n && \  
\  
apk del build-dependencies && \  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
ENV LANG=C.UTF-8  
  
RUN apk --no-cache add alpine-desktop xfce4 thunar-volman faenza-icon-theme
slim  
RUN apk --no-cache add wget xvfb linux-pam  
  
RUN TIGERVNC_VERSION=1.6.0 && \  
TIGERVNC_URL="https://bintray.com/artifact/download/tigervnc/stable" && \  
TIGERVNC_FILENAME=tigervnc-Linux-x86_64-$TIGERVNC_VERSION.tar.gz && \  
wget \  
"$TIGERVNC_URL/$TIGERVNC_FILENAME" && \  
tar zxf $TIGERVNC_FILENAME ./usr -C / && \  
rm $TIGERVNC_FILENAME  
  
COPY start.sh /opt/start.sh  
RUN chmod +x /opt/start.sh  
ENV DISPLAY :0  
ENV PASSWD changeme  
EXPOSE 5901  
CMD ["/opt/start.sh"]  

