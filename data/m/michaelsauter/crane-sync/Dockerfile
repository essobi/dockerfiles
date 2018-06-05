FROM alpine:3.6  
MAINTAINER Michael Sauter <mail@michaelsauter.net>  
  
ARG UNISON_VERSION=2.48.4  
# Install in one run so that build tools won't remain in any docker layers  
# Install build tools  
RUN apk add --update build-base curl && \  
# Install ocaml & emacs from testing repositories  
apk add \--update-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ ocaml emacs && \  
# Download & Install Unison  
curl -L https://github.com/bcpierce00/unison/archive/$UNISON_VERSION.tar.gz |
tar zxv -C /tmp && \  
cd /tmp/unison-${UNISON_VERSION} && \  
sed -i -e 's/GLIBC_SUPPORT_INOTIFY 0/GLIBC_SUPPORT_INOTIFY 1/'
src/fsmonitor/linux/inotify_stubs.c && \  
make && \  
cp src/unison src/unison-fsmonitor /usr/local/bin && \  
# Remove build tools  
apk del build-base curl emacs ocaml && \  
# Remove tmp files and caches  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/unison-${UNISON_VERSION}  
  
# These can be overridden later  
ENV TZ="Europe/Berlin" \  
LANG="C.UTF-8" \  
UNISON_DIR="/data" \  
UNISON_UID=0 \  
UNISON_GID=0 \  
HOME="/root"  
ADD bin/sync /usr/local/bin/sync  
RUN chmod 0755 /usr/local/bin/sync  
  
ENTRYPOINT ["sync"]

