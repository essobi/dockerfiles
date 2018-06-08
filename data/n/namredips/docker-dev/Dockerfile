FROM ubuntu:16.04  
MAINTAINER Jeff Cox <jeff@infiquetra.com>  
  
ENV PYTHONUNBUFFERED 1  
ENV user jefcox  
  
COPY PowerlineSymbols.otf /usr/share/fonts/  
COPY 10-powerline-symbols.conf /etc/fonts/conf.d/  
  
RUN apt-get update  
RUN apt-get install -y autoconf  
RUN apt-get install -y automake  
RUN apt-get install -y libtool  
RUN apt-get install -y autotools-dev  
RUN apt-get install -y build-essential  
RUN apt-get install -y checkinstall  
RUN apt-get install -y python3  
RUN apt-get install -y wget  
RUN apt-get install -y curl  
RUN apt-get install -y python3-pip  
RUN apt-get install -y bc  
RUN apt-get install -y ncurses-dev  
RUN apt-get install -y ncurses-term  
RUN apt-get install -y git  
RUN apt-get install -y powerline  
RUN apt-get install -y python3-powerline  
RUN apt-get install -y fonts-powerline  
RUN apt-get install -y sudo  
RUN apt-get install -y vim  
RUN apt-get install -y keychain  
RUN apt-get install -y bash  
RUN apt-get install -y openconnect  
RUN apt-get install -y openvpn  
RUN pip3 install --upgrade pip  
RUN pip3 install ipython  
RUN pip3 install flake8  
RUN pip3 install pylint  
RUN pip3 install pymongo  
RUN useradd -ms /bin/bash $user  
RUN usermod -aG sudo $user  
RUN fc-cache -vf  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
USER $user  
COPY .vimrc .  
RUN git clone https://github.com/VundleVim/Vundle.vim.git
~/.vim/bundle/Vundle.vim  
RUN vim +PluginInstall +qall  
  
USER root  
COPY .bash_profile .  
COPY .tmux.conf .  
RUN chown $user:$user .bash_profile .vimrc .tmux.conf  
  
USER $user  

