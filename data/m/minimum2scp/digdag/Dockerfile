FROM debian:sid  
  
ARG DIGDAG_VERSION=0.9.25  
ARG DOCKER_VERSION=18.03.0-ce  
ARG RUBY_VERSION=2.5.1  
ARG BUNDLER_VERSION=1.16.2  
ARG RUBYGEMS_VERSION=  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
git curl openssl ca-certificates \  
openjdk-8-jre-headless \  
python \  
build-essential autoconf bison ca-certificates libgdbm-dev libncursesw5-dev
libncurses5-dev libreadline-dev zlib1g-dev libssl-dev libffi-dev libyaml-dev
libgmp-dev && \  
apt-get clean  
  
## install digdag  
RUN curl -o /usr/local/bin/digdag --create-dirs -L
"https://dl.digdag.io/digdag-${DIGDAG_VERSION}" && \  
chmod +x /usr/local/bin/digdag  
  
## install docker  
RUN curl -L -o /tmp/docker-${DOCKER_VERSION}.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
&& \  
tar -xz -C /tmp -f /tmp/docker-${DOCKER_VERSION}.tgz && \  
mv /tmp/docker/* /usr/bin/ && \  
rm -rf /tmp/docker-${DOCKER_VERSION}.tgz /tmp/docker/  
  
## install rbenv, ruby  
RUN git clone https://github.com/rbenv/rbenv /opt/rbenv && \  
git clone https://github.com/rbenv/ruby-build /opt/rbenv/plugins/ruby-build &&
\  
git clone https://github.com/rkh/rbenv-update /opt/rbenv/plugins/rbenv-update  
ADD etc/profile.d/rbenv.sh /etc/profile.d/rbenv.sh  
RUN bash -lc "RUBY_CONFIGURE_OPTS=--disable-install-doc rbenv install
${RUBY_VERSION}" && \  
bash -lc "rbenv global ${RUBY_VERSION}" && \  
bash -lc "if [ -n \"${RUBYGEMS_VERSION}\" ] ; then gem update --system
${RUBYGEMS_VERSION}; fi" && \  
bash -lc "gem install bundler --version ${BUNDLER_VERSION} -N" && \  
bash -lc "rbenv rehash"  
  
ENTRYPOINT ["/bin/bash", "-l", "-c"]  
CMD digdag  

