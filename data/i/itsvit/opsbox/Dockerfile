FROM alpine:3.6  
ENV ANSIBLE_VERSION 2.4.1.0  
ENV JINJA2_VERSION 2.10  
ENV AWSCLI_VERSION 1.11.185  
ENV KUBE_AWS_RELEASE v0.9.8  
ENV KUBECTL_VERSION v1.8.5  
RUN apk update \  
&& apk add --no-cache unzip curl tar bash \  
python make bash vim jq \  
openssl openssh-client sshpass \  
gcc libffi-dev python-dev musl-dev openssl-dev py-pip py-virtualenv \  
git coreutils less bash-completion \  
libc6-compat && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /etc/bash_completion.d/ /etc/profile.d/  
  
# Install kubectl  
RUN curl -L -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \  
chmod +x /usr/bin/kubectl && \  
kubectl completion bash > /etc/bash_completion.d/kubectl.sh  
  
# Intsall kube-aws  
RUN curl --fail -sSL -O https://github.com/kubernetes-incubator/kube-
aws/releases/download/${KUBE_AWS_RELEASE}/kube-aws-linux-amd64.tar.gz && \  
tar xzf kube-aws-linux-amd64.tar.gz && \  
mv linux-amd64/kube-aws /usr/local/bin/kube-aws && \  
chmod +x /usr/local/bin/kube-aws && \  
rm -rf linux-amd64/ && \  
rm -f kube-aws-linux-amd64.tar.gz  
  
# Install Ansible  
RUN pip install ansible==${ANSIBLE_VERSION} Jinja2==${JINJA2_VERSION} && \  
rm -rf /root/.cache && \  
find / -type f -regex '.*\\.py[co]' -delete  
  
# Install aws cli bundle  
RUN pip install awscli==${AWSCLI_VERSION} boto && \  
rm -rf /root/.cache && \  
find / -type f -regex '.*\\.py[co]' -delete && \  
ln -s /usr/local/aws/bin/aws_bash_completer /etc/bash_completion.d/aws.sh && \  
ln -s /usr/local/aws/bin/aws_completer /usr/local/bin/  
  
COPY start.sh /start.sh  
  
RUN chmod +x /start.sh && \  
mkdir /mnt/opsbox && \  
ln -s /mnt/opsbox/.aws /root/.aws && \  
ln -s /mnt/opsbox/.kube /root/.kube  
  
WORKDIR /opsbox  
  
VOLUME ["/opsbox", "/mnt/opsbox"]  
  
ENTRYPOINT ["/start.sh"]  

