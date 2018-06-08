FROM centos:centos6  
MAINTAINER pepechoko  
  
RUN yum install -y \  
'perl(:MODULE_COMPAT_5.10.1)' \  
gcc \  
git \  
gpm \  
openssh \  
openssh-clients \  
openssh-server \  
sudo \  
which  
  
# install vim 7.4 && screeen 4.2  
ADD rpms/vim-* /tmp/  
ADD rpms/screen-* /tmp/  
  
RUN rpm -Uvh \  
/tmp/vim-filesystem-7.4.160-1.el6.x86_64.rpm \  
/tmp/vim-common-7.4.160-1.el6.x86_64.rpm \  
/tmp/vim-enhanced-7.4.160-1.el6.x86_64.rpm \  
/tmp/screen-4.2.1-4.el6.x86_64.rpm  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
  
RUN useradd -m -s /bin/bash dev  
RUN echo 'dev:password' | chpasswd  
RUN echo 'dev ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/dev  
  
## Set up SSH  
RUN \  
mkdir -p /home/dev/.ssh && \  
chown dev /home/dev/.ssh && \  
chmod 700 /home/dev/.ssh  
  
ADD keys/id_rsa.pub /home/dev/.ssh/authorized_keys  
  
RUN \  
chown dev /home/dev/.ssh/authorized_keys && \  
chmod 600 /home/dev/.ssh/authorized_keys  
  
RUN sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
RUN /usr/bin/ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -C '' -N ''  
RUN /usr/bin/ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -C '' -N ''  
  
# create dev user  
USER dev  
ENV HOME /home/dev  
  
RUN echo "export LC_CTYPE=en_US.UTF-8" >> ~/.bashrc  
RUN echo "export LC_ALL=en_US.UTF-8" >> ~/.bashrc  
  
# vim env setup  
ADD _vimrc $HOME/.vimrc  
RUN \  
mkdir -p ~/.vim/bundle && \  
git clone https://github.com/Shougo/neobundle.vim
$HOME/.vim/bundle/neobundle.vim && \  
git clone https://github.com/Shougo/vimproc.vim $HOME/.vim/bundle/vimproc.vim
&& \  
cd $HOME/.vim/bundle/vimproc.vim && \  
make && \  
cd ~/.vim/bundle/neobundle.vim/bin && \  
./neoinstall && \  
printf 'y' | vim +NeoBundleInstall +qa  
  
RUN mkdir $HOME/workspace  
  
USER root  
  
VOLUME $HOME/workspace  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  

