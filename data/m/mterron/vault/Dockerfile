FROM mterron/consul  
MAINTAINER Miguel Terron <miguel.a.terron@gmail.com>  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG HASHICORP_PGP_KEY=51852D87348FFC4C  
ARG VAULT_VERSION=0.10.2  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/mterron/vault.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0-rc.1" \  
org.label-schema.version=$VAULT_VERSION \  
org.label-schema.description="Vault secure production ready Docker image"  
  
WORKDIR /tmp  
RUN apk -q --no-cache add ca-certificates gnupg wget &&\  
# Download Vault binary & integrity file  
gpg --keyserver pgp.mit.edu --receive-keys "$HASHICORP_PGP_KEY" &&\  
wget -nv --progress=bar:force --show-progress
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
&&\  
wget -nv --progress=bar:force --show-progress
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_SHA256SUMS
&&\  
wget -nv --progress=bar:force --show-progress
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_SHA256SUMS.sig
&&\  
# Install Vault  
gpg --batch --verify vault_${VAULT_VERSION}_SHA256SUMS.sig
vault_${VAULT_VERSION}_SHA256SUMS &&\  
grep "linux_amd64.zip" vault_${VAULT_VERSION}_SHA256SUMS | sha256sum -sc &&\  
unzip -q -o vault_${VAULT_VERSION}_linux_amd64.zip -d /usr/local/bin/ &&\  
setcap 'cap_ipc_lock=+ep' /usr/local/bin/vault &&\  
# Create Vault user & group and add root to the vault group  
addgroup -S vault &&\  
adduser -H -h /tmp -D -S -G vault -g 'Vault user' -s /dev/null -D vault &&\  
addgroup vault consul &&\  
# Cleanup  
apk -q --no-cache del --purge ca-certificates gnupg wget &&\  
rm -rf vault_${VAULT_VERSION}_* /root/.gnupg  
  
# Add Containerpilot  
ARG CONTAINERPILOT_VERSION=3.8.0  
RUN echo -n -e "\e[0;32m- Install Containerpilot\e[0m" &&\  
curl -sSL
"https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz"
| tar xzf - -C /usr/local/bin &&\  
echo -e "#!/bin/sh\ncurl -kisSfi1 --head
https://127.0.0.1:8200/v1/sys/health?standbycode=204 >/dev/null" >
/usr/local/bin/vault-healthcheck &&\  
echo -e "#!/bin/sh\nsu-exec consul curl -s --unix-socket
/data/consul.http.sock http://consul/v1/status/leader|jq -cre 'if . != \"\"
then true else false end'>/dev/null ||exit 1"> /usr/local/bin/consul-
healthcheck &&\  
chown root:root /usr/local/bin/* &&\  
chmod +x /usr/local/bin/* &&\  
echo -e "\e[1;32m ✔\e[0m"  
  
# Copy binaries. bin directory contains start_vault.sh and consul-cli  
COPY bin/ /usr/local/bin  
# Copy /etc (Vault config, Containerpilot config)  
COPY etc/ /etc  
# Copy client certificates  
COPY client_certificate.* /etc/tls/  
  
RUN chown -R vault: /etc/vault &&\  
chmod +x /usr/local/bin/* &&\  
chmod 660 /etc/vault/config.json &&\  
cat /etc/tls/ca.pem >> /etc/ssl/certs/ca-certificates.crt  
  
# Provide your own Vault config file and certificates  
ONBUILD COPY config.json /etc/vault/  
ONBUILD COPY consul.json /etc/consul/  
ONBUILD COPY tls/* /etc/tls/  
ONBUILD COPY client_certificate.* /etc/tls/  
# Fix permissions & add custom certs to the system certicate store  
ONBUILD RUN chown vault:vault /etc/vault/config.json &&\  
chmod 660 /etc/vault/config.json &&\  
cat /etc/tls/ca.pem >> /etc/ssl/certs/ca-certificates.crt  
  
ENV VAULT_CLI_NO_COLOR=1 \  
CONTAINERPILOT=/etc/containerpilot.json5  
  
EXPOSE 8200  
HEALTHCHECK \--start-period=600s CMD set -e && set -o pipefail && vault status
-format=json | jq -ce '.sealed == false'  
  
ENTRYPOINT ["containerpilot"]  
  
COPY Dockerfile /etc/  

