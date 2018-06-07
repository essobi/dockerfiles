FROM gitlab/dind:latest  
MAINTAINER Firef0x <Firefgx {aT} gmail.com>  
  
ENV GITLAB_CI_MULTI_RUNNER_VERSION=1.3.0 \  
GITLAB_CI_MULTI_RUNNER_USER=gitlab_ci_multi_runner \  
GITLAB_CI_MULTI_RUNNER_HOME_DIR="/home/gitlab_ci_multi_runner" \  
DOCKER_DATA_DIR="/var/lib/docker" \  
GITLAB_CI_MULTI_RUNNER_DATA_DIR="${GITLAB_CI_MULTI_RUNNER_HOME_DIR}/data" \  
PATH=${GITLAB_CI_MULTI_RUNNER_HOME_DIR}/.nvm/bin:$PATH \  
GOSU_VERSION=1.9  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
E1DD270288B4E6030699E45FA1715D88E1DF1F24 \  
&& echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main" >>
/etc/apt/sources.list \  
# && sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
\  
&& sed -i 's/^deb-src/# deb-src/g' /etc/apt/sources.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
vim wget net-tools ca-certificates unzip git-core openssh-client curl
libapparmor1 build-essential libssl-dev \  
&& wget -O /usr/local/bin/gitlab-ci-multi-runner \  
https://gitlab-ci-multi-runner-
downloads.s3.amazonaws.com/v${GITLAB_CI_MULTI_RUNNER_VERSION}/binaries/gitlab-
ci-multi-runner-linux-amd64 \  
&& chmod 0755 /usr/local/bin/gitlab-ci-multi-runner \  
&& wget -O /usr/local/bin/gosu \  
https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture) \  
&& wget -O /usr/local/bin/gosu.asc \  
https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& adduser --disabled-login --gecos 'GitLab CI Runner'
${GITLAB_CI_MULTI_RUNNER_USER} \  
&& gosu ${GITLAB_CI_MULTI_RUNNER_USER} ln -sf
${GITLAB_CI_MULTI_RUNNER_DATA_DIR}/.ssh
${GITLAB_CI_MULTI_RUNNER_HOME_DIR}/.ssh \  
&& gpasswd -a ${GITLAB_CI_MULTI_RUNNER_USER} docker \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gosu ${GITLAB_CI_MULTI_RUNNER_USER} curl -sSL
https://raw.githubusercontent.com/creationix/nvm/master/install.sh |
NVM_DIR="${GITLAB_CI_MULTI_RUNNER_HOME_DIR}/.nvm" gosu
${GITLAB_CI_MULTI_RUNNER_USER} bash \  
&& gosu ${GITLAB_CI_MULTI_RUNNER_USER} echo "[[ -s
${GITLAB_CI_MULTI_RUNNER_HOME_DIR}/.nvm/nvm.sh ]] && .
${GITLAB_CI_MULTI_RUNNER_HOME_DIR}/.nvm/nvm.sh" >>
${GITLAB_CI_MULTI_RUNNER_HOME_DIR}/.bashrc \  
&& bash -c "echo \"[[ -s \${GITLAB_CI_MULTI_RUNNER_HOME_DIR}/.nvm/nvm.sh ]] &&
. \${GITLAB_CI_MULTI_RUNNER_HOME_DIR}/.nvm/nvm.sh\" >> /etc/profile.d/npm.sh"  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
VOLUME ["${GITLAB_CI_MULTI_RUNNER_DATA_DIR}", "${DOCKER_DATA_DIR}"]  
WORKDIR "${GITLAB_CI_MULTI_RUNNER_HOME_DIR}"  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

