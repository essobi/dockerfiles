FROM opensuse/tumbleweed  
  
LABEL description="Image to try packaging."  
  
# these default values are used, if not provided while running build script  
ENV WATERFRONT_USER=morelia  
ENV WATERFRONT_UID=9999  
######## CREATE USER  
RUN zypper --non-interactive in sudo  
RUN useradd --create-home --shell /bin/bash --uid $WATERFRONT_UID
$WATERFRONT_USER \--groups users  
RUN echo "$WATERFRONT_USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN echo "$WATERFRONT_USER ALL = NOPASSWD: /usr/bin/build" >> /etc/sudoers  
RUN echo "$WATERFRONT_USER ALL = NOPASSWD: /usr/bin/osc" >> /etc/sudoers  
  
ARG MAKETHREADS=1  
USER root  
  
# install devel-packages and build-tools for graph_tool  
RUN zypper --non-interactive --gpg-auto-import-keys addrepo \  
\--repo
http://download.opensuse.org/repositories/openSUSE:/Tools/openSUSE_Factory/openSUSE:Tools.repo  
  
RUN zypper --non-interactive --gpg-auto-import-keys refresh  
  
# install devel-packages and build-tools for graph_tool  
RUN zypper --non-interactive install \  
osc \  
build \  
hostname \  
perl-TimeDate \  
git \  
wget \  
curl \  
vim  
  
####### Finish Building Container  
# reset USER and WORKDIR  
USER $WATERFRONT_USER  
WORKDIR /home/$WATERFRONT_USER  
  
ENTRYPOINT ["/bin/bash"]  

