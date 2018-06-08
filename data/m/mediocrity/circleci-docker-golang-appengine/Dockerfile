##  
# From: https://github.com/CircleCI-Public/circleci-
dockerfiles/blob/master/golang/images/1.8.7-jessie/Dockerfile  
##  
FROM buildpack-deps:jessie-scm  
  
# make Apt non-interactive  
RUN echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/90circleci \  
&& echo 'DPkg::Options "--force-confnew";' >> /etc/apt/apt.conf.d/90circleci  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# man directory is missing in some base images  
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863199  
# Might need --no-install-recommends  
RUN apt-get update \  
&& mkdir -p /usr/share/man/man1 \  
&& apt-get install -y \  
git mercurial xvfb \  
locales sudo openssh-client ca-certificates tar gzip parallel \  
net-tools netcat unzip zip bzip2 gnupg curl wget \  
g++ gcc libc6-dev make pkg-config python-dev \  
python-setuptools apt-transport-https lsb-release \  
&& rm -rf /var/lib/apt/lists/*  
  
##  
# From: https://raw.githubusercontent.com/docker-
library/golang/cffcff7fce7f6b6b5c82fc8f7b3331a10590a661/1.8/jessie/Dockerfile  
##  
##  
ENV GOLANG_VERSION 1.8.5  
RUN set -eux; \  
\  
# this "case" statement is generated via "update.sh"  
dpkgArch="$(dpkg --print-architecture)"; \  
case "${dpkgArch##*-}" in \  
amd64) goRelArch='linux-amd64';
goRelSha256='4f8aeea2033a2d731f2f75c4d0a4995b357b22af56ed69b3015f4291fca4d42d'
;; \  
armhf) goRelArch='linux-armv6l';
goRelSha256='f5c58e7fd6cdfcc40b94c6655cf159b25836dffe13431f683b51705b8a67d608'
;; \  
i386) goRelArch='linux-386';
goRelSha256='cf959b60b89acb588843ff985ecb47a7f6c37da6e4987739ab4aafad7211464f'
;; \  
ppc64el) goRelArch='linux-ppc64le';
goRelSha256='1ee0874ce8c8625e14b4457a4861777be78f30067d914bcb264f7e0331d087de'
;; \  
s390x) goRelArch='linux-s390x';
goRelSha256='e978a56842297dc8924555540314ff09128e9a62da9881c3a26771ddd5d7ebc2'
;; \  
*) goRelArch='src'; goRelSha256='4949fd1a5a4954eb54dd208f2f412e720e23f32c91203116bed0387cf5d0ff2d'; \  
echo >&2; echo >&2 "warning: current architecture ($dpkgArch) does not have a
corresponding Go binary release; will be building from source"; echo >&2 ;; \  
esac; \  
\  
url="https://golang.org/dl/go${GOLANG_VERSION}.${goRelArch}.tar.gz"; \  
wget -O go.tgz "$url"; \  
echo "${goRelSha256} *go.tgz" | sha256sum -c -; \  
tar -C /usr/local -xzf go.tgz; \  
rm go.tgz; \  
\  
if [ "$goRelArch" = 'src' ]; then \  
echo >&2; \  
echo >&2 'error: UNIMPLEMENTED'; \  
echo >&2 'TODO install golang-any from jessie-backports for GOROOT_BOOTSTRAP
(and uninstall after build)'; \  
echo >&2; \  
exit 1; \  
fi; \  
\  
export PATH="/usr/local/go/bin:$PATH"; \  
go version  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
COPY go-wrapper /usr/local/bin/  
##  
##  
# From: https://github.com/GoogleCloudPlatform/cloud-sdk-
docker/blob/master/Dockerfile  
##  
##  
ENV CLOUD_SDK_VERSION 198.0.0  
RUN easy_install -U pip && \  
pip install -U crcmod && \  
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" >
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - &&
\  
apt-get update && \  
apt-get install -y google-cloud-sdk=${CLOUD_SDK_VERSION}-0 \  
google-cloud-sdk-app-engine-python=${CLOUD_SDK_VERSION}-0 \  
google-cloud-sdk-app-engine-java=${CLOUD_SDK_VERSION}-0 \  
google-cloud-sdk-app-engine-go=${CLOUD_SDK_VERSION}-0 \  
google-cloud-sdk-datalab=${CLOUD_SDK_VERSION}-0 \  
google-cloud-sdk-datastore-emulator=${CLOUD_SDK_VERSION}-0 \  
google-cloud-sdk-pubsub-emulator=${CLOUD_SDK_VERSION}-0 \  
google-cloud-sdk-bigtable-emulator=${CLOUD_SDK_VERSION}-0 \  
google-cloud-sdk-cbt=${CLOUD_SDK_VERSION}-0 \  
kubectl && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image && \  
gcloud --version  
VOLUME ["/root/.config"]  
##  
# Set timezone to UTC by default  
RUN ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime  
  
# Use unicode  
RUN locale-gen C.UTF-8 || true  
ENV LANG=C.UTF-8  
# install jq  
RUN JQ_URL="https://circle-downloads.s3.amazonaws.com/circleci-
images/cache/linux-amd64/jq-latest" \  
&& curl --silent --show-error --location --fail --retry 3 --output /usr/bin/jq
$JQ_URL \  
&& chmod +x /usr/bin/jq \  
&& jq --version  
  
# Install Docker  
# Docker.com returns the URL of the latest binary when you hit a directory
listing  
# We curl this URL and `grep` the version out.  
# The output looks like this:  
#> # To install, run the following commands as root:  
#> curl -fsSLO
https://download.docker.com/linux/static/stable/x86_64/docker-17.05.0-ce.tgz
&& tar --strip-components=1 -xvzf docker-17.05.0-ce.tgz -C /usr/local/bin  
#>  
#> # Then start docker in daemon mode:  
#> /usr/local/bin/dockerd  
RUN set -ex \  
&& export DOCKER_VERSION=$(curl --silent --fail --retry 3
https://download.docker.com/linux/static/stable/x86_64/ | grep -o -e
'docker-[.0-9]*-ce\\.tgz' | sort -r | head -n 1) \  
&&
DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/${DOCKER_VERSION}"
\  
&& echo Docker URL: $DOCKER_URL \  
&& curl --silent --show-error --location --fail --retry 3 --output
/tmp/docker.tgz "${DOCKER_URL}" \  
&& ls -lha /tmp/docker.tgz \  
&& tar -xz -C /tmp -f /tmp/docker.tgz \  
&& mv /tmp/docker/* /usr/bin \  
&& rm -rf /tmp/docker /tmp/docker.tgz \  
&& which docker \  
&& (docker version || true)  
  
# docker compose  
RUN COMPOSE_URL="https://circle-downloads.s3.amazonaws.com/circleci-
images/cache/linux-amd64/docker-compose-latest" \  
&& curl --silent --show-error --location --fail --retry 3 --output
/usr/bin/docker-compose $COMPOSE_URL \  
&& chmod +x /usr/bin/docker-compose \  
&& docker-compose version  
  
# install dockerize  
RUN DOCKERIZE_URL="https://circle-downloads.s3.amazonaws.com/circleci-
images/cache/linux-amd64/dockerize-latest.tar.gz" \  
&& curl --silent --show-error --location --fail --retry 3 --output
/tmp/dockerize-linux-amd64.tar.gz $DOCKERIZE_URL \  
&& tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-amd64.tar.gz \  
&& rm -rf /tmp/dockerize-linux-amd64.tar.gz \  
&& dockerize --version  
  
RUN groupadd --gid 3434 circleci \  
&& useradd --uid 3434 --gid circleci --shell /bin/bash --create-home circleci
\  
&& echo 'circleci ALL=NOPASSWD: ALL' >> /etc/sudoers.d/50-circleci \  
&& echo 'Defaults env_keep += "DEBIAN_FRONTEND"' >> /etc/sudoers.d/env_keep  
  
# BEGIN IMAGE CUSTOMIZATIONS  
# END IMAGE CUSTOMIZATIONS  
USER circleci  
  
CMD ["/bin/sh"]  

