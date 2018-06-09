FROM suckowbiz/base  
  
LABEL maintainer="Tobias Suckow <tobias@suckow.biz>"  
  
ENV VERSION_GIT=2.17.1 \  
VERSION_GIT_LFS=2.4.2 \  
GIT_HOME="/var/lib/git"  
ENV GIT_CONFIG_DIR="${GIT_HOME}/config" \  
# Tell git where the .git repository is located since the work tree is
customized.  
GIT_DIR="${GIT_HOME}/repository/.git" \  
SSH_CONFIG_DIR=/var/lib/ssh \  
URL_GIT_SOURCES_TAR_GZ="https://github.com/git/git/archive/v${VERSION_GIT}.tar.gz"  
RUN apt-get --quiet --quiet --yes --no-install-recommends install \  
asciidoc \  
autoconf \  
build-essential \  
docbook \  
gettext \  
less \  
libcurl4-openssl-dev \  
man \  
ssh \  
tcl \  
tk \  
vim \  
xsltproc \  
xmlto \  
zlib1g-dev  
  
WORKDIR /opt  
RUN curl --fail --location --show-error --silent --output git.tar.gz
"${URL_GIT_SOURCES_TAR_GZ}" \  
&& tar --extract --file git.tar.gz \  
&& rm --force git.tar.gz \  
&& cd "git-${VERSION_GIT}" \  
&& make configure \  
&& ./configure --prefix=/usr \  
&& make all man \  
&& make install install-man  
  
WORKDIR /opt/git-${VERSION_GIT}/contrib/subtree  
RUN make \  
&& make install install-man  
  
WORKDIR /opt  
RUN rm --force --recursive "git-${VERSION_GIT}"  
  
WORKDIR /var/tmp  
RUN curl \  
\--fail \  
\--location \  
\--show-error \  
\--silent \  
\--remote-name \  
https://github.com/git-lfs/git-lfs/releases/download/v${VERSION_GIT_LFS}/git-
lfs-linux-amd64-${VERSION_GIT_LFS}.tar.gz \  
&& tar --extract --file git-lfs-linux-amd64-${VERSION_GIT_LFS}.tar.gz \  
&& git-lfs-${VERSION_GIT_LFS}/install.sh \  
&& rm --recursive --force git-lfs*  
  
WORKDIR /etc/skel/  
RUN mkdir .config \  
&& ln --symbolic "${GIT_CONFIG_DIR}" .config/git \  
&& ln --symbolic "${SSH_CONFIG_DIR}" .ssh  
  
VOLUME ["${SSH_CONFIG_DIR}", "${GIT_CONFIG_DIR}"]  
  
ENTRYPOINT ["/entrypoint.sh", "git"]  
CMD ["--help"]  

