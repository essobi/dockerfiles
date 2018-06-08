FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y vim curl git build-essential python  
RUN curl -fsSL https://get.docker.com/ | sh  
  
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -  
RUN apt-get install -y nodejs && npm install -g n && n 4.4.7 && npm config set
save-exact=true  
  
ADD .vimrc /root/  
RUN git clone https://github.com/VundleVim/Vundle.vim.git
/root/.vim/bundle/Vundle.vim  
RUN vim +PluginInstall +qall  
  
ADD git-completion.bash /root/  
ADD .bashrc /root/  
  
WORKDIR /workspace  
  
ENTRYPOINT /bin/bash  

