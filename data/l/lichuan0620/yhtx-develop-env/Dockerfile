############################################################  
# Dockerfile - 通用开发环境  
# 版本：2018-05-16  
# 北京云汇天下科技有限公司  
############################################################  
  
FROM centos:7.4.1708  
  
# 李传，13701083998，lichuan@chainedbox.com  
MAINTAINER Chuan Li  
  
WORKDIR /root  
ENV HOME /root  
  
  
############################################################  
# 操作系统配置  
############################################################  
  
## 时区  
RUN echo "TZ='Asia/Shanghai'; export TZ" >> /etc/profile  
  
## ELEP (Extra Packages for Enterprise Linux)  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
# 最新版本可在这里找到：http://dl.fedoraproject.org/pub/epel/  
  
## root密码  
RUN echo hello|passwd --stdin root  
  
## SSH  
RUN yum install -y openssh-server \  
&& ssh-keygen -N '' -t rsa -q -f /etc/ssh/ssh_host_rsa_key \  
&& ssh-keygen -N '' -t dsa -q -f /etc/ssh/ssh_host_dsa_key \  
&& echo "PermitRootLogin yes" >> /etc/ssh/sshd_config \  
&& sed -i -E "s/UsePAM yes/#UsePAM yes/" /etc/ssh/sshd_config \  
&& sed -i -E "s/#UsePAM no/UsePAM no/" /etc/ssh/sshd_config  
CMD ["/usr/sbin/sshd","-D"]  
  
  
############################################################  
# 开发工具  
############################################################  
  
RUN yum install -y \  
zsh \  
which \  
git \  
wget \  
tar \  
ntp \  
ntpdate \  
mysql \  
gcc \  
ncurses-devel \  
gcc-c++ \  
make \  
cmake \  
automake \  
python-devel \  
ctags \  
ruby \  
libevent \  
libevent-devel \  
&& yum clean all  
  
########################## 配置 ##########################  
  
RUN git clone "https://github.com/CoffeyGit/config-files" \  
&& ln -s config-files/.vimrc . \  
&& ln -s config-files/.tmuxinator . \  
&& ln -s config-files/.tmux.conf . \  
&& ln -s config-files/.gitconfig . \  
&& ln -s config-files/.tmuxinator.zsh . \  
&& ln -s config-files/.zshrc . \  
&& mv .bashrc .bashrc.old \  
&& ln -s config-files/.bashrc .  
  
######################### Go和Go相关 ##########################  
  
RUN wget https://dl.google.com/go/go1.8.6.linux-amd64.tar.gz \  
&& tar -C /usr/local -xzvf go1.8.6.linux-amd64.tar.gz \  
&& rm -f go1.8.6.linux-amd64.tar.gz  
  
RUN mkdir -p go/{src,bin,pkg,conf}  
  
COPY gocode \  
golint \  
gotags \  
errcheck \  
godef \  
goimports \  
gorename \  
oracle \  
go/bin/  
  
RUN ["/bin/bash","-c","-l","go get github.com/go-sql-driver/mysql"]  
  
RUN git clone "https://github.com/go-yaml/yaml.git" "go/src/gopkg.in/yaml.v2"
\  
&& cp -R go/src/gopkg.in/yaml.v2 go/src/gopkg.in/yaml.v1 \  
&& cd go/src/gopkg.in/yaml.v1 \  
&& git checkout -b v1 origin/v1  
  
  
RUN git clone "https://github.com/go-yaml/yaml.git"
"/usr/local/go/src/gopkg.in/yaml.v2" \  
&& cp -R /usr/local/go/src/gopkg.in/yaml.v2 /usr/local/go/src/gopkg.in/yaml.v1
\  
&& cd /usr/local/go/src/gopkg.in/yaml.v1 \  
&& git checkout -b v1 origin/v1  
  
############################ tmux ############################  
  
COPY tmux-2.0.tar.gz ./  
  
RUN tar -xzvf tmux-2.0.tar.gz \  
&& rm -f tmux-2.0.tar.gz \  
&& cd tmux-2.0 \  
&& ./configure \  
&& make \  
&& make install  
  
  
######################### ruby + gem #########################  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 \  
&& curl -sSL https://get.rvm.io |bash -s stable --ruby \  
&& echo "source /etc/profile" >> /etc/zprofile  
#RUN ["/bin/bash","-c","-l","rvm use 2.2.1"]  
#RUN ["/bin/bash","-c","-l","gem sources --remove https://rubygems.org/"]  
#RUN ["/bin/bash","-c","-l","gem sources -a https://ruby.taobao.org/"]  
RUN ["/bin/bash","-c","-l","gem install tmuxinator"]  
  
################## oh-my-zsh ######################  
RUN git clone git://github.com/bwithem/oh-my-zsh.git ~/.oh-my-zsh \  
# && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \  
&& chsh -s /bin/zsh  
#RUN sed -i -E "s/^plugins=\\((.*)\\)$/plugins=(\1 tmux themes tmuxinator)/"
~/.zshrc  
  
####### vim #############  
COPY vim-7.4.tar.bz2 ./  
RUN tar -xjvf vim-7.4.tar.bz2 \  
&& rm -f vim-7.4.tar.bz2 \  
&& cd vim74 \  
&& ./configure --with-features=huge --enable-multibyte --enable-xim --with-x
--enable-pythoninterp=yes --enable-cscope --enable-fontset --with-python-
config-dir=/usr/lib64/python2.6/config \  
&& make \  
&& make install \  
&& git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle \  
&& git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
\  
&& git clone "https://github.com/SirVer/ultisnips.git" ~/.vim/bundle/ultisnips
\  
&& git clone "https://github.com/motemen/git-vim.git" ~/.vim/bundle/git-vim \  
&& git clone "https://github.com/tpope/vim-fugitive.git" ~/.vim/bundle/vim-
fugitive \  
&& git clone "https://github.com/majutsushi/tagbar.git" ~/.vim/bundle/tagbar \  
&& git clone "https://github.com/fatih/vim-go.git" ~/.vim/bundle/vim-go \  
&& git clone "https://github.com/bling/vim-airline.git" ~/.vim/bundle/vim-
airline \  
&& git clone "https://github.com/fannheyward/rainbow_parentheses.vim.git"
~/.vim/bundle/rainbow_parentheses.vim \  
&& rm /bin/vi \  
&& ln -s /usr/local/bin/vim /bin/vi  
  
########## YouCompleteMe ################  
RUN git clone "https://github.com/Valloric/YouCompleteMe.git"
.vim/bundle/YouCompleteMe \  
&& cd .vim/bundle/YouCompleteMe \  
&& git submodule update --init --recursive  
RUN ["/bin/bash","-c","-l","cd .vim/bundle/YouCompleteMe;./install.sh
--gocode-completer"]

