FROM stackfeed/alpine-python3  
  
# Host user *IDs  
ONBUILD ARG _USER=user  
ONBUILD ARG _UID=1000  
ONBUILD ARG _GID=1000  
ARG TF_VERSION=0.11.7  
ARG KOPS_RELEASE=1.8.1  
# KUBECTL_SOURCE: Change to kubernetes-dev/ci for CI  
ARG KUBECTL_SOURCE=kubernetes-release/release  
# KUBECTL_TRACK: Currently latest from KUBECTL_SOURCE. Change to
latest-1.3.txt, etc. if desired.  
ARG KUBECTL_TRACK=stable.txt  
  
# Additional packages for the toolbox  
RUN apk add --no-cache vim sudo jq fping make git openssh-client iptables  
  
# Install awscli & terraform  
RUN pip install awscli sshuttle && apk add --no-cache groff less mailcap && \  
curl -sSL
https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip
-o /tmp/terraform.zip && \  
unzip /tmp/terraform.zip -d /usr/bin && \  
rm -rf /tmp/*  
  
# Get kops and kubectl  
RUN curl -SsL --retry 5 -o /usr/bin/kops
https://github.com/kubernetes/kops/releases/download/${KOPS_RELEASE}/kops-
linux-amd64 && \  
KUBECTL_VERSION=$(curl -SsL --retry 5
"https://storage.googleapis.com/${KUBECTL_SOURCE}/${KUBECTL_TRACK}") && \  
curl -SsL --retry 5
"https://storage.googleapis.com/${KUBECTL_SOURCE}/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"
> /usr/bin/kubectl && \  
chmod +x /usr/bin/kubectl /usr/bin/kops  
  
# entrypoint (bash is the default default)  
ADD ./entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Configure unprivileged user (remeber NOT TO USE adduser from busybox!)  
ONBUILD RUN groupadd -g ${_GID} ${_USER} && \  
useradd -s /bin/bash -md /home/${_USER} -u ${_UID} -g ${_GID} ${_USER} && \  
echo "${_USER} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${_USER} && \  
chmod 440 /etc/sudoers.d/${_USER}  
  
ONBUILD USER $_UID:$_GID  
  
VOLUME ["/code"]  
WORKDIR "/code"  

