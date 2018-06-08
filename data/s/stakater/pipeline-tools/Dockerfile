FROM docker:17.09.1-ce as docker  
FROM golang:1.9.3-alpine3.7  
COPY \--from=docker /usr/local/bin/docker /usr/local/bin/  
  
MAINTAINER Stakater <stakater@gmail.com>  
  
# Update apk repository list in separate layer  
# so that install layer does not run everytime  
RUN apk update  
  
# This is needed for compatibility with our nodes  
ENV DOCKER_API_VERSION=1.32  
# Install ansible, boto, aws-cli, and some handy tools  
RUN echo "===> Installing Utilities from apk ..." && \  
apk -v --update --progress add sudo git bash wget openssh groff less python
py-pip curl jq unzip nodejs=8.9.3-r1 coreutils python py-pip openssl ca-
certificates make sshpass openssh-client rsync && \  
\  
apk --update add --virtual build-dependencies \  
python-dev libffi-dev openssl-dev build-base && \  
pip install --upgrade pip cffi && \  
\  
\  
echo "===> Installing Ansible..." && \  
pip install ansible && \  
\  
\  
echo "===> Installing Boto..." && \  
pip install boto && \  
\  
\  
echo "===> Installing Aws-Cli..." && \  
pip install awscli && \  
\  
\  
echo "===> Installing handy tools (not absolutely required)..." && \  
pip install --upgrade pywinrm && \  
\  
\  
echo "===> Removing package list..." && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk/* && \  
\  
\  
echo "===> Adding hosts for convenience..." && \  
mkdir -p /etc/ansible && \  
echo 'localhost' > /etc/ansible/hosts  
  
# Install gotpl  
ARG GOTPL_VERSION=0.1.5  
ARG
GOTPL_URL=https://github.com/wodby/gotpl/releases/download/${GOTPL_VERSION}/gotpl-
alpine-linux-amd64-${GOTPL_VERSION}.tar.gz  
RUN mkdir -p /tmp/gotpl/ && \  
wget ${GOTPL_URL} -O /tmp/gotpl/gotpl.tar.gz && \  
tar -xzvf /tmp/gotpl/gotpl.tar.gz -C /tmp/gotpl/ && \  
mv /tmp/gotpl/gotpl /usr/local/bin/gotplenv  
  
# Install kops, kubectl, and terraform  
RUN mkdir -p /aws && \  
curl -LO --show-error
https://github.com/kubernetes/kops/releases/download/1.8.1/kops-linux-amd64 &&
\  
mv kops-linux-amd64 /usr/local/bin/kops && \  
chmod +x /usr/local/bin/kops && \  
curl -LO --show-error https://storage.googleapis.com/kubernetes-
release/release/v1.8.0/bin/linux/amd64/kubectl && \  
mv kubectl /usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/kubectl && \  
wget
https://releases.hashicorp.com/terraform/0.11.1/terraform_0.11.1_linux_amd64.zip
&& \  
unzip terraform_0.11.1_linux_amd64.zip && \  
mv terraform /usr/local/bin/ && \  
rm terraform_0.11.1_linux_amd64.zip  
  
# Install helm, and landscaper  
ARG HELM_VERSION=v2.7.2  
ARG HELM_FILENAME=helm-${HELM_VERSION}-linux-amd64.tar.gz  
ARG HELM_URL=http://storage.googleapis.com/kubernetes-helm/${HELM_FILENAME}  
  
ARG LANDSCAPER_VERSION=1.0.12  
ARG LANDSCAPER_FILENAME=landscaper-${LANDSCAPER_VERSION}-linux-amd64.tar.gz  
ARG
LANDSCAPER_URL=https://github.com/Eneco/landscaper/releases/download/${LANDSCAPER_VERSION}/${LANDSCAPER_FILENAME}  
  
RUN curl -L ${HELM_URL} | tar zxv -C /tmp \  
&& cp /tmp/linux-amd64/helm /bin/helm \  
&& rm -rf /tmp/* \  
&& curl -L ${LANDSCAPER_URL} | tar zxv -C /tmp \  
&& cp /tmp/landscaper /bin/landscaper \  
&& rm -rf /tmp/* \  
&& curl https://glide.sh/get | sh \  
&& wget https://github.com/stakater/jx-release-
version/releases/download/1.1.0/jx-release-version_v1.1.0_Linux_x86_64.tar.gz
\  
&& tar -xzvf jx-release-version_v1.1.0_Linux_x86_64.tar.gz -C /tmp \  
&& cd /tmp \  
&& chmod +x jx-release-version \  
&& mv jx-release-version /bin/jx-release-version \  
&& rm -rf /tmp/*  
  
ADD bootstrap.sh /  
  
ADD binaries/* /usr/local/bin/  
  
ENTRYPOINT ["/bootstrap.sh"]  

