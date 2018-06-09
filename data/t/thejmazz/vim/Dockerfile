FROM ubuntu:16.04  
# Install system packages  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install vim git curl build-essential cmake python-dev python3-dev
-y  
  
# Install node for ternjs  
RUN mkdir /usr/local/node  
RUN curl -O https://nodejs.org/dist/v6.7.0/node-v6.7.0-linux-x64.tar.xz  
RUN tar -xJf node-v6.7.0-linux-x64.tar.xz --strip-components=1 -C
/usr/local/node  
RUN rm node-v6.7.0-linux-x64.tar.xz  
  
# Install yadm  
RUN curl -sfLo /usr/local/bin/yadm
https://github.com/TheLocehiliosan/yadm/raw/master/yadm && chmod a+x
/usr/local/bin/yadm  
  
# Make a node group which owns /usr/local/node  
RUN groupadd -r node && useradd -r -g node node  
RUN chown node:node /usr/local/node  
  
# Main user  
RUN groupadd -r vim && useradd -r -g vim vim  
RUN usermod -aG node vim  
RUN mkdir -p /home/vim  
ENV PATH $PATH:/usr/local/node/bin  
RUN chown -R vim:vim /home/vim  
  
# Do the rest as vim user so repos and .git are not owned by root  
USER vim  
  
# Download dotfiles (specifically .vimrc)  
RUN yadm clone https://github.com/thejmazz/dotfiles  
  
# Clone Vundle  
RUN git clone https://github.com/VundleVim/Vundle.vim
/home/vim/.vim/bundle/Vundle.vim  
  
# Install plugins, hiding output. see  
# - https://github.com/VundleVim/Vundle.vim/issues/511#issuecomment-134251209  
# - http://superuser.com/questions/873890/can-i-get-vim-to-install-bundles-
and-close-in-the-background  
RUN vim -E -u NONE -S ~/.vimrc +PluginInstall +qall > /dev/null  
  
# Compile YCM  
RUN /home/vim/.vim/bundle/YouCompleteMe/install.py  
# Install tern and tern-node-express  
RUN cd
/home/vim/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/tern_runtime
&& npm install --production && npm install tern-node-express  
# Need to remove tern from tern-node-express' node_modules. see:
https://github.com/angelozerr/tern-node-
express/issues/17#issuecomment-236537137  
RUN rm -rf
/home/vim/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/tern_runtime/node_modules/tern-
node-express/node_modules/tern  
  
RUN mkdir /home/vim/work  
WORKDIR /home/vim/work  

