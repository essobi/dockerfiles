# Docker image containing all dependencies for running terraform in Nubis  
FROM alpine:3.6  
LABEL maintainer="Jason Crowe <jcrowe@mozilla.com>"  
  
# Do not add a 'v' as pert of the version string (ie: v1.1.3)  
#+ This causes issues with extraction due to GitHub's methodology  
#+ Where necesary the 'v' is specified in code below  
ENV AwCliVersion=1.10.38 \  
JqVersion=1.5-r4 \  
KopsVersion=1.9.0 \  
KubeCtlVersion=1.10.2 \  
TerraformVersion=0.11.7 \  
Json2HclVersion=0.0.6 \  
UnicredsVersion=1.5.1  
WORKDIR /nubis  
  
# Install container dependencies  
#+ Cleanup apk cache files  
RUN apk add --no-cache \  
bash \  
bind-tools \  
curl \  
git \  
jq=${JqVersion} \  
py-pip \  
rsync \  
unzip \  
&& rm -f /var/cache/apk/APKINDEX.* \  
&& pip install awscli==${AwCliVersion} \  
&& mkdir -p /nubis/bin /nubis/work  
  
# Install Terraform & Unicreds & Kops & Kubectl  
RUN ["/bin/bash", "-c", "set -o pipefail \  
&& curl -L -o terraform_${TerraformVersion}_linux_amd64.zip
https://releases.hashicorp.com/terraform/${TerraformVersion}/terraform_${TerraformVersion}_linux_amd64.zip
\  
&& unzip terraform_${TerraformVersion}_linux_amd64.zip -d /nubis/bin \  
&& rm terraform_${TerraformVersion}_linux_amd64.zip \  
&& curl -L
https://github.com/Versent/unicreds/releases/download/${UnicredsVersion}/unicreds_${UnicredsVersion}_linux_amd64.tar.gz
\  
| tar -C /nubis/bin -xzf - \  
&& curl -LO --silent --show-error
https://github.com/kubernetes/kops/releases/download/${KopsVersion}/kops-
linux-amd64 \  
&& mv kops-linux-amd64 /usr/local/bin/kops \  
&& chmod +x /usr/local/bin/kops \  
&& curl -LO --silent --show-error
https://github.com/kvz/json2hcl/releases/download/v${Json2HclVersion}/json2hcl_v${Json2HclVersion}_linux_amd64
\  
&& mv json2hcl_v${Json2HclVersion}_linux_amd64 /usr/local/bin/json2hcl \  
&& chmod +x /usr/local/bin/json2hcl \  
&& curl -LO https://storage.googleapis.com/kubernetes-
release/release/v${KubeCtlVersion}/bin/linux/amd64/kubectl \  
&& mv kubectl /usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl" ]  
  
# Copy over the nubis-deploy script  
COPY [ "nubis-deploy", "/nubis/bin/" ]  
  
# Copy over the account-deploy script  
COPY [ "account-deploy", "/nubis/bin/" ]  
  
ENV PATH /nubis/bin:$PATH  
ENTRYPOINT [ "/nubis/bin/nubis-deploy" ]  
CMD [ "help" ]  

