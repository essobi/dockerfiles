FROM centos:centos7  
  
# Yum packages  
RUN yum -y install
http://download.fedoraproject.org/pub/epel/beta/7/x86_64/epel-
release-7-0.2.noarch.rpm  
RUN yum -y update  
RUN yum -y install emacs-nox  
RUN yum -y install gcc  
RUN yum -y install git  
RUN yum -y install mlocate  
RUN yum -y install sudo  
RUN yum -y install tmux  
  
# User  
RUN useradd -u 1100 -g wheel stm  
RUN sed -i 's/.*wheel.*NOPASSWD.*/%wheel ALL=(ALL) NOPASSWD: ALL/'
/etc/sudoers  
ENV HOME /home/stm  
WORKDIR /home/stm  
  
# Symlinks  
RUN rm -f .emacs .bashrc .bash_profile  
RUN ln -s ~/configs/emacs/dot-emacs ~/.emacs  
RUN ln -s ~/configs/bash/bashrc ~/.bashrc  
RUN ln -s ~/configs/bash/bashrc ~/.bash_profile  
RUN ln -s ~/configs/git/gitconfig ~/.gitconfig  
RUN ln -s ~/configs/git/gitignore_global ~/.gitignore_global  
  
# Metadata  
VOLUME .ssh  
VOLUME save  
CMD bash  
  
# Add config files.  
ADD configs /home/stm/configs  
RUN chown -R stm /home/stm  
USER stm  

