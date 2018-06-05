FROM seansummers/alpine-apk-static:3.4  
MAINTAINER seansummers@gmail.com  
RUN [ "/sbin/apk.static", "add", "-u", "--no-cache", "busybox" ]  
ENV MILLER_VERSION v4.0.0  
RUN /sbin/apk.static add -u --no-cache --virtual .build-deps \  
git gcc libc-dev make autoconf automake libtool gawk flex file diffutils \  
&& mkdir -p /usr/src && cd /usr/src \  
&& git clone --depth 1 \--branch ${MILLER_VERSION}
https://github.com/johnkerl/miller.git \  
&& cd /usr/src/miller \  
&& autoreconf -fiv && ./configure --prefix=/usr/local \  
&& cd /usr/src/miller \  
&& sed -i 's/ -pg / /' c/Makefile.in \  
&& make && make check && make install \  
&& rm -rf /usr/src \  
&& /sbin/apk.static del .build-deps  
ENTRYPOINT [ "/usr/local/bin/mlr" ]  

