FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
man \  
curl \  
ca-certificates \  
unzip \  
openssl \  
python \  
fish \  
openssh-client \  
jq \  
git  
  
RUN curl -sSL https://bootstrap.pypa.io/get-pip.py | python  
RUN pip install -q awscli  
  
ENV MACHINE_STORAGE_BUCKET=docker-machine.staging.gfio.ca  
ENV MACHINE_STORAGE_PATH=/root/.docker/machine  
ENV BIN_PATH=/usr/local/bin  
  
ENV TERRAFORM_VERSION=0.6.14  
RUN bash -c "\  
curl -sSOL
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
;\  
unzip -qq -d ${BIN_PATH} terraform_${TERRAFORM_VERSION}_linux_amd64.zip ;\  
rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip"  
  
ENV PACKER_VERSION=0.10.0  
RUN bash -c "\  
curl -sSOL
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
;\  
unzip -qq -d ${BIN_PATH} packer_${PACKER_VERSION}_linux_amd64.zip ;\  
rm packer_${PACKER_VERSION}_linux_amd64.zip"  
  
ENV KUBE_AWS_VERSION=0.6.1  
RUN bash -c "\  
curl -sSL https://github.com/coreos/coreos-
kubernetes/releases/download/v${KUBE_AWS_VERSION}/kube-aws-linux-amd64.tar.gz
| tar -zxvf - ;\  
mv linux-amd64/kube-aws ${BIN_PATH} ;\  
rm -r linux-amd64"  
  
ENV KUBECTL_VERSION=1.2.2  
RUN bash -c "\  
curl -sSL https://storage.googleapis.com/kubernetes-
release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl >
${BIN_PATH}/kubectl ;\  
chmod +x ${BIN_PATH}/kubectl"  
  
ENV DOCKER_MACHINE_VERSION=0.6.0  
RUN bash -c "\  
curl -sSL
https://github.com/docker/machine/releases/download/v${DOCKER_MACHINE_VERSION}/docker-
machine-Linux-x86_64 > ${BIN_PATH}/docker-machine ;\  
chmod +x ${BIN_PATH}/docker-machine"  
  
ENV DOCKER_COMPOSE_VERSION=1.7.1  
RUN bash -c "\  
curl -sSL
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-Linux-x86_64 > ${BIN_PATH}/docker-compose ;\  
chmod +x ${BIN_PATH}/docker-compose"  
  
ENV DOCKER_VERSION=1.11.1  
RUN bash -c "\  
cd /tmp ;\  
curl -sSL
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz | tar
-zxvf - ;\  
mv docker/* ${BIN_PATH}/"  
  
ENV RACK_VERSION=1.1.1  
RUN bash -c "\  
curl -sSL
https://ec4a542dbf90c03b9f75-b342aba65414ad802720b41e8159cf45.ssl.cf5.rackcdn.com/${RACK_VERSION}/Linux/amd64/rack
> ${BIN_PATH}/rack ;\  
chmod +x ${BIN_PATH}/rack"  
  
COPY rootfs /  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  

