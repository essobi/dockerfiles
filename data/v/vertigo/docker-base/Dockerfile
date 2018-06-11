# Base CentOS 7 with a few perks  
# Includes epel repo  
  
FROM centos:latest  
  
MAINTAINER Andre Fernandes <andre@vertigo.com.br>  
  
ARG BASEREPO  
ARG EPELREPO  
  
ADD src/* /opt/  
  
RUN echo "Building docker-base..." && \  
cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-
Base.repo.original && \  
chmod +x /opt/setbaserepo.sh && \  
sh /opt/setbaserepo.sh && \  
yum update -y && \  
yum install net-tools iputils tar wget unzip epel-release -y && \  
cp /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo.original && \  
chmod +x /opt/setepelrepo.sh && \  
sh /opt/setepelrepo.sh && \  
yum -y install pwgen && \  
yum clean all  
  
#RUN yum -y install vim git && \  
# yum clean all && \  
# git clone https://github.com/VundleVim/Vundle.vim.git
~/.vim/bundle/Vundle.vim && \  
# wget https://git.vertigo.com.br/vertigobr/osx-shell/raw/master/vimrc -q -O
~/.vimrc  
#RUN echo | echo | vim +PluginInstall +PluginUpdate +qall &>/dev/null && \  
# alias vi=vim  

