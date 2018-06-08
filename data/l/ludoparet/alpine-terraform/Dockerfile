FROM alpine:3.7  
  
ENV TERRAFORM_VERSION "0.11.7"  
  
ARG RUNTIME_DEPS="libintl git"  
ARG BUILD_DEPS="gnupg gettext openssl curl"  
  
RUN apk update && \  
apk upgrade && \  
apk add --no-cache ${RUNTIME_DEPS} && \  
apk add --no-cache --virtual build-dependencies ${BUILD_DEPS} && \  
cp /usr/bin/envsubst /usr/local/bin/envsubst && \  
curl -s https://keybase.io/hashicorp/key.asc | gpg --import && \  
curl -Os
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
curl -Os
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS
&& \  
curl -Os
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS.sig
&& \  
gpg --verify terraform_${TERRAFORM_VERSION}_SHA256SUMS.sig
terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
sed -i "/terraform_${TERRAFORM_VERSION}_linux_amd64.zip/!d"
terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
sha256sum -c terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
chmod +x terraform && \  
mv terraform /usr/local/bin/terraform && \  
apk del build-dependencies && \  
rm -rf terraform_${TERRAFORM_VERSION}_* /var/cache/apk/* /tmp/* && \  
terraform -v  
  
ENTRYPOINT []  

