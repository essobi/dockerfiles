FROM alpine:3.5 as downloader  
RUN apk add --no-cache wget tar xz  
  
ENV ALT_IMG_DATE=20180312  
ENV ALT_IMG_ARC=i586  
  
WORKDIR /tmp/  
RUN \  
wget --no-check-certificate --progress=bar:force --output-
document=basealt.tar.xz https://mirror.yandex.ru/altlinux-
starterkits/release/alt-p8-ovz-generic-${ALT_IMG_DATE}-${ALT_IMG_ARC}.tar.xz
&& \  
mkdir -p /alt/ && \  
tar -xJvf /tmp/basealt.tar.xz -C /alt/  
  
FROM scratch  
  
ENV LANG ru_RU.UTF-8  
COPY \--from=downloader /alt/ /  
  
RUN \  
apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get -y install basesystem etcnet apt apt-repo bash && \  
apt-get clean && \  
echo -ne "LANG=ru_RU.UTF-8\nSUPPORTED=ru_RU.UTF-8\n" >/etc/sysconfig/i18n && \  
rm -f /var/cache/apt/archives/*.rpm /var/cache/apt/*.bin
/var/lib/apt/lists/*.*  
  
ENTRYPOINT /bin/bash

