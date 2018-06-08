FROM pinterb/base:alpine  
  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
# This is the release of Terraform to pull in.  
LABEL vendor="HashiCorp" \  
com.hashicorp.terraform.version="0.9.4" \  
com.hashicorp.terraform.release-date="2017-04-26"  
  
ENV TERRAFORM_VERSION 0.9.4  
ENV GLIBC_PKG_VERSION 2.25-r0  
ENV PUID 1000  
ENV PGID 1000  
RUN apk add --no-cache --update-cache ca-certificates unzip bash sudo graphviz
&& \  
curl -Lo /etc/apk/keys/sgerrand.rsa.pub "https://github.com/sgerrand/alpine-
pkg-glibc/releases/download/${GLIBC_PKG_VERSION}/sgerrand.rsa.pub" && \  
curl -Lo glibc-${GLIBC_PKG_VERSION}.apk "https://github.com/sgerrand/alpine-
pkg-
glibc/releases/download/${GLIBC_PKG_VERSION}/glibc-${GLIBC_PKG_VERSION}.apk"
&& \  
curl -Lo glibc-bin-${GLIBC_PKG_VERSION}.apk
"https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_PKG_VERSION}/glibc-
bin-${GLIBC_PKG_VERSION}.apk" && \  
curl -Lo glibc-i18n-${GLIBC_PKG_VERSION}.apk
"https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_PKG_VERSION}/glibc-i18n-${GLIBC_PKG_VERSION}.apk"
&& \  
apk add glibc-${GLIBC_PKG_VERSION}.apk glibc-bin-${GLIBC_PKG_VERSION}.apk
glibc-i18n-${GLIBC_PKG_VERSION}.apk && \  
curl -Lo /terraform.zip
"https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip"
&& \  
unzip /terraform.zip -d /bin && \  
apk del --purge curl ca-certificates unzip && \  
rm -rf /var/cache/apk/* glibc-${GLIBC_PKG_VERSION}.apk /terraform.zip  
  
# create dev user  
RUN addgroup -g $PGID dev && \  
adduser -h /config -u $PUID -H -D -G dev -s /bin/bash dev && \  
sed -ri 's/(wheel:x:10:root)/\1,dev/' /etc/group && \  
sed -ri 's/# %wheel ALL=\\(ALL\\) NOPASSWD: ALL/%wheel ALL=\\(ALL\\) NOPASSWD:
ALL/' /etc/sudoers  
  
# Create a shared data volume  
# We need to create an empty file, otherwise the volume will  
# belong to root.  
RUN mkdir /data/ /ops/ /state/  
RUN touch /data/.extra /ops/.extra /state/.extra  
RUN chown -R dev:dev /data  
RUN chown -R dev:dev /ops  
RUN chown -R dev:dev /state  
  
## Expose some volumes  
VOLUME ["/data", "/ops", "/state"]  
WORKDIR /data  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["--help"]  

