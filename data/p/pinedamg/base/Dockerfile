FROM debian:jessie  
MAINTAINER MPineda <pinedamg@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y install vim curl git bash-completion  
RUN git clone https://github.com/magicmonty/bash-git-prompt.git ~/.bash-git-
prompt --depth=1  
  
RUN echo '. /etc/bash_completion' >> ~/.bashrc  
RUN echo 'source ~/.bash-git-prompt/gitprompt.sh' >> ~/.bashrc  
RUN echo 'GIT_PROMPT_ONLY_IN_REPO=1' >> ~/.bashrc  
COPY .gitconfig /root/.gitconfig  
COPY ./aliases /root/.bash_aliases  
RUN echo 'source ~/.bash_aliases' >> ~/.bashrc  
  
RUN apt-get update && apt-get -y autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root

