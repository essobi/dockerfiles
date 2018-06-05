FROM debian:stretch  
MAINTAINER Chris Hardekopf <cjh@ygdrasill.com>  
  
# Install prerequisites  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
wget python libgl1 xz-utils xdg-utils imagemagick dumb-init \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /opt/calibre  
WORKDIR /opt/calibre  
  
# Install calibre  
ENV CALIBRE_VERSION=3.14.0  
RUN wget -O - --quiet
https://github.com/kovidgoyal/calibre/releases/download/v$CALIBRE_VERSION/calibre-$CALIBRE_VERSION-x86_64.txz
\  
| tar xJvf -  
  
# Expose the calibre-server port  
EXPOSE 8080  
# Default library location  
VOLUME ["/calibre"]  
  
# dumb-init, calibre-server  
ENTRYPOINT ["/usr/bin/dumb-init", "--", "./calibre-server"]  
  
# The default arguments enable authentication and expect a user database at  
# /calibre/user.db along with the library at /calibre. You can manage a user  
# database using the "--manage-users" command line argument.  
CMD ["--enable-auth", "--auth-mode=auto", "--userdb=/calibre/user.db",
"/calibre"]  
  

