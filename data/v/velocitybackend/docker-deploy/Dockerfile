FROM google/cloud-sdk:alpine  
  
RUN gcloud components install kubectl  
  
RUN apk add --no-cache \  
tar \  
sudo \  
jq \  
gnupg \  
make \  
expect \  
g++ \  
openssh \  
openssl \  
openssl-dev \  
curl \  
bash \  
git \  
python \  
py-pip \  
groff \  
less \  
mailcap \  
&& \  
pip install --upgrade awscli s3cmd python-magic  
  
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get
> get_helm.sh \  
&& chmod +x get_helm.sh \  
&& ./get_helm.sh -v v2.3.0  
  
VOLUME /root/.aws  
VOLUME /project  
  
WORKDIR /project  
  
RUN set -x && curl -O https://www.agwa.name/projects/git-crypt/downloads/git-
crypt-0.6.0.tar.gz && \  
tar -zxf git-crypt-0.6.0.tar.gz && \  
cd git-crypt-0.6.0 && \  
make && \  
make install  
  
RUN set -x && \  
VER="17.09.0-ce" && \  
curl -L -o /tmp/docker-$VER.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-$VER.tgz && \  
tar -xzf /tmp/docker-$VER.tgz -C /tmp && \  
mv /tmp/docker/* /usr/bin  

