FROM python:3.5  
MAINTAINER Jonathan Foster <jxf9099@rit.edu>  
  
WORKDIR /usr/src/app  
  
RUN apt-get update && apt-get install -y \  
tmux vim git  
  
# setup git  
RUN git config --global user.email "jxf9099@rit.edu"  
RUN git config --global user.name "Jonathan Foster"  
  
# getting my dot files into place  
RUN git clone https://github.com/fostertheweb/dotfiles ~/.vim  
RUN mv ~/.vim/tmux.conf ~/.tmux.conf  
RUN mv ~/.vim/vimrc ~/.vimrc  
  
# download VimPlug  
RUN sh ~/.vim/install.sh  
  
CMD ["/bin/bash"]  
  

