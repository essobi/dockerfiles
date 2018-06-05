# acs docker file  
FROM centos:centos6.9  
MAINTAINER Alexis Tejeda <github.com/atejeda/alma.scheduling.online.docker>  
  
# user setup  
USER root  
RUN echo "root:almadev" | chpasswd  
  
# setup  
RUN yum update -y  
RUN yum install -y http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum install -y redhat-lsb* kernel-devel wget man tree top htop openssh \  
openssh-server cvs git svn emacs vim gcc gcc-* fortran \  
java-1.7.0-openjdk* java-1.8.0-openjdk* maven ant* make \  
cmake libgfortran boost* openssl* lapack* libffi* \  
rpmrebuild mock rpm-devel dialog ksh service sshd start \  
liblockfile liblockfile-devel lockfile-progs lsb-release \  
procmail tmux  
  
RUN ln -s /usr/lib64/libgfortran.so.3 /usr/lib64/libgfortran.so.1  
RUN chkconfig --level 345 sshd on && service sshd start  
RUN echo "[[ -f \$HOME/alma.profile ]] && source alma.profile" >> /etc/bashrc  
RUN git clone https://github.com/atejeda/dotfiles /opt/dotfiles || true  
  
# entrypoint  
COPY entrypoint /usr/local/bin/entrypoint  
RUN chmod +x /usr/local/bin/entrypoint  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  

