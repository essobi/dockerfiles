FROM ubuntu:14.04  
MAINTAINER Jioh L. Jung "ziozzang@gmail.com"  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
ENV USER_ID ziozzang  
  
RUN sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list  
RUN apt-get update && apt-get -y -o Dpkg::Options::="--force-confold" upgrade  
RUN apt-get install -fy -qqy curl git-core sudo make build-essential libssl-
dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev  
  
RUN useradd -m ${USER_ID}  
RUN echo "${USER_ID} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN chsh -s /bin/bash ${USER_ID}  
  
WORKDIR /home/${USER_ID}  
USER ${USER_ID}  
ENV HOME /home/${USER_ID}  
  
# INSTALL  
RUN curl -k -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash  
  
ENV PYENVPATH $HOME/.pyenv  
ENV PATH $PYENVPATH/shims:$PYENVPATH/bin:$PATH  
RUN echo 'export PYENVPATH=$HOME/.pyenv' >> ~/.bashrc  
RUN echo 'export PATH=$PYENVPATH/shims:$PYENVPATH/bin:$PATH' >> ~/.bashrc  
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc  
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc  
RUN pyenv install $(pyenv install -l | grep " 2." | tail -n 1)  
RUN pyenv global $(pyenv install -l | grep " 2." | tail -n 1)  

