FROM langrisha/room:laputa  
  
ENV \  
RCRC=/usr/local/lib/rcrc \  
TERM=xterm-256color \  
XDG_CONFIG_HOME=/root/.config \  
HOME=/root  
  
CMD ["/bin/zsh"]  
  
RUN \  
npm install -g \  
commitizen \  
cz-conventional-changelog \  
diff-so-fancy \  
eslint \  
eslint-config-airbnb \  
eslint-loader \  
eslint-plugin-import \  
eslint-plugin-jsx-a11y \  
eslint-plugin-react \  
git-recent \  
lighthouse \  
standard \  
  
# rcm  
&& export rcm_version=1.3.0-1 \  
&& curl https://thoughtbot.github.io/rcm/debs/rcm_${rcm_version}_all.deb \  
-o /tmp/rcm.deb \  
&& rcm_sha=2e95bbc23da4a0b995ec4757e0920197f4c92357214a65fedaf24274cda6806d \  
sha=$(sha256sum /tmp/rcm.deb | cut -f1 -d' ') \  
[ "$sha" = "$rcm_sha" ] \  
&& dpkg -i /tmp/rcm.deb \  
&& rm /tmp/rcm.deb \  
  
# Goodies  
&& apt-get update && apt-get install -y \--no-install-recommends \  
ack-grep \  
dnsutils \  
emacs \  
gdb \  
gettext-base \  
htop \  
install-info \  
iotop \  
less \  
lsof \  
lynx \  
man-db \  
mc \  
neovim/testing \  
net-tools \  
rsync \  
siege \  
silversearcher-ag \  
socat \  
strace \  
sudo \  
tmux \  
vim \  
weechat \  
zsh \  
&& rm -rf /var/lib/apt/lists/* \  
  
&& pip2 install \  
neovim \  
&& pip3 install urwid \  
&& pip3 install \  
neovim \  
sen \  
  
# SciPy stack  
&& pip3 install \  
numpy \  
scipy \  
matplotlib \  
ipython \  
jupyter \  
pandas \  
sympy \  
nose  
  
COPY rcrc /usr/local/lib/rcrc  
  
RUN \  
# dotfiles  
git clone --depth 1 \  
https://github.com/thoughtbot/dotfiles.git \  
/usr/local/lib/thoughtbot-dotfiles \  
&& git clone --depth 1 \  
https://github.com/langri-sha/dotfiles.git \  
/usr/local/lib/langri-sha-dotfiles \  
  
# root user  
&& chsh -s /bin/zsh root \  
&& USER=root rcup -t emacs -t nvim -t tmux -t zsh \  
&& TMUX_PLUGIN_MANAGER_PATH=$HOME/.tmux/install_plugins \  
$HOME/.tmux/plugins/tpm/bin/install_plugins \  
&& nvim -c "call dein#install() | quit" \  
&& git config --global core.pager "diff-so-fancy | less --tabs=4 -RFX" \  
  
# Pretty Git log visualization (http://stackoverflow.com/a/34467298/44041)  
&& git config --global alias.lg '!git lg1' \  
&& git config --global alias.lg1 '!git lg1-specific --all' \  
&& git config --global alias.lg2 '!git lg2-specific --all' \  
&& git config --global alias.lg3 '!git lg3-specific --all' \  
&& git config --global alias.lg1-specific "log --graph --abbrev-commit
--decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold
green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold
yellow)%d%C(reset)'" \  
&& git config --global alias.lg2-specific "log --graph --abbrev-commit
--decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold
cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''
%C(white)%s%C(reset) %C(dim white)- %an%C(reset)'" \  
&& git config --global alias.lg3-specific "log --graph --abbrev-commit
--decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold
cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset) %C(bold cyan)(committed:
%cD)%C(reset) %C(bold yellow)%d%C(reset)%n'' %C(white)%s%C(reset)%n'' %C(dim
white)- %an <%ae> %C(reset) %C(dim white)(committer: %cn <%ce>)%C(reset)'" \  
  
# Admit all to sudoers.  
&& echo "ALL ALL=(ALL:ALL) ALL" > /etc/sudoers \  
  
# Configure access control in the home directory.  
&& find /root -type d -exec chmod o+rwx {} \; \  
&& find /root -type f -exec chmod o+rw {} \; \  
&& chmod o-w -R /root/.oh-my-zsh /root/.zsh  

