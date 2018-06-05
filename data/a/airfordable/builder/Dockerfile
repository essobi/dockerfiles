FROM fedora:latest  
  
MAINTAINER Airfordable Engineering <engineering(at)airfordable.com>  
  
# COPY repos/ /etc/yum.repos.d/  
# Installing the pre-release of yarn works around the publishing bug in 0.27.5  
RUN dnf -y install \  
awscli \  
docker \  
docker-compose \  
findutils \  
gcc-c++ \  
git \  
jq \  
mongodb-server \  
node-gyp \  
nodejs \  
pigz \  
procps-ng \  
python \  
strace \  
tar \  
which \  
zip \  
&& dnf -y autoremove \  
&& dnf -y clean all \  
&& npm -g install lerna@2.10.2  
#  
# Use docker binary from Docker because Fedora docker breaks things. See  
# https://discuss.circleci.com/t/aws-ecr-unable-to-push-no-basic-auth-
credentials/12868  
#  
ENV DOCKER_CHANNEL=stable DOCKER_VERSION=17.03.1-ce  
RUN curl -fL \  
"https://download.docker.com/linux/static/${DOCKER_CHANNEL}/x86_64/docker-${DOCKER_VERSION}.tgz"
\  
| tar xz \  
&& mv ./docker/docker /usr/bin/docker-vanilla \  
&& chmod 755 /usr/bin/docker-vanilla  
  
#  
# Use this to control what Docker we use  
#  
RUN mv /usr/bin/docker /usr/bin/docker-fedora \  
&& ln -s docker-vanilla /usr/bin/docker  
  
# Do this copy here to help caching.  
COPY bin/ /usr/bin/  

