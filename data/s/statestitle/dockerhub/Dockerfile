FROM heroku/heroku:16  
## This file is broken into sections.  
## 1. Installation of binaries needed by the underwriter  
## 2. Python setup from https://github.com/docker-
library/python/blob/cf179e4a7b442b29d85f521c2b172b89ef04beef/3.6/stretch/Dockerfile  
## 3. Standard circleci setup from https://github.com/circleci/circleci-
images/blob/master/shared/images/Dockerfile-basic.template  
### 1. Underwriter binaries  
RUN apt-get update -y  
RUN apt-get -y install software-properties-common libffi-dev libssl-dev build-
essential  
RUN add-apt-repository --yes ppa:libreoffice/libreoffice-5-4  
RUN apt-get update -y  
RUN apt-get install -y wget libgl1-mesa-glx libreoffice-writer libtiff-tools
libxdamage1 libxfixes3  
  
### 2. Python  
### The following is copied from: https://github.com/docker-
library/python/blob/cf179e4a7b442b29d85f521c2b172b89ef04beef/3.6/stretch/Dockerfile  
ENV PATH /usr/local/bin:$PATH  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# runtime dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
tcl \  
tk \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D  
ENV PYTHON_VERSION 3.6.2  
RUN set -ex \  
&& buildDeps=' \  
dpkg-dev \  
tcl-dev \  
tk-dev \  
' \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -rf "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--enable-loadable-sqlite-extensions \  
\--enable-shared \  
\--with-system-expat \  
\--with-system-ffi \  
\--without-ensurepip \  
&& make -j "$(nproc)" \  
&& make install \  
&& ldconfig \  
\  
&& apt-get purge -y --auto-remove $buildDeps \  
\  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python  
  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python3-config python-config  
  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 9.0.1  
RUN set -ex; \  
\  
wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \  
\  
python get-pip.py \  
\--disable-pip-version-check \  
\--no-cache-dir \  
"pip==$PYTHON_PIP_VERSION" \  
; \  
pip --version; \  
\  
find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' +; \  
rm -f get-pip.py  
  
### 3. CircleCI  
### The following is copied from: https://github.com/circleci/circleci-
images/blob/master/shared/images/Dockerfile-basic.template  
# make Apt non-interactive  
RUN echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/90circleci \  
&& echo 'DPkg::Options "--force-confnew";' >> /etc/apt/apt.conf.d/90circleci  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# man directory is missing in some base images  
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863199  
RUN apt-get update \  
&& mkdir -p /usr/share/man/man1 \  
&& apt-get install -y \  
git mercurial xvfb \  
locales sudo openssh-client ca-certificates tar gzip parallel \  
net-tools netcat unzip zip bzip2 gnupg curl wget  
  
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
  
USER circleci  

