FROM overview/overview-convert-framework:0.0.15 as framework  
  
  
FROM alpine:3.7 AS os  
RUN apk add --update --no-cache ca-certificates  
  
FROM alpine:3.7 AS test-base  
RUN apk add --update --no-cache bats  
WORKDIR /app  
  
# alpine's gmime+json-glib packages don't have static variants. We'll need  
# to compile them ourselves. (Debian doesn't have json-glib, either, and it  
# uses glibc, which shouldn't be statically linked.)  
FROM alpine:3.7 AS build  
RUN \  
apk add --update --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \  
gnu-libiconv \  
gnu-libiconv-dev \  
&& apk add --update --no-cache \  
ca-certificates \  
curl \  
bash \  
meson \  
glib-dev \  
glib-static \  
libidn-dev \  
musl-dev \  
util-linux-dev \  
gcc \  
make \  
tar \  
xz \  
&& mkdir -p /build && cd /build \  
&& curl -o - --location
https://download.gnome.org/sources/gmime/3.2/gmime-3.2.0.tar.xz | tar -Jx \  
&& cd gmime-* \  
&& ./configure && make -j4 install \  
&& cd /build \  
&& curl -o - --location https://download.gnome.org/sources/json-glib/1.4/json-
glib-1.4.2.tar.xz | tar -Jx \  
&& cd json-glib-* \  
&& sed -ie 's/json_lib = library/json_lib = static_library/' json-
glib/meson.build \  
&& ./configure && make install  
WORKDIR /build/convert-email  
COPY Makefile Makefile  
COPY src/ src/  
RUN make  
  
FROM os AS base  
WORKDIR /app  
COPY \--from=framework /app/run /app/  
COPY \--from=framework /app/convert-stream-to-mime-multipart /app/convert  
COPY \--from=build /build/convert-email/do-convert-stream-to-mime-multipart
/app/  
CMD [ "/app/run" ]  
  
FROM base AS dev  
  
  
# The "test" image is special: we integration-test on Docker Hub by actually  
# _running_ the tests as part of the build.  
FROM test-base AS test  
COPY \--from=framework /app/convert-stream-to-mime-multipart /app/convert  
COPY \--from=build /build/convert-email/do-convert-stream-to-mime-multipart
/app/  
COPY /test/ /app/test/  
RUN ./test/suite.bats  
CMD [ "true" ]  
  
FROM base AS production  

