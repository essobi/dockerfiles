FROM debian  
  
RUN apt-get update && apt-get install -y \  
vim \  
curl \  
wget \  
git \  
make \  
netcat \  
python \  
g++ \  
bzip2 \  
dnsutils \  
screen  
  
ADD https://raw.githubusercontent.com/amix/vimrc/master/vimrcs/basic.vim
~/.vimrc  
  
CMD bash  

