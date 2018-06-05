FROM alessandrob/aws-codebuild-git  
  
ENV KUBECTL_VERSION=1.9.2  
ENV KOPS_VERSION=1.8.0  
ENV TERM xterm  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q git curl python-pip \  
&& curl -LO https://storage.googleapis.com/kubernetes-
release/release/v$KUBECTL_VERSION/bin/linux/amd64/kubectl \  
&& mv kubectl /usr/bin/ \  
&& chmod +x /usr/bin/kubectl \  
&& curl -LO
https://github.com/kubernetes/kops/releases/download/$KOPS_VERSION/kops-linux-
amd64 \  
&& mv kops-linux-amd64 /usr/bin/kops \  
&& chmod +x /usr/bin/kops \  
&& pip install envtpl awscli\  
&& curl -sSL https://get.docker.com/ | sh\  
&& apt-get clean && apt-get purge -y -q --auto-remove curl && rm -rf
/var/lib/apt/lists/*  
  
ADD docker-entrypoint /  
RUN chmod +x /docker-entrypoint  
  
ENTRYPOINT ["/docker-entrypoint"]

