FROM resin/armhf-alpine  
LABEL maintainer="Felix Krull"  
RUN ["cross-build-start"]  
  
EXPOSE 22 3000  
RUN apk --no-cache add \  
su-exec \  
ca-certificates \  
sqlite \  
bash \  
git \  
linux-pam \  
s6 \  
curl \  
openssh \  
gettext \  
tzdata  
RUN addgroup \  
-S -g 1000 \  
git && \  
adduser \  
-S -H -D \  
-h /data/git \  
-s /bin/bash \  
-u 1000 \  
-G git \  
git && \  
echo "git:$(dd if=/dev/urandom bs=24 count=1 status=none | base64)" | chpasswd  
  
ENV USER git  
ENV GITEA_CUSTOM /data/gitea  
ENV GODEBUG=netdns=go  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["/usr/bin/entrypoint"]  
CMD ["/bin/s6-svscan", "/etc/s6"]  
  
COPY docker /  
ARG RELEASE=1.3.3  
ARG ARCH=arm-6  
ADD https://github.com/go-
gitea/gitea/releases/download/v${RELEASE}/gitea-${RELEASE}-linux-${ARCH}
/app/gitea/gitea  
RUN chmod 0755 /app/gitea/gitea  
  
RUN ["cross-build-end"]  

