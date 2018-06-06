# gitlab-ci-runner-python  
FROM ubuntu:14.04.1  
MAINTAINER Doug Goldstein "cardoe@cardoe.com"  
# Based on https://github.com/bkw/gitlab-ci-runner-nodejs/master/Dockerfile  
# by Bernhard Weisshuhn <bkw@codingforce.com>  
# Based on https://github.com/gitlabhq/gitlab-ci-runner/blob/master/Dockerfile  
# by Sytse Sijbrandij <sytse@gitlab.com>  
# This script will start a runner in a docker container.  
#  
# First build the container and give a name to the resulting image:  
# docker build \  
# -t cardoe/gitlab-ci-runner-python \  
# github.com/cardoe/docker-gitlab-ci-runner-python  
#  
# Then set the environment variables and run the gitlab-ci-runner in the
container:  
# docker run \  
# -d \  
# -e CI_SERVER_URL=https://ci.example.com \  
# -e REGISTRATION_TOKEN=replaceme \  
# -e HOME=/root \  
# -e GITLAB_SERVER_FQDN=gitlab.example.com \  
# cardoe/gitlab-ci-runner-python  
#  
# The new runner should show up in the GitLab CI interface on /runners  
#  
# You can start an interactive session to test new commands with:  
# docker run \  
# -it \  
# -e CI_SERVER_URL=https://ci.example.com \  
# -e REGISTRATION_TOKEN=replaceme \  
# -e HOME=/root \  
# cardoe/gitlab-ci-runner-python:latest /bin/bash  
#  
# If you ever want to freshly rebuild the runner please use:  
# docker build -no-cache \  
# -t cardoe/gitlab-ci-runner-python \  
# github.com/cardoe/docker-gitlab-ci-runner-python  
# Building a container so we don't have an interactive prompt to debconf  
ENV DEBIAN_FRONTEND noninteractive  
  
# Enable deadsnakes repo  
RUN echo "deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu trusty main" >
\  
/etc/apt/sources.list.d/fkrull-deadsnakes.list  
RUN gpg --keyserver keyserver.ubuntu.com --recv-keys DB82666C && \  
gpg --armor --export DB82666C | apt-key add -  
  
# Update your packages and install the ones that are needed to compile Ruby  
RUN apt-get --quiet --yes update && \  
apt-get --quiet --yes install \  
curl \  
build-essential \  
openssh-server \  
ruby2.0 \  
ruby2.0-dev \  
libicu-dev \  
git \  
python2.6-dev \  
python3.3-dev \  
python3.4-dev \  
python2.7-dev \  
python-pip \  
python3-pip \  
python-virtualenv && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
# Ubuntu is weird about Ruby  
RUN rm /usr/bin/ruby /usr/bin/gem  
RUN ln -s /usr/bin/ruby2.0 /usr/bin/ruby  
RUN ln -s /usr/bin/gem2.0 /usr/bin/gem  
  
# don't install ruby rdocs or ri:  
RUN echo "gem: --no-rdoc --no-ri" >> /etc/gemrc  
  
# Prepare a known host file for non-interactive ssh connections  
RUN mkdir -p /root/.ssh  
RUN touch /root/.ssh/known_hosts  
  
# Install the runner  
RUN mkdir /gitlab-ci-runner && cd /gitlab-ci-runner && curl -sL
https://github.com/gitlabhq/gitlab-ci-runner/archive/v5.0.0.tar.gz | tar xz
--strip-components=1  
  
# Install the gems for the runner  
RUN cd /gitlab-ci-runner && gem install bundler && bundle install  
  
# When the image is started add the remote server key, install the runner and
run it  
WORKDIR /gitlab-ci-runner  
CMD ssh-keyscan -H $GITLAB_SERVER_FQDN >> /root/.ssh/known_hosts & bundle exec
./bin/setup_and_run  
  

