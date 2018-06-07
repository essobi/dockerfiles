FROM ubuntu:16.04  
  
# Update system and install prerequisites  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y apt-transport-https && \  
apt-get clean  
  
ENV BAZEL_VERSION 0.4.5  
  
RUN echo 'APT::Install-Recommends "false";' >>
/etc/apt/apt.conf.d/99_norecommends \  
&& echo 'APT::AutoRemove::RecommendsImportant "false";' >>
/etc/apt/apt.conf.d/99_norecommends \  
&& echo 'APT::AutoRemove::SuggestsImportant "false";' >>
/etc/apt/apt.conf.d/99_norecommends  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends ca-certificates curl git \  
&& echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" > \  
/etc/apt/sources.list.d/bazel.list \  
&& curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | apt-key
add \- \  
&& apt-get update \  
&& apt-get install -y bazel=${BAZEL_VERSION} \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /etc/apt/sources.list.d/bazel.list \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN update-ca-certificates -f  
  
  
  
# Add Docker APT source  
RUN echo deb https://get.docker.io/ubuntu docker main >
/etc/apt/sources.list.d/docker.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 && \  
apt-get update -y && \  
apt-get install -y lxc-docker python python-dev python-pip python-virtualenv
git && \  
apt-get clean \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo 'DOCKER_OPTS="-H :2375 unix:///var/run/docker.sock"' >>
/etc/default/docker  

