FROM pinterb/base:alpine  
  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
ENV PACKER_VERSION 0.8.6  
ENV GLIBC_PKG_VERSION 2.23-r3  
  
RUN apk add --no-cache --update-cache ca-certificates wget gzip unzip bash
sudo openssh-client graphviz && \  
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
glibc-i18n-${GLIBC_PKG_VERSION}.apk  
  
RUN wget -q -O /packer.zip
"https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip"
&& \  
unzip /packer.zip -d /bin && \  
wget -q -O /bin/azure.tar.gz "https://github.com/Azure/packer-
azure/releases/download/prerelease/packer-azure-linux-amd64-prerelease.tar.gz"
&& \  
gunzip /bin/azure.tar.gz && \  
tar -xvf /bin/azure.tar -C /bin && \  
apk del --purge wget ca-certificates unzip gzip && \  
rm -rf /var/cache/apk/* glibc-${GLIBC_PKG_VERSION}.apk /packer.zip
/bin/azure.tar  
  
RUN addgroup dev && \  
adduser -G dev dev -D -h /home/dev && \  
mkdir -p /home/dev/bin /home/dev/lib /home/dev/include /home/dev/.ssh && \  
sed -ri 's/(wheel:x:10:root)/\1,dev/' /etc/group && \  
sed -ri 's/# %wheel ALL=\\(ALL\\) NOPASSWD: ALL/%wheel ALL=\\(ALL\\) NOPASSWD:
ALL/' /etc/sudoers  
  
ENV PATH /home/dev/bin:$PATH  
  
RUN ssh-keygen -t rsa -N '' -f /home/dev/.ssh/dummy_rsa && \  
chown -R dev:dev /home/dev/.ssh  
  
# Create a shared data volume  
# We need to create an empty file, otherwise the volume will  
# belong to root.  
RUN mkdir /data/ /ansible/ /state/  
RUN touch /data/.extra /ansible/.extra /state/.extra  
RUN chown -R dev:dev /data  
RUN chown -R dev:dev /ansible  
RUN chown -R dev:dev /state  
  
## Expose some volumes  
VOLUME ["/data", "/ansible", "/state", "/home/dev/.ssh"]  
  
ENV HOME /home/dev  
USER dev  
WORKDIR /data  
  
ENTRYPOINT ["/bin/packer"]  
CMD ["--help"]  

