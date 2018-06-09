FROM alpine:3.4  
MAINTAINER Hans J Schroeder <hs@cloudno.de> (@cloudno_de)  
  
# This is the release of Standardfile to pull in.  
ENV STANDARDFILE_VERSION=0.1.1  
# This is the release of https://github.com/hashicorp/docker-base to pull in
order  
# to provide HashiCorp-built versions of basic utilities like dumb-init and
gosu.  
ENV DOCKER_BASE_VERSION=0.0.4  
# Create a stdfile user and group first so the IDs get set the same way,  
# even as the rest of this may change over time.  
RUN addgroup stdfile && \  
adduser -S -G stdfile stdfile  
  
# Set up certificates, our base tools, and Standardfile.  
RUN apk add --no-cache ca-certificates gnupg openssl libcap jq && \  
gpg --recv-keys 91A6E7F85D05C65630BEF18951852D87348FFC4C && \  
mkdir -p /tmp/build && \  
cd /tmp/build && \  
wget https://releases.hashicorp.com/docker-base/${DOCKER_BASE_VERSION}/docker-
base_${DOCKER_BASE_VERSION}_linux_amd64.zip && \  
wget https://releases.hashicorp.com/docker-base/${DOCKER_BASE_VERSION}/docker-
base_${DOCKER_BASE_VERSION}_SHA256SUMS && \  
wget https://releases.hashicorp.com/docker-base/${DOCKER_BASE_VERSION}/docker-
base_${DOCKER_BASE_VERSION}_SHA256SUMS.sig && \  
gpg --batch --verify docker-base_${DOCKER_BASE_VERSION}_SHA256SUMS.sig docker-
base_${DOCKER_BASE_VERSION}_SHA256SUMS && \  
grep ${DOCKER_BASE_VERSION}_linux_amd64.zip docker-
base_${DOCKER_BASE_VERSION}_SHA256SUMS | sha256sum -c && \  
unzip docker-base_${DOCKER_BASE_VERSION}_linux_amd64.zip && \  
cp bin/gosu bin/dumb-init /bin && \  
gpg --recv-keys f907e8bdeef20735b8b50c139eab9fc5e745bc63 && \  
wget
https://github.com/dvbportal/standardfile/releases/download/${STANDARDFILE_VERSION}/standardfile-${STANDARDFILE_VERSION}-linux-
amd64.zip && \  
wget
https://github.com/dvbportal/standardfile/releases/download/${STANDARDFILE_VERSION}/standardfile-${STANDARDFILE_VERSION}-linux-
amd64.zip.sig && \  
gpg --batch --verify standardfile-${STANDARDFILE_VERSION}-linux-amd64.zip.sig
standardfile-${STANDARDFILE_VERSION}-linux-amd64.zip && \  
unzip -d /bin standardfile-${STANDARDFILE_VERSION}-linux-amd64.zip && \  
cd /tmp && \  
rm -rf /tmp/build && \  
apk del gnupg openssl && \  
rm -rf /root/.gnupg  
  
# /stdfile/logs is made available to use as a location to store logs  
RUN mkdir -p /stdfile/logs && \  
mkdir -p /stdfile/db && \  
chown -R stdfile:stdfile /stdfile  
  
# Expose the logs directory as a volume since there's potentially long-running  
# state in there  
VOLUME /stdfile/logs  
  
# Expose the db directory as a volume since there's potentially long-running  
# state in there  
VOLUME /stdfile/db  
  
# 8888/tcp is the primary interface that applications use to interact with  
# standardfile.  
EXPOSE 8888  
# The entry point script uses dumb-init as the top-level process to reap any  
# zombie processes created by Vault sub-processes.  
#  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
WORKDIR /stdfile/logs  
CMD ["standardfile", "'-db /stdfile/db/sf.db'"]  

