# docker build -t shunsuke89/ubuntu-desktop .  
FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y zsh  
  
# ユーザの作成  
RUN useradd -m ubuntu -s /usr/bin/zsh  
RUN echo ubuntu:password | chpasswd  
RUN gpasswd -a ubuntu sudo  
  
WORKDIR /home/ubuntu  
  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository ppa:git-core/ppa  
RUN apt-get update  
RUN apt-get install -y git  
  
RUN apt-get install -y aptitude  
RUN apt-get install -y wget  
RUN apt-get install -y curl  
RUN apt-get install -y build-essential  
RUN apt-get install -y aptitude  
RUN apt-get install -y golang  
RUN apt-get install -y openjdk-7-jdk  
RUN apt-get install -y man-db  
RUN apt-get install -y haskell-platform  
  
RUN apt-get build-dep -y python2.7  
RUN apt-get build-dep -y python3.4  
  
RUN apt-get install -y mercurial  
RUN apt-get build-dep -y vim  
RUN apt-get install -y libluajit-5.1-dev  
RUN apt-get install -y luajit  
RUN apt-get build-dep -y nodejs  
RUN apt-get build-dep -y ruby  
RUN apt-get install -y silversearcher-ag  
  
USER ubuntu  
WORKDIR /home/ubuntu  
RUN mkdir work .vimundo data  
  
WORKDIR /home/ubuntu/work  
RUN hg clone https://vim.googlecode.com/hg/ vim  
WORKDIR vim  
RUN ./configure --enable-luainterp=yes --with-lua-prefix=/usr --enable-
pythoninterp --enable-multibyte --enable-xim --with-gnome --with-x  
RUN make -j4  
RUN make test  
  
# Node.jsは古いのでソースからインストール  
WORKDIR /home/ubuntu/work  
RUN wget https://nodejs.org/dist/latest-v0.12.x/node-v0.12.7.tar.gz  
RUN tar xvzf node-v0.12.7.tar.gz  
WORKDIR node-v0.12.7  
RUN ./configure  
RUN make -j4  
# RUN make test  
WORKDIR /home/ubuntu  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git .oh-my-zsh  
RUN git clone https://github.com/yyuu/pyenv.git .pyenv  
RUN git clone https://github.com/sstephenson/rbenv.git .rbenv  
  
RUN mkdir -p gh/kics gl/suzuki-shunsuke  
  
WORKDIR gh/kics  
RUN git clone https://github.com/kics/vim-conf.git  
RUN ln -s /home/ubuntu/gh/kics/vim-conf/.vim /home/ubuntu/.vim  
RUN ln -s /home/ubuntu/gh/kics/vim-conf/.vimrc /home/ubuntu/.vimrc  
RUN ln -s /home/ubuntu/gh/kics/vim-conf/.vimshrc /home/ubuntu/.vimshrc  
RUN git clone https://github.com/kics/zsh-config.git  
RUN ln -s /home/ubuntu/gh/kics/zsh-config/.zshrc /home/ubuntu/.zshrc  
  
USER root  
  
WORKDIR /home/ubuntu/work/vim  
RUN make install  
  
WORKDIR /home/ubuntu/work/node-v0.12.7  
RUN make install  
  
WORKDIR /home/ubuntu/work  
RUN npm install -g grunt-cli gulp bower jsonlint  
  
USER ubuntu  
  
RUN curl -L
https://raw.githubusercontent.com/Shougo/neobundle.vim/master/bin/install.sh |
sh  
  
WORKDIR /home/ubuntu  

