FROM alpine  
  
ENV DOCKER_VERSION="17.12.1-ce"  
ENV DOCKER_COMPOSE_VERSION="1.20.1"  
ENV KUBECTL_VERSION="1.7.3"  
ENV TERRAFORM_VERSION="0.11.7"  
RUN apk -Uuv add curl git bash python py-pip jq openssh-client && \  
pip install awscli docker-compose==${DOCKER_COMPOSE_VERSION} && \  
curl -fsSLO
https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz
&& \  
tar --strip-components=1 -xvzf docker-$DOCKER_VERSION.tgz -C /usr/local/bin &&
\  
rm /docker-$DOCKER_VERSION.tgz && \  
curl -L https://storage.googleapis.com/kubernetes-
release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/kubectl && \  
curl -L
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
-o ${TERRAFORM_VERSION} && \  
unzip -x ${TERRAFORM_VERSION} -d /usr/local/bin/ && \  
rm ${TERRAFORM_VERSION} && \  
chmod +x /usr/local/bin/terraform && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  

