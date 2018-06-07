FROM slogsdon/develop-base  
  
RUN \  
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
575159689BEFB442 &&\  
echo 'deb http://download.fpcomplete.com/debian jessie main' | sudo tee
/etc/apt/sources.list.d/fpco.list &&\  
sudo apt-get update &&\  
sudo apt-get install -y \  
stack \  
libgmp-dev \  
xz-utils \  
zlib1g-dev \  
&&\  
stack setup &&\  
stack install alex &&\  
stack install ghc-mod &&\  
stack install happy &&\  
stack install hdevtools &&\  
stack install hlint  
  
ENV PATH $HOME/.local/bin:$PATH  

