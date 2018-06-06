FROM buildpack-deps:jessie-scm  
WORKDIR /terraform/  
VOLUME ["/terraform/plans"]  
ENV TF_LOG=INFO  
ENV TF_LOG_PATH=/terraform/plans/terraform.log  
  
ENV TERRAFORM_VERSION=0.8.4  
ENV
TERRAFORM_SHA256SUM=297d35d0b4311445cd87ef032d3dec917bcc7a8b163ead28a4c45d966a2f75cc  
  
RUN apt-get update && apt-get install -y wget nano ca-certificates unzip git
bash bash-completion curl \  
unzip zip netcat-openbsd mysql-client python && \  
curl -sSL https://get.docker.com/ | sh && \  
curl
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
> terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
echo "${TERRAFORM_SHA256SUM} terraform_${TERRAFORM_VERSION}_linux_amd64.zip" >
terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
sha256sum -c terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin && \  
rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
rm terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
curl -o awscli-bundle.zip https://s3.amazonaws.com/aws-cli/awscli-bundle.zip
&& \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm -r awscli-bundle.zip && \  
rm -rf awscli-bundle && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
cd /bin && \  
curl -s https://api.github.com/repos/chadgrant/terraform-
helpers/releases/latest | grep 'browser_' | grep "_linux_amd64" | cut -d\" -f4
| awk '{print "curl -LOk " $0}' | sh && \  
chmod +x *_linux_amd64 && \  
for f in *_linux_amd64; do mv $f $(echo $f | sed 's/_linux_amd64$//g'); done  
  
COPY modules /terraform/modules/  

