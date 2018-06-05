FROM alpine:latest  
  
ENV TERRAFORM_VERSION=0.10.0  
ENV
TERRAFORM_SHA256SUM=f991039e3822f10d6e05eabf77c9f31f3831149b52ed030775b6ec5195380999  
  
ENV HUGO_VERSION 0.26  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-64bit  
  
RUN apk add --update git curl openssh python py-pip python3 py-pygments bash
tar jq tree && \  
rm -rf /var/cache/apk/* && \  
curl
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
> terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
echo "${TERRAFORM_SHA256SUM} terraform_${TERRAFORM_VERSION}_linux_amd64.zip" >
terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
sha256sum -cs terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin && \  
rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip  
  
# HUGO  
ADD
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
/tmp  
RUN tar -xf /tmp/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz -C /tmp \  
&& mkdir -p /usr/local/sbin \  
&& mv /tmp/hugo /usr/local/sbin/hugo \  
&& rm -rf /tmp/hugo_${HUGO_VERSION}_linux_amd64  
  
# AWS CLI  
RUN pip install --upgrade awscli s3cmd python-magic setuptools httpie python-
frontmatter requests python-dateutil

