################################################################################  
# DOCKER IMAGE BUILD FILE  
################################################################################  
FROM centos  
  
MAINTAINER Louie Menard <louie.menard@gmail.com>  
LABEL description="Centos"  
LABEL version="1.0"  
  
################################################################################  
# install packages  
################################################################################  
USER root  
RUN yum update -y  
RUN yum install -y zsh  
RUN yum install -y curl  
RUN yum install -y wget  
RUN yum install -y sudo  
RUN yum install -y vim  
RUN yum install -y git  
RUN yum install -y which  
RUN yum install -y unzip  
  
################################################################################  
# update root  
################################################################################  
RUN echo root:docker | chpasswd  
  
################################################################################  
# install zshell for root  
################################################################################  
USER root  
RUN sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -O -)"  
RUN wget https://raw.githubusercontent.com/babun/babun/master/babun-
core/plugins/oh-my-zsh/src/babun.zsh-theme -O ~/.oh-my-zsh/themes/babun.zsh-
theme  
ENV ZSH_THEME="babun"  
RUN sed -i 's/^ZSH_THEME.*$/ZSH_THEME=babun/' ~/.zshrc  
ENV SHELL="/bin/zsh"  
RUN rm /bin/sh && ln -sf /bin/zsh /bin/sh  
  
RUN sed -i '$i/bin/zsh' ~/.bashrc  
RUN set -o vi  
  
################################################################################  
# create new users  
################################################################################  
RUN adduser Louie  
RUN echo Louie:docker | chpasswd  
RUN usermod -aG wheel Louie  
  
################################################################################  
# install zshell for new users  
################################################################################  
USER Louie  
WORKDIR /home/Louie  
RUN sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -O -)"  
RUN wget https://raw.githubusercontent.com/babun/babun/master/babun-
core/plugins/oh-my-zsh/src/babun.zsh-theme -O ~/.oh-my-zsh/themes/babun.zsh-
theme  
ENV ZSH_THEME="babun"  
RUN sed -i 's/^ZSH_THEME.*$/ZSH_THEME=babun/' ~/.zshrc  
ENV SHELL="/bin/zsh"  
  
RUN sed -i '$i/bin/zsh' ~/.bashrc  
RUN set -o vi  
  
################################################################################  
# entry point  
################################################################################  
#ENTRYPOINT /bin/zsh  
  
  

