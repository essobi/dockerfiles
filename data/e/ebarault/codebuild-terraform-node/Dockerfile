FROM ubuntu:16.04  
ARG TERRAFORM_VERSION=0.11.7  
ARG TERRAGRUNT_VERSION=0.14.10  
ARG NODE_VERSION=6.x  
ARG AWSCLI_VERSION=1.15.21  
ARG GITLFS_VERSION=2.3.4  
ARG ANSIBLE_VERSION=2.4.3.0  
ENV DOCKER_BUCKET="download.docker.com" \  
DOCKER_VERSION="17.09.0-ce" \  
DOCKER_CHANNEL="stable" \  
DOCKER_SHA256="a9e90a73c3cdfbf238f148e1ec0eaff5eb181f92f35bdd938fd7dab18e1c4647"
\  
DIND_COMMIT="3b5fac462d21ca164b3778647420016315289034" \  
DOCKER_COMPOSE_VERSION="1.16.1"  
RUN apt-get update && \  
# Install add-apt-repository  
apt-get install -y --no-install-recommends \  
software-properties-common && \  
# Update git and install utils  
add-apt-repository ppa:git-core/ppa && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
wget curl git openssh-client jq python make \  
ca-certificates tar gzip zip unzip bzip2 gettext-base && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
# Install Nodejs  
RUN curl -sL https://deb.nodesource.com/setup_"$NODE_VERSION" | bash -  
RUN apt-get install -y --no-install-recommends nodejs  
  
# Install Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install yarn  
  
# Install pip  
RUN wget "https://bootstrap.pypa.io/get-pip.py" -O /tmp/get-pip.py && \  
python /tmp/get-pip.py  
  
# Install Ansible  
RUN pip install "ansible==$ANSIBLE_VERSION"  
  
# Install boto and boto3  
# boto is installed from maishsk:develop until
https://github.com/boto/boto/pull/3794 is merged  
RUN pip install boto3 && \  
git clone -b develop https://github.com/maishsk/boto.git && \  
cd boto && \  
python setup.py install  
  
# Install AWS CLI  
RUN pip install awscli=="$AWSCLI_VERSION" && \  
rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install AWS ELASTIC BEANSTALK CLI  
RUN pip install awsebcli --upgrade  
  
# Install Terraform  
RUN curl -sL
https://releases.hashicorp.com/terraform/"$TERRAFORM_VERSION"/terraform_"$TERRAFORM_VERSION"_linux_amd64.zip
-o terraform_"$TERRAFORM_VERSION"_linux_amd64.zip && \  
unzip terraform_"$TERRAFORM_VERSION"_linux_amd64.zip -d /usr/bin && \  
chmod +x /usr/bin/terraform  
  
# Install Terragrunt  
RUN curl -sL https://github.com/gruntwork-
io/terragrunt/releases/download/v"$TERRAGRUNT_VERSION"/terragrunt_linux_amd64
-o /usr/bin/terragrunt && \  
chmod +x /usr/bin/terragrunt  
  
# Install Git LFS  
RUN curl -sL https://github.com/git-lfs/git-
lfs/releases/download/v"$GITLFS_VERSION"/git-lfs-linux-
amd64-"$GITLFS_VERSION".tar.gz -o gitlfs.tar.gz && \  
mkdir -p gitlfs && \  
tar --extract --file gitlfs.tar.gz --strip-components 1 --directory gitlfs &&
\  
chmod +x gitlfs/install.sh && \  
./gitlfs/install.sh  
  
# Install Docker with dind support  
COPY dockerd-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/dockerd-entrypoint.sh  
  
# From the docker:17.09  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/linux/static/${DOCKER_CHANNEL}/x86_64/docker-${DOCKER_VERSION}.tgz"
-o docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar --extract --file docker.tgz --strip-components 1 --directory
/usr/local/bin/ \  
&& rm docker.tgz \  
&& docker -v \  
# From the docker dind 17.09  
# && apt-get update && apt-get install -y --no-install-recommends \  
# e2fsprogs=1.42.9-* iptables=1.4.21-* xfsprogs=3.1.9ubuntu2 xz-
utils=5.1.1alpha+20120614-* \  
&& apt-get update && apt-get install -y --no-install-recommends \  
e2fsprogs iptables xfsprogs xz-utils \  
# set up subuid/subgid so that "--userns-remap=default" works out-of-the-box  
&& addgroup dockremap \  
&& useradd -g dockremap dockremap \  
&& echo 'dockremap:165536:65536' >> /etc/subuid \  
&& echo 'dockremap:165536:65536' >> /etc/subgid \  
&& wget
"https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" -O
/usr/local/bin/dind \  
&& curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-Linux-x86_64 > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/dind /usr/local/bin/docker-compose \  
# Ensure docker-compose works  
&& docker-compose version \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
  
VOLUME /var/lib/docker  
  
ENTRYPOINT ["dockerd-entrypoint.sh"]  

