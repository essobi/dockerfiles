FROM debian:stretch  
  
ARG MAKEMKV_VERSION=1.12.0  
ARG PREFIX=/usr/local  
  
# Install MakeMKV dependencies.  
RUN set -ex; \  
buildDeps=' \  
ca-certificates \  
g++ \  
gcc-6 \  
libavcodec-dev \  
libexpat-dev \  
libqt4-dev \  
libssl-dev \  
make \  
pkg-config \  
wget \  
zlib1g-dev \  
'; \  
apt-get update; \  
apt-get install -y --no-install-recommends $buildDeps; \  
\  
echo "Install MakeMKV."; \  
for pkg in makemkv-oss makemkv-bin; do \  
wget -O "${pkg}.tgz"
"http://www.makemkv.com/download/${pkg}-${MAKEMKV_VERSION}.tar.gz"; \  
mkdir -p "${pkg}"; \  
tar -xvf "${pkg}.tgz" -C "${pkg}" \--strip-components=1; \  
rm "${pkg}.tgz"; \  
cd "${pkg}"; \  
if [ -f configure ]; then \  
./configure --prefix="${PREFIX}"; \  
else \  
mkdir -p tmp; \  
touch tmp/eula_accepted; \  
fi; \  
make -j "$(nproc)" PREFIX="${PREFIX}"; \  
make install PREFIX="${PREFIX}"; \  
cd ..; \  
rm -r "${pkg}"; \  
done; \  
\  
echo "Some of the packages are still required"; \  
apt-mark manual \  
libavcodec57 \  
libqtdbus4 \  
libqtgui4 \  
libssl1.1 \  
; \  
\  
echo "Purge the dependencies"; \  
apt-get purge -y --auto-remove $buildDeps; \  
echo "Install a few other required binaries"; \  
apt-get install -y \  
ca-certificates-java \  
openjdk-8-jre-headless \  
python \  
python-requests; \  
\  
echo "Purge the apt cache"; \  
rm -rf /var/lib/apt/lists/*;  
  
RUN mkdir -p ~/.MakeMKV  
  
COPY bin/entrypoint.sh /entrypoint.sh  
COPY entrypoint.d/ /entrypoint.d/  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["makemkvcon"]  
  
# Metadata  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL maintainer="Dave Lasley <dave@dlasley.net>" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="MakeMKV" \  
org.label-schema.description="Provides MakeMKV CLI in Docker." \  
org.label-schema.url="https://hub.docker.com/r/lasley/makemkvcon/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/lasley/docker-makemkvcon" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  

