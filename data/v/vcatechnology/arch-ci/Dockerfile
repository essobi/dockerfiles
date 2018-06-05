FROM vcatechnology/arch:latest  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="An up-to-date Arch Linux image with basic tool
chain packages" \  
org.label-schema.url="https://www.archlinux.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/vcatechnology/docker-arch-ci" \  
org.label-schema.vendor="VCA Technology" \  
org.label-schema.version=$VERSION \  
org.label-schema.license=MIT \  
org.label-schema.schema-version="1.0"  
  
# Install development packages  
RUN vca-install-package \  
make \  
cmake \  
automake \  
git \  
python \  
sudo \  
openssh \  
rsync  
  
# Grab the VCA CI scripts  
RUN vca-install-package wget && \  
wget -q https://tool-chain.vcatechnology.com/release/vca-tool-chain-ci-
scripts-latest.tar.xz && \  
tar -Jxf vca-tool-chain-ci-scripts-latest.tar.xz -C / && \  
rm vca-tool-chain-ci-scripts-latest.tar.xz && \  
vca-uninstall-package wget  
  
# Create a build-server user with sudo permissions & no password  
RUN useradd -ms /bin/bash build-server && \  
echo "build-server ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/build-
server && \  
echo "#includedir /etc/sudoers.d" >> /etc/sudoers && \  
chmod 0440 /etc/sudoers.d/build-server  
  
# Set the build-server user as default  
RUN mkdir /mnt/builds  
WORKDIR /mnt/builds  
RUN chown build-server:build-server /mnt/builds  
USER build-server  

