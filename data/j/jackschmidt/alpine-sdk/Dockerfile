FROM arm32v6/alpine:edge  
RUN sed -i 's/v3.6/edge/' /etc/apk/repositories && \  
apk add -U -u --purge \  
alpine-base \  
alpine-conf \  
alpine-sdk \  
apk-tools \  
autoconf \  
automake \  
build-base \  
busybox \  
diffutils \  
git \  
fakeroot \  
grub-efi \  
linux-headers \  
linux-rpi2 \  
musl \  
ncurses-dev \  
rsync \  
squashfs-tools \  
vimdiff \  
xorriso \  
; true  
RUN addgroup root abuild ; \  
mkdir -p -m 755 /root/.abuild ; \  
adduser abuild -G abuild -D -s /bin/ash ; \  
mkdir -m 755 -p ~abuild/.abuild ; \  
chown abuild.abuild -R ~abuild  
CMD ["/bin/sh"]  
ARG BUILD_DATE  
ARG SOURCE_TAG  
ARG SOURCE_COMMIT  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Alpine SDK" \  
org.label-schema.description="A Docker image for building static binaries
using Alpine SDK" \  
org.label-schema.vcs-ref=$SOURCE_COMMIT \  
org.label-schema.vcs-url="https://github.com/jackschmidt/docker-alpine-sdk" \  
org.label-schema.version=$SOURCE_TAG \  
org.label-schema.schema-version="1.0"  

