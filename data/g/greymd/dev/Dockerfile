FROM ubuntu:16.04  
MAINTAINER Yamada, Yasuhiro <greengregson@gmail.com>  
ENV DEBFULLNAME="Yamada, Yasuhiro" DEBEMAIL=greengregson@gmail.com  
  
# Prepare sudo  
RUN apt update && apt install -y sudo  
  
# Add a non-root user  
RUN useradd -m -d /home/docker -s /bin/bash docker && \  
echo "docker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
USER docker  
ENV HOME /home/docker  
ENV USER_NAME docker  
WORKDIR /home/docker  
  
# ------------------  
# Install Basic softwares  
# ------------------  
RUN sudo apt install -y locales && \  
sudo localedef -f UTF-8 -i ja_JP ja_JP.utf8 && \  
sudo apt install -y git vim curl make netcat libreadline-dev nkf bc expect
tree inotify-tools sl jq dnsutils \  
# In order to develop debian package (Ref:
http://www.rain.hyarc.nagoya-u.ac.jp/~satoki/main/Linux/configure/make_deb.html).  
dh-make fakeroot pbuilder \  
# For PPA  
software-properties-common  
  
# ------------------  
# Install Egison  
# ------------------  
RUN sudo apt install -y haskell-platform libncurses-dev && \  
cabal update && \  
cabal install egison egison-tutorial  
  
# ------------------  
# Install Ruby  
# ------------------  
RUN sudo apt install -y build-essential libssl-dev libffi-dev libreadline-dev
&& \  
git clone https://github.com/sstephenson/rbenv.git $HOME/.rbenv && \  
git clone https://github.com/sstephenson/ruby-build.git
$HOME/.rbenv/plugins/ruby-build && \  
$HOME/.rbenv/bin/rbenv install 2.5.0 && \  
$HOME/.rbenv/bin/rbenv global 2.5.0 && \  
$HOME/.rbenv/shims/gem install cureutils gist snacknomama matsuya  
  
# ------------------  
# Install zplug  
# ------------------  
RUN sudo apt install -y zsh python && \  
export ZPLUG_HOME=$HOME/.zplug && \  
git clone https://github.com/zplug/zplug $ZPLUG_HOME  
  
# ------------------  
# Install universal-ctags  
# ------------------  
# Ref: https://github.com/universal-ctags/ctags/blob/master/docs/autotools.rst  
RUN sudo apt install -y dh-autoreconf pkg-config && \  
git clone https://github.com/universal-ctags/ctags.git $HOME/repos/universal-
ctags/ctags && \  
cd $HOME/repos/universal-ctags/ctags && \  
./autogen.sh && \  
./configure && \  
make && \  
sudo make install  
  
# ------------------  
# Install Go  
# ------------------  
RUN cd $HOME && \  
mkdir $HOME/.go && \  
curl -L https://storage.googleapis.com/golang/go1.10.linux-amd64.tar.gz | tar
zxv && \  
sudo mv go /usr/local && \  
ls /usr/local/go/bin/ | sed 's;.*;sudo ln -s /usr/local/go/bin/&
/usr/local/bin/&;' | sh  
  
# ------------------  
# Install pt  
# ------------------  
RUN cd $HOME && \  
curl -L
https://github.com/monochromegane/the_platinum_searcher/releases/download/v2.1.5/pt_linux_amd64.tar.gz
| tar zxv && \  
sudo cp pt_linux_amd64/pt /usr/local/bin && \  
rm -rf pt_linux_amd64  
  
# ------------------  
# Install fzy  
# ------------------  
RUN cd $HOME && \  
sudo apt install -y wget && \  
wget
https://github.com/jhawthorn/fzy/releases/download/0.8/fzy_0.8-1_amd64.deb &&
\  
sudo dpkg -i fzy_0.8-1_amd64.deb && \  
rm fzy_0.8-1_amd64.deb  
  
# ------------------  
# Install GlueLang  
# ------------------  
RUN cd $HOME && \  
sudo apt install -y g++ && \  
git clone https://github.com/ryuichiueda/GlueLang.git && \  
cd GlueLang && \  
make && \  
sudo make install && \  
cd $HOME && \  
rm -rf GlueLang  
  
# ------------------  
# Install Tmux related softwares  
# ------------------  
RUN sudo apt install -y libevent-dev ncurses-dev && \  
export TMUX_VERSION=2.5 && \  
curl -L
"https://github.com/tmux/tmux/releases/download/${TMUX_VERSION}/tmux-${TMUX_VERSION}.tar.gz"
| tar zxv && \  
cd tmux-${TMUX_VERSION} && \  
curl -L
https://raw.githubusercontent.com/silenvx/PKGBUILD/master/tmux/borders.patch >
borders.patch && \  
patch tty-acs.c < borders.patch && \  
./configure; make && \  
sudo make install && \  
cd .. && rm -rf tmux-${TMUX_VERSION} && \  
git clone https://github.com/tmux-plugins/tpm $HOME/.tmux/plugins/tpm  
  
