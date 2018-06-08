FROM buildpack-deps:jessie  
  
MAINTAINER Potiguar Faga <potz@potz.me>  
  
# Define software versions  
ENV GIT_VERSION=2.12.2 \  
VIM_VERSION=8.0.0525 \  
TMUX_VERSION=2.3 \  
DOCKER_VERSION=17.03.1-ce \  
ASDF_VERSION=0.2.1 \  
NODE_VERSION=7.8.0 \  
YARN_VERSION=0.22.0 \  
ERLANG_VERSION=19.3 \  
ELIXIR_VERSION=1.4.2 \  
PYTHON_VERSION=2.7.13 \  
RUBY_VERSION=2.4.1 \  
RUST_VERSION=1.16.0  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y locales && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale && \  
locale-gen en_US.utf8 && \  
update-locale LANG=en_US.UTF-8 && \  
cd /tmp && \  
# Git  
apt-get install -y wget gettext && \  
wget \--quiet https://github.com/git/git/archive/v${GIT_VERSION}.tar.gz && \  
tar -zxf v${GIT_VERSION}.tar.gz && \  
cd git-${GIT_VERSION} && make prefix=/usr/local install && \  
cd /tmp && rm -rf /tmp/v${GIT_VERSION}.tar.gz /tmp/git-${GIT_VERSION} && \  
# Vim  
apt-get install -y libncurses5-dev libgnome2-dev libgnomeui-dev \  
libgtk2.0-dev libatk1.0-dev libbonoboui2-dev \  
libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev \  
python3-dev ruby ruby-dev lua5.1 lua5.1-dev libperl-dev && \  
wget \--quiet https://github.com/vim/vim/archive/v${VIM_VERSION}.tar.gz && \  
tar -zxf v${VIM_VERSION}.tar.gz && \  
cd vim-${VIM_VERSION} && \  
./configure \--with-features=huge \  
\--enable-multibyte \  
\--enable-rubyinterp=yes \  
\--enable-pythoninterp=yes \  
\--with-python-config-dir=/usr/lib/python2.7/config \  
\--enable-gui=gtk2 \--enable-cscope \--prefix=/usr && \  
make VIMRUNTIMEDIR=/usr/share/vim/vim80 && \  
make install && \  
update-alternatives \--install /usr/bin/editor editor /usr/bin/vim 1 && \  
update-alternatives \--set editor /usr/bin/vim && \  
update-alternatives \--install /usr/bin/vi vi /usr/bin/vim 1 && \  
update-alternatives \--set vi /usr/bin/vim && \  
cd /tmp && rm -rf /tmp/v${VIM_VERSION}.tar.gz /tmp/vim-${VIM_VERSION} && \  
# Tmux  
apt-get install -y libevent-dev libncurses-dev pkg-config && \  
wget \--quiet
https://github.com/tmux/tmux/releases/download/${TMUX_VERSION}/tmux-${TMUX_VERSION}.tar.gz
&& \  
tar -zxf tmux-${TMUX_VERSION}.tar.gz && cd tmux-${TMUX_VERSION} && \  
./configure && make && make install && \  
cd /tmp && rm -rf /tmp/tmux-${TMUX_VERSION}.tar.gz /tmp/tmux-${TMUX_VERSION}
&& \  
# NodeJS  
for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys "$key" || \  
gpg \--keyserver pgp.mit.edu \--recv-keys "$key" || \  
gpg \--keyserver keyserver.pgp.com \--recv-keys "$key" ; \  
done && \  
curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" && \  
curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" && \  
gpg \--batch \--decrypt \--output SHASUMS256.txt SHASUMS256.txt.asc && \  
grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c -
&& \  
tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 && \  
rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt &&
\  
ln -s /usr/local/bin/node /usr/local/bin/nodejs && \  
# Yarn  
for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys "$key" || \  
gpg \--keyserver pgp.mit.edu \--recv-keys "$key" || \  
gpg \--keyserver keyserver.pgp.com \--recv-keys "$key" ; \  
done && \  
curl -fSL -o yarn.js "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-
legacy-$YARN_VERSION.js" && \  
curl -fSL -o yarn.js.asc "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-
legacy-$YARN_VERSION.js.asc" && \  
gpg \--batch \--verify yarn.js.asc yarn.js && \  
rm yarn.js.asc && \  
mv yarn.js /usr/local/bin/yarn && \  
chmod +x /usr/local/bin/yarn && \  
# ASDF package manager  
git clone https://github.com/asdf-vm/asdf.git /root/.asdf \--branch
v${ASDF_VERSION} && \  
# Docker binaries  
wget \--quiet
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz && \  
tar zxvf docker-${DOCKER_VERSION}.tgz && \  
find docker -maxdepth 1 -type f | xargs -I {} cp {} /bin && \  
rm -rf docker docker-${DOCKER_VERSION}.tgz && \  
# SSH Server  
apt-get install -y openssh-server && \  
sed -i "s/^#PasswordAuthentication.*$/PasswordAuthentication no/"
/etc/ssh/sshd_config && \  
mkdir /var/run/sshd && \  
chmod 0755 /var/run/sshd && \  
# Some useful tools  
apt-get install -y \  
tree strace htop less zip \  
tcpdump telnet net-tools dnsutils \  
wdiff colordiff && \  
# Install language tools with the asdf version manager  
/root/.asdf/bin/asdf plugin-add erlang https://github.com/asdf-vm/asdf-
erlang.git && \  
/root/.asdf/bin/asdf install erlang $ERLANG_VERSION && \  
/root/.asdf/bin/asdf global erlang $ERLANG_VERSION && \  
/root/.asdf/bin/asdf plugin-add elixir https://github.com/asdf-vm/asdf-
elixir.git && \  
/root/.asdf/bin/asdf install elixir $ELIXIR_VERSION && \  
/root/.asdf/bin/asdf global elixir $ELIXIR_VERSION && \  
/root/.asdf/bin/asdf plugin-add python https://github.com/tuvistavie/asdf-
python.git && \  
/root/.asdf/bin/asdf install python $PYTHON_VERSION && \  
/root/.asdf/bin/asdf global python $PYTHON_VERSION && \  
/root/.asdf/bin/asdf plugin-add ruby https://github.com/asdf-vm/asdf-ruby.git
&& \  
/root/.asdf/bin/asdf install ruby $RUBY_VERSION && \  
/root/.asdf/bin/asdf global ruby $RUBY_VERSION && \  
/root/.asdf/bin/asdf plugin-add rust https://github.com/code-lever/asdf-
rust.git && \  
/root/.asdf/bin/asdf install rust $RUST_VERSION && \  
/root/.asdf/bin/asdf global rust $RUST_VERSION  
  
# Fix locale settings  
ENV LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8  
  
VOLUME /root/.ssh  
WORKDIR /root  
EXPOSE 22  
  
ADD bootstrap.sh /  
  
CMD [ "/bootstrap.sh" ]  

