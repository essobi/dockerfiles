FROM microsoft/aspnetcore-build:latest  
  
RUN apt-get -qq update && apt-get -qq install apt-transport-https  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
ENV CLOUD_SDK_VERSION 174.0.0  
ARG INSTALL_COMPONENTS  
RUN apt-get update -qqy && apt-get install -qqy \  
xsltproc \  
jq \  
yarn \  
curl \  
gcc \  
python-dev \  
python-setuptools \  
apt-transport-https \  
lsb-release \  
openssh-client \  
git \  
&& easy_install -U pip && \  
pip install -U crcmod && \  
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" >
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - &&
\  
apt-get update && apt-get install -y google-cloud-sdk=${CLOUD_SDK_VERSION}-0
kubectl $INSTALL_COMPONENTS && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image  
VOLUME ["/root/.config"]  
  
RUN curl -sL https://sentry.io/get-cli/ | bash  
ENV SENTRY_ORG fasterintel  
  
ENV DOCKER_VERSION 17.06.1-ce  
ENV HELM_VERSION 2.6.1  
RUN curl -L -o /tmp/helm-$HELM_VERSION.tgz https://kubernetes-
helm.storage.googleapis.com/helm-v$HELM_VERSION-linux-amd64.tar.gz \  
&& mkdir -p /tmp/helm \  
&& tar -xz -C /tmp/helm -f /tmp/helm-$HELM_VERSION.tgz \  
&& mv /tmp/helm/linux-amd64/* /usr/bin/ \  
&& chmod +x /usr/bin/helm  
  
RUN curl -L -o /tmp/docker-$DOCKER_VERSION.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz
\  
&& tar -xz -C /tmp -f /tmp/docker-$DOCKER_VERSION.tgz \  
&& mv /tmp/docker/* /usr/bin

