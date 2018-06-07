FROM cybe/ps-sshd-base:xenial  
  
RUN \  
# Install runtime tools  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
bind9-host \  
ca-certificates \  
curl \  
dnsutils \  
file \  
geoip-database \  
git \  
gnupg \  
htop \  
iftop \  
iproute2 \  
iputils-ping \  
iputils-tracepath \  
keychain \  
less \  
lsof \  
man-db \  
mc \  
mtr-tiny \  
netcat-openbsd \  
nmap \  
openssl \  
powerline \  
psmisc \  
tmux \  
traceroute \  
unrar \  
unzip \  
whois \  
wget \  
xz-utils \  
zip \  
zsh \  
# Cleanup  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
# Prepare config directories for vim and zsh  
&& mkdir /etc/vim/vimrc.local.d \  
&& mkdir /etc/zsh/zlogin.d \  
&& rm /usr/share/zsh/*/scripts/newuser \  
# Install tmux-resurrect  
&& git clone https://github.com/tmux-plugins/tmux-resurrect
/usr/local/share/tmux/plugins/tmux-resurrect \  
&& cd /usr/local/share/tmux/plugins/tmux-resurrect \  
&& rm -rf docs/ lib/ tests/ video/ .git* .travis.yml CHANGELOG.md
CONTRIBUTING.md LICENSE.md README.md run_tests \  
&& cd / \  
# Install tmux-continuum  
&& git clone https://github.com/tmux-plugins/tmux-continuum
/usr/local/share/tmux/plugins/tmux-continuum \  
&& cd /usr/local/share/tmux/plugins/tmux-continuum \  
&& rm -rf docs/ .git* CHANGELOG.md CONTRIBUTING.md LICENSE.md README.md \  
&& cd /  
  
COPY dircolors.conf /etc/  
COPY tmux/* /etc/tmux/  
COPY zlogin zprofile /etc/zsh/  
COPY vimrc.local /etc/vim/  
COPY base16-ocean.vim /etc/vim/colors/  
COPY meminfo upinfo /usr/local/bin/  
COPY powerline /usr/local/share/powerline/  
  

