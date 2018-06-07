FROM ubuntu:16.04  
MAINTAINER jizhilong <zhilongji@gamil.com>  
  
  
RUN apt-get update &&\  
apt-get install -y python vim\  
ctags openssh-client\  
build-essential python2.7-dev\  
net-tools iproute2 wget\  
curl git zsh tmux  
  
RUN curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh | zsh || true  
  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 &&\  
chmod +x /usr/local/bin/dumb-init  
  
RUN wget https://bootstrap.pypa.io/get-pip.py &&\  
python get-pip.py && rm -f get-pip* && \  
pip install jupyter  
  
ADD .vimrc /root/.vimrc  
ADD vim-plugins /root/.vim/vim-plugins  
ADD install-vim-plugins.sh /usr/bin/install-vim-plugins  
  
RUN mkdir -p ~/.vim/autoload ~/.vim/bundle && \  
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim &&\  
install-vim-plugins  
  
ADD sources.list /etc/apt/sources.list  
ADD pip.conf /root/.pip/pip.conf  
ADD .tmux.conf /root/.tmux.conf  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
CMD zsh  

