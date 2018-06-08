FROM ubuntu:wily  
MAINTAINER Holger Piontek <hp9390@gmail.com>  
  
ENV GOPATH /usr/share/go/  
ENV SHELL zsh  
ENV BROWSER lynx  
ENV LANG C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
ADD aliases.zsh /root/.zsh/aliases.zsh  
ADD configs.zsh /root/.zsh/configs.zsh  
RUN chmod u+s /usr/bin/whoami  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get update --fix-missing -y && apt-get update && apt-get -y upgrade \  
&& apt-get install -y language-pack-en \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure locales  
RUN echo ":let g:session_autosave = 'no'" > /root/.vimrc  
RUN ["/bin/bash", "-c", "apt-get install -y aria2 apt-utils"]  
RUN ["/bin/bash", "-c", "apt-get install -y zsh vim-nox curl git git-flow
build-essential software-properties-common wget curl git man unzip nano tmux
colord zsh emacs gnupg2 rake exuberant-ctags httpie ruby php5"]  
RUN ["/bin/bash", "-c", "apt-get install -y pass p7zip-full sshfs supervisor
monit htop lynx-cur golang-go inetutils-ping encfs"]  
RUN ["/bin/bash", "-c", "apt-get install -y tor proxychains ncdu tor ding
trans-de-en dict dict-de-en dictd stardict stardict-plugin qstardict"]  
RUN ["/bin/bash", "-c", "apt-get install -y goldendict dictd dict-freedict-
eng-deu dict-freedict-deu-eng dict-de-en"]  
RUN ["/bin/bash", "-c", "apt-get install -y dict-freedict-deu-eng dict-
freedict-deu-fra dict-freedict-eng-fra dict-freedict-deu-ita dict-freedict-
eng-rus dict-freedict-eng-rus dict-freedict-eng-deu"]  
ADD
https://raw.githubusercontent.com/haad/proxychains/master/src/proxychains.conf
/etc/proxychains.conf  
RUN ["/bin/bash", "-c", "add-apt-repository -y ppa:ubuntu-desktop/ubuntu-
make"]  
RUN ["/bin/bash", "-c", "apt-get update"]  
RUN ["/bin/bash", "-c", "apt-get install -y ubuntu-make w3m procmail ssmtp
mutt irssi weechat weechat-curses weechat-plugins weechat-scripts weechat-
doc"]  
RUN ["/bin/bash", "-c", "curl -sS https://getcomposer.org/installer | php --
--install-dir=/usr/local/bin --filename=composer"]  
RUN ["/bin/bash", "-c", "curl -LsS http://symfony.com/installer -o
/usr/local/bin/symfony"]  
RUN ["/bin/bash", "-c", "composer global require 'laravel/installer=~1.1'"]  
RUN ["/bin/bash", "-c", "chmod a+x /usr/local/bin/symfony"]  
RUN ["/bin/bash", "-c", "curl -sL https://deb.nodesource.com/setup_5.x | bash
-"]  
RUN apt-get install -y nodejs  
RUN ["/bin/bash", "-c", "curl -O https://bootstrap.pypa.io/get-pip.py"]  
RUN ["/bin/bash", "-c", "python get-pip.py"]  
RUN ["/bin/bash", "-c", "pip install awscli"]  
RUN ["/bin/bash", "-c", "yes s | sh <(curl -fsSL
https://raw.githubusercontent.com/skwp/dotfiles/master/install.sh) -m"]  
RUN ["/bin/bash", "-c", "bash <(curl -L
https://raw.githubusercontent.com/kepbod/ivim/master/setup.sh) -m"]  
RUN ["/bin/bash", "-c", "echo 'for config_file ($HOME/.zsh/*.zsh) source
$config_file' >> /root/.zshrc"]  
RUN ["/bin/bash", "-c", "apt-get install -y dict-freedict-all rng-tools build-
essential libglib2.0-dev libssl-dev libcurl4-openssl-dev
libgirepository1.0-dev megatools build-essential libssl-dev pkg-config
libprotobuf-dev protobuf-compiler qt5-qmake qt5-default qtbase5-dev
qttools5-dev-tools qtdeclarative5-dev qtmultimedia5-dev qml-module-qtquick-
controls qml-module-qtquick-dialogs qml-module-qtmultimedia"]  
RUN ["/bin/bash", "-c", "git clone https://github.com/ricochet-im/ricochet.git
&& (cd ricochet && qmake DEFINES+=RICOCHET_NO_PORTABLE && make && make
install)"]  
RUN ["/bin/bash", "-c", "apt-get install -y openssl libcurl4-openssl-dev
libxml2 libssl-dev libxml2-dev pinentry-curses xclip source-highlight docbook
latex-cjk-all opensp texlive-lang-all texlive-lang-cyrillic texlive-xetex
transfig docbook-dsssl-doc dbtoepub fop libsaxon-java libxslthl-java xalan
sgmls-doc perl-tk latexmk chktex lacheck latexdiff xindy purifyeps fragmaster
dvidvi dvipng psutils libspreadsheet-parseexcel-perl dot2tex prerex xmltex
asciidoc"]  
RUN ["/bin/bash", "-c", "git clone https://github.com/lastpass/lastpass-
cli.git && (cd lastpass-cli && make && make install && make install-doc)"]  
  
WORKDIR /root/  
ENTRYPOINT ["/bin/zsh"]  

