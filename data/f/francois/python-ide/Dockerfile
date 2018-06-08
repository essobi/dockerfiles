# Base docker image  
FROM debian:jessie  
MAINTAINER François Billant <fbillant@gmail.com>  
  
RUN sed -i.bak 's/jessie main/jessie main contrib non-free/g'
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y \  
tmux \  
git \  
vim-nox \  
python-dev \  
python-pip  
  
RUN cd /root && \  
git clone \--recursive https://github.com/FrancoisBillant/dotfiles.git && \  
cp -r /root/dotfiles/. /root && \  
rm -Rf /root/scripts && \  
rm -Rf /root/dotfiles && \  
rm -f /root/README.md  
  
# Install YouCompleteMe plugin  
RUN apt-get install -y python-dev build-essential cmake && \  
cd /root/.vim/bundle && \  
git clone https://github.com/Valloric/YouCompleteMe.git && \  
cd YouCompleteMe && \  
git submodule update --init --recursive && \  
./install.sh  
  
# Add YCM config to .vimrc  
RUN echo '\"YCM options \n\  
let g:ycm_autoclose_preview_window_after_completion=1 \n\  
map <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>\n' \  
>> /root/.vimrc  
  