# ------------------  
# Install xpanes  
# ------------------  
RUN curl https://raw.githubusercontent.com/greymd/tmux-
xpanes/master/bin/xpanes | sudo tee /usr/bin/xpanes > /dev/null && \  
sudo chmod +x /usr/bin/xpanes  
  
# ------------------  
# Install Node environment  
# ------------------  
RUN git clone "git://github.com/creationix/nvm.git" $HOME/.nvm && \  
bash -c 'source $HOME/.nvm/nvm.sh && nvm install v8.1.4 && npm install
--global yarn faker-cli emspect'  
  
# ------------------  
# Installing useful commands  
# ------------------  
RUN mkdir "$HOME/bin" && \  
git clone https://github.com/ShellShoccar-jpn/Parsrs.git "$HOME/Parsrs" && \  
bash -c 'ls $HOME/Parsrs/*.sh | while read f;do cp "$f" "$HOME/bin/$(basename
${f%.sh})";done' && \  
rm -rf "$HOME/Parsrs"  
  
# ------------------  
# Install heroku  
# ------------------  
RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh  
  
# ------------------  
# Install eclim requirements  
# ------------------  
RUN sudo apt install -y xvfb x11vnc x11-xkb-utils xfonts-100dpi xfonts-75dpi
xfonts-scalable xfonts-cyrillic x11-apps \  
wget curl git gcc make zip libswt-gtk-3-jni && \  
curl -s "https://get.sdkman.io" | bash && \  
bash -c 'source "$HOME/.sdkman/bin/sdkman-init.sh" && sdk install java
9ea13-zulu && sdk install java 8u131-zulu && sdk use java 8u131-zulu && sdk
install gradle 4.0.1 && sdk install ant 1.10.1 && sdk install maven 3.5.0'  
  
# ------------------  
# Set dotfiles  
# ------------------  
RUN mkdir -p $HOME/repos/greymd && \  
git clone https://github.com/greymd/dotfiles.git $HOME/repos/greymd/dotfiles
&& \  
cd $HOME/repos/greymd/dotfiles && \  
# Delete existing dotfiles  
ls -a | grep '^\\.' | grep -vFw '.' | grep -v '^\\.git$' | sed 's|^|rm -f
$HOME/|' | sh && \  
# Set links  
ls -a | grep '^\\.' | grep -v '^\\.git$' | grep -vwF '.' | sed 's/^.*/echo ln
-s $(pwd)\/& $HOME\/&/' | sh | sh  
  
# ------------------  
# Install antigen  
# ------------------  
RUN mkdir -p $HOME/repos/zsh-users/antigen && \  
git clone https://github.com/zsh-users/antigen.git $HOME/repos/zsh-
users/antigen  
  
# Install antigen plugins  
RUN zsh --rcs $HOME/.zshrc -c 'antigen-update'  
  
# ------------------  
# Vim settings  
# ------------------  
RUN sudo apt install -y vim && \  
mkdir -p $HOME/.cache/dein && \  
curl -L
https://raw.githubusercontent.com/Shougo/dein.vim/master/bin/installer.sh >
$HOME/installer.sh && \  
sh $HOME/installer.sh $HOME/.cache/dein && \  
rm $HOME/installer.sh  
# Install dein plugins  
RUN yes | vim -c ":silent call dein#install() | :q"  
# Create vimproc_linux64.so for vimproc  
RUN cd $HOME/.cache/dein/repos/github.com/Shougo/vimproc.vim && \  
make  
  
# ------------------  
# Installing Eclipse & eclim  
# ------------------  
ENV JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF8"  
ENV DISPLAY :1  
ENV WORKSPACE /home/docker/workspace  
  
RUN cd $HOME && \  
mkdir -p $WORKSPACE && \  
mkdir -p $HOME/.vim && \  
curl -L
"http://ftp.jaist.ac.jp/pub/eclipse/technology/epp/downloads/release/oxygen/R/eclipse-
jee-oxygen-R-linux-gtk-x86_64.tar.gz" | tar zxv && \  
wget
"https://github.com/ervandew/eclim/releases/download/2.7.0/eclim_2.7.0.jar" &&
\  
bash -c 'source "$HOME/.sdkman/bin/sdkman-init.sh" && java
-Dvim.files=$HOME/.vim -Declipse.home=$HOME/eclipse -jar $HOME/eclim_2.7.0.jar
install' && \  
rm $HOME/eclim_2.7.0.jar  
  
# # ------------------  
# # Installing Lombok for eclipse  
# # ------------------  
# RUN printf "%s" "-Xbootclasspath/a:lombok.jar -javaagent:lombok.jar" | xargs
-n 1 >> $HOME/eclipse/eclipse.ini && \  
# wget https://projectlombok.org/downloads/lombok.jar -O
$HOME/eclipse/lombok.jar  
# ------------------  
# Install Network related tools  
# ------------------  
RUN sudo apt install -y tcpdump iputils-ping ngrep  
  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
# Cleaning  
RUN sudo apt clean && \  
sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD if ( type Xvfb > /dev/null 2>&1 ) && ! ( ps alx | grep -wq '[X]vfb' )
;then nohup Xvfb :1 -screen 0 1024x768x24 &> /dev/null & fi; zsh -c 'tmux -2'  

