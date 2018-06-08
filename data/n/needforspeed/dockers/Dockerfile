FROM debian:latest  
  
MAINTAINER Yuncong Zhang <njitzyc@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
gcc g++ make cmake build-essential \  
python python-dev \  
git \  
locales \  
vim-nox \  
nano \  
zsh \  
curl \  
lynx \  
tmux > /dev/null && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# create the docker user  
RUN groupadd docker && useradd -d /home/docker -s /bin/zsh -m -g docker docker  
  
# install nodejs  
# gpg keys listed at https://github.com/nodejs/node  
RUN for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 5.9.1  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
VOLUME ["/data"]  
  
# setup oh-my-zsh  
USER docker  
WORKDIR /home/docker  
RUN touch .zshrc  
ENV TERM=xterm  
ENV PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin  
RUN bash -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-
my-zsh/master/tools/install.sh)"  
  
# get configs  
RUN curl -fsSL
https://raw.githubusercontent.com/needforspeed/configs/master/.vimrc -O && \  
curl -fsSL
https://raw.githubusercontent.com/needforspeed/configs/master/.tern-config -O
&& \  
curl -fsSL
https://raw.githubusercontent.com/needforspeed/configs/master/.tmux.conf -O  
  
# setup vim plugins  
RUN mkdir -p .vim/bundle && \  
git clone \--depth 1 https://github.com/VundleVim/Vundle.vim.git
~/.vim/bundle/Vundle.vim && \  
git clone \--depth 1 https://github.com/ternjs/tern_for_vim.git
.vim/bundle/tern_for_vim && \  
cd .vim/bundle/tern_for_vim && \  
npm i > /dev/null && \  
cd && \  
git clone \--depth 1 https://github.com/Valloric/YouCompleteMe.git
.vim/bundle/YouCompleteMe && \  
cd .vim/bundle/YouCompleteMe && \  
git submodule update --init --recursive && \  
./install.py --clang-completer --tern-completer > /dev/null && \  
rm -rf .git third_party/ycmd/cpp third_party/ycmd/clang_includes
third_party/ycmd/clang_archives && \  
cd && \  
vim -E -u NONE -S ~/.vimrc +PluginInstall +qall > /dev/null; exit 0  
  
CMD ["/bin/zsh"]  

