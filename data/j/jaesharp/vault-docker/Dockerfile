FROM alpine:3.3  
MAINTAINER J Lynn <Justin.Lynn@cba.com.au>  
  
ENV VAULT_VERSION 0.5.1  
ENV VAULT_REL_ENV linux_amd64  
  
ENV VAULT_TMP /tmp/vault-install  
ENV GNUPGHOME ${VAULT_TMP}/gpg  
ENV VAULT_PUBKEY ${GNUPGHOME}/vault_release.pubkey.asc  
ENV VAULT_CSUM ${VAULT_TMP}/vault.sha256sum  
ENV VAULT_CSUMSIG ${VAULT_CSUM}.sig  
ENV VAULT_DWNLDED_CSUM ${VAULT_CSUM}.downloaded  
ENV VAULT_DWNLDED ${VAULT_TMP}/vault_${VAULT_VERSION}_${VAULT_REL_ENV}.zip  
  
ENV VAULT_HOME /usr/local/bin  
ENV PATH $PATH:${VAULT_HOME}  
  
# Note that this creates ${VAULT_TMP} implicitly  
ADD keyring/hashicorp.security.releases.pubkey.asc ${VAULT_PUBKEY}  
  
# The --no-check-certificate flag is fine here because we're verifying the
signature of the SHA256sums file  
# with a known, static, GPG key inclued in the /keyring directory of this
repository. We need to support  
# building this image behind http(s) proxies which MITM and rewrite
certificate without modifying the  
# base image. Typically, we would just download via HTTP but it appears
hashicorp only publish via HTTPS (good  
# on them).  
RUN apk --no-cache add \  
bash \  
ca-certificates \  
wget \  
gnupg &&\  
wget --quiet --output-document=${VAULT_CSUM} \--no-check-certificate
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_SHA256SUMS
&&\  
wget --quiet --output-document=${VAULT_CSUMSIG} \--no-check-certificate
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_SHA256SUMS.sig
&&\  
chmod 700 ${GNUPGHOME} &&\  
gpg --quiet --import ${VAULT_PUBKEY} &&\  
gpg --quiet --verify ${VAULT_CSUMSIG} ${VAULT_CSUM} &&\  
wget --quiet --output-document=${VAULT_DWNLDED} \--no-check-certificate
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_${VAULT_REL_ENV}.zip
&&\  
cat ${VAULT_CSUM} | grep ${VAULT_REL_ENV} > ${VAULT_DWNLDED_CSUM} &&\  
bash -c "cd ${VAULT_TMP} && sha256sum -c ${VAULT_DWNLDED_CSUM}" &&\  
unzip ${VAULT_DWNLDED} -d ${VAULT_HOME} &&\  
rm -rf ${VAULT_TMP} &&\  
apk --purge del \  
gnupg  
  
EXPOSE 8200  
ADD etc/vault/* /etc/vault/  
  
VOLUME /vaultdb  
  
ENTRYPOINT ["/usr/local/bin/vault"]  
CMD ["server", "-config", "/etc/vault/dev.hcl"]  

