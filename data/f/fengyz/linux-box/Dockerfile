FROM ubuntu:16.04  
MAINTAINER Yizhi FENG "yizhi.feng@gmail.com"  
ADD aliyun.list /etc/apt/sources.list  
ENV REFRESHED_AT 2016-08-14  
RUN apt-get update  
RUN apt-get install -y --fix-missing \  
build-essential libevent-dev libncurses5-dev \  
libtool libtool-bin autoconf \  
python-dev python-pip python3-dev python3-pip \  
software-properties-common python-software-properties \  
zsh wget curl vim emacs editorconfig \  
aspell aspell-en man-db tree cmake \  
git git-core \  
nodejs npm \  
imagemagick \  
curl zlib1g-dev libssl-dev libreadline-dev \  
libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev \  
libcurl4-openssl-dev libffi-dev  
  
# config zsh with oh-my-zsh  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git /root/.oh-my-zsh  
  
# install tmux  
RUN mkdir /root/tmp  
ADD downloads/tmux-2.2.tar.gz /root/tmp/  
WORKDIR /root/tmp/tmux-2.2  
RUN ./configure && make && make install && rm -rf /root/tmp/  
# set work dir to /root  
WORKDIR /root  
# install percol  
RUN pip install percol  
# set language  
ENV LANG=C.UTF-8  
# set local timezone  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
WORKDIR /root  
# install ruby & rails  
RUN git clone git://github.com/sstephenson/rbenv.git .rbenv  
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> .zshrc && echo 'eval
"$(rbenv init -)"' >> ~/.zshrc  
RUN git clone git://github.com/sstephenson/ruby-build.git .rbenv/plugins/ruby-
build  
RUN echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> .zshrc  
RUN ["/bin/zsh", "-c","source ~/.zshrc && rbenv install -v 2.4.0 && rbenv
global 2.4.0"]  
RUN ["/bin/zsh", "-c","source ~/.zshrc && echo \"gem: --no-document\" >
.gemrc"]  
RUN ["/bin/zsh", "-c","source ~/.zshrc && gem update --system"]  
RUN ["/bin/zsh", "-c","source ~/.zshrc && gem sources --remove
https://rubygems.org/ --add https://gems.ruby-china.org/"]  
RUN ["/bin/zsh", "-c","source ~/.zshrc && rbenv rehash"]  
RUN ["/bin/zsh", "-c","source ~/.zshrc && gem install rails -v 5.1.4"]  
  
# install clang 3.8  
RUN echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-3.9 main" >>
/etc/apt/sources.list  
RUN echo "deb-src http://apt.llvm.org/xenial/ llvm-toolchain-xenial-3.9 main"
>> /etc/apt/sources.list  
RUN apt-get update  
RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add -  
RUN apt-get install -y --allow-unauthenticated \  
clang-3.9 clang-3.9-doc libclang-common-3.9-dev libclang-3.9-dev \  
libclang1-3.9 libclang1-3.9-dbg libllvm-3.9-ocaml-dev libllvm3.9
libllvm3.9-dbg \  
lldb-3.9 llvm-3.9 llvm-3.9-dev llvm-3.9-doc llvm-3.9-examples llvm-3.9-runtime
\  
clang-format-3.9 python-clang-3.9  
  
# install spf-13 vim configuration  
ENV REFRESHED_AT 2016-08-14  
ADD .vimrc.before.local /root/  
ADD .vimrc.bundles.local /root/  
RUN curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh  
  
# install and config YCM  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN cd /root/.vim/bundle/YouCompleteMe/ && ./install.py --clang-completer
--tern-completer  
RUN npm install -g typescript  
  
# add config files  
ADD .vimrc.local /root/  
ADD .editorconfig /  
# makeshift, .zshrc should be copied in place before building ruby  
ADD .zshrc /root/.zshrc_tmp  
RUN cat /root/.zshrc_tmp /root/.zshrc > /root/.zshrc_new && rm
/root/.zshrc_tmp && mv /root/.zshrc_new /root/.zshrc  
# my zsh-theme  
ADD fengyz.zsh-theme /root/.oh-my-zsh/themes/  
# tmux configuration  
ADD .tmux.conf /root/  
# git configuration  
ADD .gitconfig /root/  
# enter zsh  
RUN chsh -s /bin/zsh  
CMD ["/bin/zsh"]  
  
EXPOSE 3000  
# install ipython/jupyter/iruby  
RUN apt-get install -y python-virtualenv libzmq3-dev  
RUN virtualenv -p python3 venv  
RUN ["/bin/zsh", "-c","source /root/venv/bin/activate"]  
RUN pip3 install 'ipython[notebook]'  
RUN ["/bin/zsh", "-c","source ~/.zshrc && gem install rbczmq"]  
RUN ["/bin/zsh", "-c","source ~/.zshrc && gem install iruby"]  
# install python2 kernel  
RUN pip install --upgrade pip  
RUN pip install 'ipython[notebook]'  
RUN ipython2 kernel install  
# install bash kernel  
RUN pip3 install bash_kernel  
RUN python3 -m bash_kernel.install  
  
# install javascript kernel to jupyter  
RUN npm install -g ijavascript  
RUN ijs --ijs-install-kernel  
  
# register ruby kernel, so that we can use jupyter instead of iruby in CLI  
RUN ["/bin/zsh", "-c","source ~/.zshrc && iruby register"]  
  
# add percol key map  
ADD percol_d_rc.py /root/.percol.d/rc.py  
  
# cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

