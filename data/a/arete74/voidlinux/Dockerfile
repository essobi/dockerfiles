FROM alpine:latest as builder  
RUN apk --no-cache add ca-certificates  
  
ADD https://repo.voidlinux.eu/static/xbps-static-latest.x86_64-musl.tar.xz
/root/  
RUN tar -Jxvf /root/xbps-static-latest.x86_64-musl.tar.xz -C / && mkdir -p
/root/voidlinux/root /root/voidlinux/cache  
RUN yes|/usr/bin/xbps-install -Syu -R https://repo.voidlinux.eu/current xbps-
triggers coreutils base-files glibc-locales dash grep xbps iana-etc tzdata sed
-r /root/voidlinux/root -c /root/voidlinux/cache  
  
FROM scratch  
WORKDIR /  
COPY \--from=builder root/voidlinux/root/ .  

