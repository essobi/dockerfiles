FROM cybe/ps-sshd-interactive:xenial  
  
RUN \  
# Install build-deps for lftp  
apt-get update \  
&& BUILD_DEPS="build-essential libncurses5-dev libreadline-dev pkg-config
libgnutls-dev" \  
&& apt-get install -y \--no-install-recommends ${BUILD_DEPS} \  
# Fetch lftp  
&& mkdir /tmp/lftp \  
&& wget -nv http://lftp.yar.ru/ftp/lftp-4.8.0.tar.xz -O /tmp/lftp/lftp.tar.xz
\  
&& echo "1e6598c655176f60cb6e35ecd3e2464bbbcfee74 /tmp/lftp/lftp.tar.xz" |
sha1sum -c - \  
&& tar -xJf /tmp/lftp/lftp.tar.xz -C /tmp/lftp \--strip-components=1 \  
&& rm /tmp/lftp/lftp.tar.xz \  
# Compile and install lftp  
&& cd /tmp/lftp \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
# Cleanup  
&& rm -rf /tmp/lftp \  
&& apt-get purge -y ${BUILD_DEPS} \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
# Add user files  
&& deluser www-data \  
&& addgroup \--gid 801 files \  
&& addgroup \--gid 800 dl \  
&& addgroup \--system \--gid 99 www-data \  
&& useradd -g 801 -G dl,www-data -m -N -s /usr/bin/zsh -u 8003 files \  
&& mkdir /files /www /dl \  
&& chown files:files /files \  
&& chown files:www-data /www \  
&& chown files:dl /dl \  
&& chmod 775 /dl /www \  
# Setup environment for user files  
&& ln -s /files/.ssh ~files/.ssh \  
&& ln -s /files/.lftp ~files/.lftp \  
&& ln -s /files/.tmux ~files/.tmux \  
&& echo "[ -d /files ] && HISTFILE=/files/.zsh_history" >
/etc/zsh/zlogin.d/10-history.zsh \  
&& echo "set viminfo+=n/files/.viminfo" >
/etc/vim/vimrc.local.d/10-viminfo.vim \  
# Resolve uids of other users  
&& useradd -d /nonexistent -g 800 -l -M -N -s /usr/sbin/nologin -u 8000
torrent \  
&& useradd -d /nonexistent -g 800 -l -M -N -s /usr/sbin/nologin -u 8001 aria2
\  
&& useradd -d /nonexistent -g 800 -l -M -N -s /usr/sbin/nologin -u 8002
filebot  

