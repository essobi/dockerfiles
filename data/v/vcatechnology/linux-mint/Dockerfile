FROM vcatechnology/ubuntu:16.04  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="A Linux Mint image that is updated daily" \  
org.label-schema.url="https://www.linuxmint.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/vcatechnology/docker-linux-mint"
\  
org.label-schema.vendor="VCA Technology" \  
org.label-schema.version=$VERSION \  
org.label-schema.license=MIT \  
org.label-schema.schema-version="1.0"  
  
# Set up the Linux Mint repositories  
RUN REPO_LIST=/etc/apt/sources.list.d/mint.list \  
&& echo "deb http://packages.linuxmint.com/ sarah main upstream import
backport " > ${REPO_LIST} \  
&& LINUX_MINT_KEY=$(apt update 2>&1 | grep -o '[0-9A-Z]\\{16\\}$' | xargs) \  
&& apt-key adv --recv-keys --keyserver keyserver.ubuntu.com ${LINUX_MINT_KEY}
\  
&& vca-install-package --allow-unauthenticated linuxmint-keyring \  
&& unset LINUX_MINT_KEY REPO_LIST  
  
# Install the necessary packages to convert to Linux Mint  
RUN vca-install-package base-files  
  
# Update all packages  
RUN apt-get -q update \  
&& echo console-setup console-setup/charmap select UTF-8 | debconf-set-
selections \  
&& apt-get -fqy -o Dpkg::Options::="--force-confnew" -o APT::Immediate-
Configure=false dist-upgrade \  
&& apt-get -qy autoremove \  
&& apt-get -q clean  

