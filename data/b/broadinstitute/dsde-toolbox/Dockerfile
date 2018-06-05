FROM alpine:3.3  
ENV VAULT_VERSION=0.6.5 \  
CONSUL_TEMPLATE_VERSION=0.12.0 \  
CLOUDSDK_PYTHON_SITEPACKAGES=1 \  
VAULT_ADDR='https://clotho.broadinstitute.org:8200'  
COPY binary2string.sh create-token.sh mysql-connect.sh render-templates.sh
run-mytop.sh run-innotop.sh tokenInfo vault-edit /usr/local/bin/  
COPY config.json /etc/consul-template/config/config.json  
COPY mysql.json /usr/local/etc/  
COPY mytop /usr/bin/mytop  
COPY innotop/innotop /usr/local/bin/innotop  
COPY innotop/innotop.1 /usr/local/share/man/man1/innotop.1  
  
RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk update && \  
apk add perl-carp perl-compress-raw-bzip2 \  
perl-compress-raw-zlib perl-dbd-mysql \  
perl-dbi perl-data-dumper@community \  
perl-exporter \  
perl-file-temp perl-getopt-long \  
perl-io-compress perl-pathtools \  
perl-socket perl-term-readkey \  
perl-time-local@testing \  
perl-time-hires && \  
apk add bash \  
ca-certificates \  
curl \  
jq \  
mysql-client \  
openssl \  
python \  
util-linux \  
vim \  
wget && \  
wget --no-check-certificate
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
-O /tmp/vault_${VAULT_VERSION}_linux_amd64.zip && \  
wget --no-check-certificate https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -O
/tmp/consul_template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip -O
/tmp/google-cloud-sdk.zip && \  
cd /tmp && \  
unzip vault_${VAULT_VERSION}_linux_amd64.zip && \  
unzip consul_template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
mv consul-template vault /usr/local/bin/ && \  
chmod 0755 /usr/local/bin/* && \  
cd /usr/local && unzip /tmp/google-cloud-sdk.zip && \  
google-cloud-sdk/install.sh --usage-reporting=false \--path-update=true
\--bash-completion=true && \  
google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
WORKDIR /working  

