FROM freyskeyd/vim  
  
USER root  
  
RUN apt-get update -y && \  
apt-get install -y \--no-install-recommends --no-install-suggests \  
tree \  
git \  
tmux \  
zsh \  
rake \  
exuberant-ctags \  
automake \  
pkg-config \  
libpcre3-dev \  
zlib1g-dev \  
liblzma-dev \  
openssh-client \  
task \  
git-flow \  
php5 \  
php5-cli \  
python-pip \  
curl \  
wget && \  
git clone git://github.com/ggreer/the_silver_searcher.git && \  
cd the_silver_searcher && \  
./build.sh && \  
make install && \  
cd .. && \  
rm -rf the_silver_searcher && \  
pip install virtualenvwrapper && \  
pip install -U fig && \  
touch /etc/profile.d/init.sh && \  
chsh developer -s /bin/zsh && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed
"s/\\(.*\\)-\\([^0-9]\\+\\)/\1/")"'/d;s/^[^ ]* [^ ]* \\([^
]*\\).*/\1/;/[0-9]/!d' | xargs sudo apt-get -y purge  
  
ENV LANG=C.UTF-8  
  
USER developer  
  
RUN mkdir ~/.ssh && \  
ssh-keyscan -t rsa,dsa github.com >> ~/.ssh/known_hosts && \  
git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && \  
git clone --recursive git://github.com/Freyskeyd/dotfiles.git ~/.dotfiles && \  
ln -s ~/.dotfiles/zshrc ~/.zshrc && \  
echo 'source /etc/profile' >> ~/.zprofile && \  
ln -s ~/.dotfiles/maximum-awesome/tmux.conf ~/.tmux.conf && \  
ln -s ~/.dotfiles/maximum-awesome/tmux.conf.local ~/.tmux.conf.local && \  
ln -s ~/.dotfiles/maximum-awesome/vimrc ~/.vimrc && \  
ln -s ~/.dotfiles/maximum-awesome/vimrc.bundles ~/.vimrc.bundles && \  
ln -s ~/.dotfiles/maximum-awesome/vimrc.local ~/.vimrc.local && \  
ln -s ~/.dotfiles/maximum-awesome/vimrc.bundles.local ~/.vimrc.bundles.local
&& \  
ln -s ~/.dotfiles/maximum-awesome/vim ~/.vim && \  
git clone http://github.com/gmarik/vundle.git ~/.vim/bundle/vundle && \  
echo 'LC_ALL=en_US.UTF-8' >> ~/.zshrc && \  
echo 'LANG=C.UTF-8' >> ~/.zshrc && \  
echo 'LC_CTYPE=en_US.UTF-8' >> ~/.zshrc && \  
yes | vim +BundleInstall +qall && \  
composer global require "squizlabs/php_codesniffer=*" && \  
composer global require "phpmd/phpmd=@stable" && \  
cp ~/.composer/vendor/squizlabs/php_codesniffer/CodeSniffer.conf.dist \  
~/.composer/vendor/squizlabs/php_codesniffer/CodeSniffer.conf  
  
VOLUME ["/home/developer/.ssh", "/workspace", "/Users"]  
  
CMD ["/bin/zsh"]  

