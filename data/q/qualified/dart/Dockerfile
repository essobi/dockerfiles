FROM buildpack-deps:xenial  
  
ENV DART_VERSION=1.23.0 \  
DART_SDK=/usr/lib/dart \  
PATH=/usr/lib/dart/bin:$PATH  
  
RUN set -ex; \  
apt-get -q update; \  
apt-get install --no-install-recommends -y -q \  
apt-transport-https \  
; \  
curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
-; \  
curl -sS
https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list
> /etc/apt/sources.list.d/dart_stable.list; \  
apt-get -q update; \  
apt-get install -q -y --no-install-recommends dart=${DART_VERSION}-1; \  
rm -rf /var/lib/apt/lists/*;  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
COPY rootfs/workspace/dart /workspace/dart  
RUN chown -R codewarrior:codewarrior /workspace/dart  
  
WORKDIR /workspace  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  
  
RUN set -ex; \  
cd /workspace/dart; \  
pub get;  

