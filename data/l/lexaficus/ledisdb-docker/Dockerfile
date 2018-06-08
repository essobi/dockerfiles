FROM golang:1.7.4-alpine  
MAINTAINER Aleksei Pavliukov <alex@implus.co>  
  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apk add --no-cache --virtual .gosu-deps \  
dpkg \  
gnupg \  
openssl \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apk del .gosu-deps  
  
RUN apk --update add ca-certificates curl git make bash autoconf automake g++
libtool libc-dev  
  
ENV GOROOT /usr/local/go  
ENV GOPATH /go  
ENV PATH /go/bin:$PATH  
  
  
RUN addgroup ledisdb && \  
adduser -S -G ledisdb ledisdb  
  
RUN mkdir -p /ledisdb  
WORKDIR /ledisdb  
  
RUN mkdir -p /usr/local/go/src/github.com/siddontang/ledisdb  
RUN git clone https://github.com/siddontang/ledisdb.git
/usr/local/go/src/github.com/siddontang/ledisdb  
RUN curl https://glide.sh/get | sh  
  
#RUN  
ADD build.sh ./  
RUN bash ./build.sh  
  
ADD ledis.conf ./  
  
RUN apk del curl git make bash autoconf automake g++ libtool libc-dev  
RUN rm -r /usr/local/go/*  
RUN mkdir /data  
EXPOSE 6381  
RUN chown ledisdb:ledisdb /data  
ENTRYPOINT ["gosu"]  
CMD ["ledisdb", "./ledis-server", "-config=/ledisdb/ledis.conf"]

