FROM mcranmer/dockers:cuda-buildpack  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
vim-nox-py2 \  
zsh \  
manpages-posix \  
manpages-posix-dev  
  
WORKDIR /tmp  
  
RUN curl -fSsL -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
RUN wget
https://raw.githubusercontent.com/MilesCranmer/bootstrap/master/bootstrap.sh
&& \  
chmod +x bootstrap.sh && ./bootstrap.sh  
  
WORKDIR /workspace  
  
CMD ["/bin/zsh"]  

