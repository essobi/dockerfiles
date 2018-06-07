FROM centos:7  
# @see http://label-schema.org/rc1/  
LABEL maintainer="Phase2 <outrigger@phase2technology.com>" \  
# Replacement for the old MAINTAINER directive has fragmented.  
# "vendor" prevents CentOS from leaking through, the other is for tools
integrations.  
vendor="Phase2 <outrigger@phase2technology.com>" \  
org.label-schema.vendor="Phase2 <outrigger@phase2technology.com>" \  
# CentOS adds a name label but it is misleading in our instance.  
name="Outrigger Keel" \  
org.label-schema.name="Outrigger Keel" \  
org.label-schema.description="A CentOS-based CLI Developer Base Image for
building cross-functional containers. Not for production services." \  
org.label-schema.url="http://docs.outrigger.sh" \  
org.label-schema.vcs-url="https://github.com/phase2/docker-keel" \  
org.label-schema.docker.cmd="docker run -it --rm outrigger/keel bash" \  
org.label-schema.docker.cmd.help="docker run -it --rm outrigger/keel" \  
org.label-schema.docker.debug="docker exec -it $CONTAINER bash" \  
org.label-schema.schema-version="1.0"  
# Install base packages.  
RUN yum -y install epel-release yum-plugin-ovl deltarpm && \  
# Add the IUS repository. This is needed for git2.  
curl -L "https://centos7.iuscommunity.org/ius-release.rpm" > /usr/local/ius-
release.rpm && \  
rpm -Uvh /usr/local/ius-release.rpm && \  
yum -y update && \  
yum -y install \  
bind-utils \  
bzip2 \  
curl \  
dnsutils \  
git2u-all \  
jq \  
less \  
make \  
openssl \  
patch \  
pv \  
rsync \  
sudo \  
ssh \  
sendmail \  
telnet \  
unzip \  
vim-minimal \  
# Necessary for drush and developer orientation.  
which && \  
yum clean all  
  
# Download & Install confd.  
ENV CONFD_VERSION 0.11.0  
RUN curl -L
"https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-
linux-amd64" > /usr/bin/confd && \  
chmod +x /usr/bin/confd  
ENV CONFD_OPTS '--backend=env --onetime'  
# Ensure $HOME is set  
ENV HOME /root  
  
# Configure Git  
# https://git-scm.com/docs/git-config#git-config-corepreloadIndex  
RUN git config --global core.preloadindex true  
# Run the init script.  
# This script can be customized for extending Docker images by:  
# 1. Copy the script to your image repo.  
# 2. Modify the script as needed.  
# 3. In your Dockerfile, copy the script to the filesystem root.  
ENTRYPOINT ["/init"]  
  
# Set up a standard volume for logs.  
VOLUME ["/var/log/services"]  
  
COPY root /  
  
CMD [ "/usage.sh" ]  

