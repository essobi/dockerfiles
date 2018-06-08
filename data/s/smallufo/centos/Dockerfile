FROM centos  
MAINTAINER smallufo smallufo@gmail.com  
  
RUN echo 'export LANG="zh_TW.UTF-8"' >> /root/.bashrc  
  
RUN echo 'export
PS1="\\[\033[1;33m\\]\u\\[\033[1;37m\\]@\\[\033[1;32m\\]\h\\[\033[1;37m\\]:\\[\033[1;31m\\]\w
\\[\033[1;36m\\]\$ \\[\033[0m\\]"' >> /root/.bashrc  
  
RUN echo 'export
PS1="\\[\033[1;33m\\]\u\\[\033[1;37m\\]@\\[\033[1;32m\\]\h\\[\033[1;37m\\]:\\[\033[1;31m\\]\w
\\[\033[1;36m\\]\$ \\[\033[0m\\]"' >> /etc/bashrc  
  
ENV TZ=Asia/Taipei  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs  
RUN yum -y update;  
  
RUN yum -y install wget unzip lynx elinks nmap  
RUN yum -y install openssh-clients openssh-server  
  
# nload exists in epel  
RUN yum -y install epel-release  
RUN yum -y install nload  
  
RUN yum clean all;  
  
ENV lang=zh_TW.UTF-8  
RUN useradd -ms /bin/bash smallufo  

