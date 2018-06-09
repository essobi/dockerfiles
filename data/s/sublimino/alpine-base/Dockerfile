FROM alpine:3.6  
  
WORKDIR /code  
  
# https://github.com/docker/docker/blob/master/project/PACKAGERS.md#runtime-
dependencies  
RUN apk add --no-cache \  
btrfs-progs \  
curl \  
e2fsprogs \  
e2fsprogs-extra \  
iptables \  
xfsprogs \  
xz  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.11.1  
ENV DOCKER_SHA256
893e3c6e89c0cd2c5f1e51ea41bc2dd97f5e791fcfa3cee28445df277836339d  
  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v \  
&& echo "docker daemon -D -s overlay" >> $HOME/.bash_history  
  
ENV ALPINE_DIG_URL https://github.com/sequenceiq/docker-alpine-
dig/releases/download/v9.10.2/dig.tgz  
  
ENV APK_PACKAGES \  
ack \  
atop \  
awstats \  
bash \  
bash-completion \  
bc \  
build-base \  
coreutils \  
curl \  
docker \  
docker-bash-completion \  
findutils \  
git \  
git-bash-completion \  
gnupg \  
go \  
grep \  
jq \  
less \  
lsof \  
man \  
mtr \  
nginx \  
ngrep \  
nmap \  
nodejs \  
nodejs-npm \  
ntop \  
openssh \  
py2-pip \  
python2-dev \  
python3 \  
python3-dev \  
smokeping \  
strace \  
sudo \  
supervisor \  
shadow \  
sysstat \  
tar \  
tcpdump \  
the_silver_searcher \  
tree \  
vim \  
wget  
  
# tmux-bash-completion not found  
RUN sed 's#alpine/v[0-9\.]*/main$#alpine/edge/testing#' /etc/apk/repositories
| grep testing >> /etc/apk/repositories \  
&& apk --update-cache --arch=x86_64 add ${APK_PACKAGES} \  
&& pip install s3cmd \  
&& curl -L ${ALPINE_DIG_URL} | tar -xzv -C /usr/local/bin/ \  
&& curl -L http://www.ivarch.com/programs/sources/pv-1.6.0.tar.gz | tar -xvz
-C /tmp/ \  
&& cd /tmp/pv-1* && ./configure && make install \  
&& sed 's#/bin/ash$#/bin/bash#' -i /etc/passwd \  
&& rm -rf /tmp/pv /var/cache/apk/*  
  
RUN TF_RELEASES=$(curl https://releases.hashicorp.com/index.json); \  
TF_VERSION=$(echo "${TF_RELEASES}" | jq '.terraform.versions[].version' \  
| grep -v '-' | sort -V | tail -n1); \  
echo "Terraform version: ${TF_VERSION}"; \  
echo "${TF_RELEASES}" \  
| jq -r ".terraform.versions[${TF_VERSION}].builds | .[].url |
match(\".*linux_amd64.*\").string" \  
| xargs wget \  
&& unzip terraform*.zip \  
&& mv terraform /usr/local/bin/ && \  
unset TF_RELEASES TF_VERSION  
  
RUN echo "cache-min 9999999" >> ~/.npmrc \  
&& npm config set cache-min 31540000 \  
&& npm i sublimino/rollcage  
  
RUN \  
cd /root \  
&& touch /root/.bashrc \  
&& wget --continue
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-186.0.0-linux-x86_64.tar.gz \  
&& tar xzvf google-cloud-sdk-*.tar.gz \  
&& google-cloud-sdk/install.sh \  
\--usage-reporting false \  
\--command-completion true \  
\--path-update true \  
\--rc-path /root/.bashrc \  
\--additional-components \  
beta \  
kubectl \  
docker-credential-gcr \  
\--quiet  
ENV PATH="/root/google-cloud-sdk/bin:${PATH}"  
  
# glibc compat layer https://github.com/sgerrand/alpine-pkg-glibc  
RUN \  
apk --no-cache add ca-certificates \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk \  
&& apk add glibc-2.25-r0.apk  
  
ENV GOPATH=/code/  
ENV PATH="${PATH}:/code/bin"  
RUN go get -v -u github.com/golang/dep/cmd/dep  
  
RUN curl -sfL https://raw.githubusercontent.com/apex/up/master/install.sh | sh  
RUN curl
https://github.com/gohugoio/hugo/releases/download/v0.30.2/hugo_0.30.2_Linux-64bit.tar.gz
-LO \  
&& tar xzvf hugo*.tar.gz \  
&& mv hugo /usr/local/bin/  
  
CMD ["bash"]  

