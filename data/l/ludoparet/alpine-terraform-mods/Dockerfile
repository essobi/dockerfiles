FROM alpine:3.7  
ENV TERRAFORM_VERSION "0.11.7"  
ENV TF_PLUGIN_CACHE_DIR "/mods"  
ARG RUNTIME_DEPS="libintl git"  
ARG BUILD_DEPS="gnupg gettext go gcc musl-dev openssl curl"  
ARG GO_PATH="/go"  
COPY ./main.tf /tmp/main.tf  
COPY ./terraformrc /root/.terraformrc  
  
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
export GOPATH=${GO_PATH} && \  
export PATH=${GOPATH}/bin:${PATH} && \  
mkdir -p ${GOPATH}/src ${GOPATH}/bin ${TF_PLUGIN_CACHE_DIR}/linux_amd64 && \  
go get -u github.com/golang/dep/cmd/dep github.com/vmware/terraform-provider-
vra7 && \  
cd ${GOPATH}/src/github.com/vmware/terraform-provider-vra7 && \  
dep ensure && \  
go build -o ${TF_PLUGIN_CACHE_DIR}/linux_amd64/terraform-provider-vra7 && \  
cd /tmp && \  
terraform init && \  
apk del build-dependencies && \  
rm -rf /terraform_${TERRAFORM_VERSION}_* /var/cache/apk/* /tmp/* ${GOPATH} &&
\  
terraform -v  
  
ENTRYPOINT []  

