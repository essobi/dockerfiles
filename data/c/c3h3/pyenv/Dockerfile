FROM debian:jessie  
  
MAINTAINER Chia-Chi Chang <c3h3.tw@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV HOME /root  
ENV PYENVPATH $HOME/.pyenv  
ENV PATH $PYENVPATH/shims:$PYENVPATH/bin:$PATH  
  
RUN apt-get update && apt-get -y install git-core build-essential gfortran
sudo make cmake libssl-dev zlib1g-dev libbz2-dev libreadline-dev
libsqlite3-dev wget curl llvm vim  
  
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash  
  
RUN echo 'eval "$(pyenv init -)"' > /root/.bashrc  
  
RUN pyenv install 2.7.8 && pyenv global 2.7.8  
  

