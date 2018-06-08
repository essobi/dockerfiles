FROM alpine:3.4  
RUN apk update && apk add curl  
  
# This is the release of https://github.com/hashicorp/docker-base to pull in
order  
# to provide HashiCorp-built versions of basic utilities like dumb-init and
gosu.  
ENV DOCKER_BASE_VERSION=0.0.4  
# Set up certificates, our base tools.  
RUN apk add --no-cache ca-certificates gnupg openssl && \  
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
apk del gnupg openssl && \  
rm -rf /root/.gnupg  
  
COPY ./swarm /usr/local/bin/swarm  
COPY ./certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt  
  
ENV SWARM_HOST :2375  
ENV SWARM_ADVERTISE_PORT 2375  
EXPOSE 2375  
EXPOSE 4000  
VOLUME /.swarm  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["help"]  

