FROM alpine:latest  
  
# We can use ENV or ARG to define version variables, but the best-practices  
# doc suggests using ENV for this purpose.  
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/#env  
ENV REMGLK_TAG="remglk-0.2.6" \  
LIBFIZMO_TAG="libfizmo_0-7-14" \  
LIBGLKIF_TAG="libglkif_0-2-3" \  
FIZMO_REMGLK_TAG="fizmo-remglk_0-1-2"  
LABEL maintainer="jaredreisinger@hotmail.com" \  
remglk.tag="${REMGLK_TAG}" \  
libfizmo.tag="${LIBFIZMO_TAG}" \  
libglkif.tag="${LIBGLKIF_TAG}" \  
fizmo-remglk.tag="${FIZMO_REMGLK_TAG}"  
  
COPY *.patch /tmp/patches/  
  
RUN apk add --no-cache ca-certificates  
  
RUN set -eux; \  
echo "============================================================"; \  
echo "acquire tools..."; \  
echo "============================================================"; \  
apk add --no-cache --virtual .build-deps \  
autoconf \  
automake \  
gcc \  
git \  
make \  
musl-dev \  
; \  
# libxml2-dev is separate, because the shared library needs to stick  
# around for running fizmo-remglk.  
apk add \--no-cache \  
libxml2-dev \  
; \  
echo "============================================================"; \  
echo "acquire sources..."; \  
echo "============================================================"; \  
mkdir -p /tmp; \  
cd /tmp; \  
git clone \--depth 1 --branch "${REMGLK_TAG}"
https://github.com/erkyrath/remglk; \  
git clone \--depth 1 --branch "${LIBFIZMO_TAG}"
https://github.com/chrender/libfizmo.git; \  
git clone \--depth 1 --branch "${LIBGLKIF_TAG}"
https://github.com/chrender/libglkif.git; \  
git clone \--depth 1 --branch "${FIZMO_REMGLK_TAG}"
https://github.com/chrender/fizmo-remglk.git; \  
echo "apply patches..."; \  
for p in /tmp/patches/*.patch; do \  
if [ -f "$p" ]; then \  
base=$(basename "$p" .patch); \  
dir=$(echo "$base" | sed -e 's/^\\(.*\\)\\.[0-9]*$/\1/'); \  
cd "$dir"; \  
patch -p 1 -i "$p"; \  
cd ..; \  
fi; \  
done; \  
echo "============================================================"; \  
echo "build..."; \  
echo "============================================================"; \  
echo "------------------------------------------------------------"; \  
echo "remglk"; \  
echo "------------------------------------------------------------"; \  
cd /tmp/remglk; \  
make; \  
cp lib*.a /usr/local/lib/.; \  
mkdir -p /usr/local/include; \  
cp *.h /usr/local/include/.; \  
echo "------------------------------------------------------------"; \  
echo "libfizmo"; \  
echo "------------------------------------------------------------"; \  
cd /tmp/libfizmo; \  
autoreconf --force --install; \  
./configure \  
\--disable-filelist \  
\--disable-command-history \  
\--disable-output-history \  
\--disable-config-files \  
\--disable-prefix-commands \  
; \  
make install-dev; \  
echo "------------------------------------------------------------"; \  
echo "libglkif"; \  
echo "------------------------------------------------------------"; \  
cd /tmp/libglkif; \  
autoreconf --force --install; \  
./configure; \  
make install-dev; \  
echo "------------------------------------------------------------"; \  
echo "fizmo-remglk"; \  
echo "------------------------------------------------------------"; \  
cd /tmp/fizmo-remglk; \  
autoreconf --force --install; \  
./configure; \  
# ./configure LDFLAGS=-static; \  
make install; \  
echo "============================================================"; \  
echo "cleanup"; \  
echo "============================================================"; \  
cd /tmp; \  
echo "remove patches/build files..."; \  
apk del .build-deps; \  
rm -rf /tmp/*; \  
echo "set up games directory"; \  
mkdir -p /usr/local/games; \  
echo "============================================================"; \  
echo "DONE"  
  
COPY play /usr/local/bin/.  
  
VOLUME /usr/local/games  
WORKDIR /usr/local/games  

