FROM ubuntu  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninterective apt-get install -y \  
vim-youcompleteme \  
clang \  
python3-dev \  
python-dev \  
exuberant-ctags \  
cmake \  
build-essential \  
bash-completion \  
git \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root/  
  
COPY vimconfig/.vimrc /root/  
  
RUN \  
curl -fLo /root/.vim/autoload/plug.vim --create-dirs \  
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim  
RUN vim +PlugInstall +qall  

