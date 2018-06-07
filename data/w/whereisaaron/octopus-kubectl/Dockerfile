  
FROM mono  
MAINTAINER Aaron Roydhouse <aaron@roydhouse.com>  
  
# Based on official mono with kubectl Kubernetes client added  
# mono and sshd is needed for the Octopus Deploy Calamari utility  
# kubectl, helm, cli53, and jq are used to deploy to a Kubernetes cluster  
# gettext-base package is added for envsubt utility  
# git, patch, rsync, p7zip are includes to assist fetching packages  
#  
# When deployed into a Kubernetes cluster the Pod Service Account  
# is automatically available, and will work with kubectl without  
# further configuration. Or you can mount a kubctl config file  
# with certificates/tokens/password from a Kubernetes secret  
#  
# For ssh access you need to mount a suitable file at  
# /root/.ssh/authorized_keys  
# create-config.sh will create the ConfigMap for you, and  
# the start.sh script will fix the .ssh directory permissions  
ENV \  
KUBE_VERSION="v1.5.2" \  
HELM_VERSION="v2.5.1" \  
CLI53_VERSION="0.8.12" \  
DUPLICACY_VERSION="2.0.10" \  
JQ_VERSION="1.5" \  
TERM=xterm  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -y \  
&& apt-get install -y ssh gettext-base git patch rsync p7zip mg \  
&& curl -sS -L https://storage.googleapis.com/kubernetes-
release/release/${KUBE_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& curl -sS -L https://storage.googleapis.com/kubernetes-
helm/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar xzf - -C /usr/local/bin
--strip-components=1 linux-amd64/helm \  
&& curl -sS -L
https://github.com/barnybug/cli53/releases/download/${CLI53_VERSION}/cli53-linux-
amd64 -o /usr/local/bin/cli53 \  
&& curl -sS -L
https://github.com/gilbertchen/duplicacy/releases/download/v${DUPLICACY_VERSION}/duplicacy_linux_x64_${DUPLICACY_VERSION}
-o /usr/local/bin/duplicacy \  
&& curl -sS -L
https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64
-o /usr/local/bin/jq \  
&& chmod +x /usr/local/bin/kubectl /usr/local/bin/cli53
/usr/local/bin/duplicacy /usr/local/bin/jq \  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& mkdir -p /var/run/sshd \  
&& chmod 0755 /var/run/sshd  
  
# We will start and expose ssh on port 22  
EXPOSE 22  
# Add fixed host keys to the container, so they don't change on every restart  
ADD host-keys/ssh_host_*_key /etc/ssh/  
  
# Add the container start script, which will start ssh  
COPY start.sh /  
ENTRYPOINT ["/start.sh"]  

