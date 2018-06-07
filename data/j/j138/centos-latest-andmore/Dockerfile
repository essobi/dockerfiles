FROM centos:centos6  
MAINTAINER Junya Nakazato  
ENV HOME /root  
  
# package install  
RUN \  
yum -y install yum-plugin-fastestmirror; \  
echo "include_only=.jp" >> /etc/yum/pluginconf.d/fastestmirror.conf; \  
yum update -y  
  
ADD td.repo /etc/yum.repos.d/td.repo  
  
RUN \  
rpm --import http://rpms.famillecollet.com/RPM-GPG-KEY-remi; \  
rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6; \  
rpm --import http://apt.sw.be/RPM-GPG-KEY.dag.txt; \  
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm; \  
rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm; \  
rpm -ivh http://pkgs.repoforge.org/rpmforge-release/rpmforge-
release-0.5.3-1.el6.rf.x86_64.rpm; \  
rpm -ivh http://swiftsignal.com/packages/centos/6/x86_64/the-silver-
searcher-0.13.1-1.el6.x86_64.rpm  
  
RUN \  
yum --enablerepo=remi,epel,treasuredata install -y \  
sudo wget which tar bzip2 zip unzip telnet curl-devel git mercurial openssh-
server openssh-clients syslog gcc gcc-c++ libxml2 libxml2-devel libxslt
libxslt-devel readline readline-devel jemalloc jemmalloc-devel \  
httpd httpd-devel nginx mysql-server mysql-devel sqlite sqlite-devel redis td-
agent python python-devel python-pip \  
nodejs npm erlang zsh zsh-devel autojump htop colordiff autojump-zsh
the_silver_searcher bash-completion; \  
yum clean all  
  
# vim setup  
RUN \  
hg clone https://vim.googlecode.com/hg/ /usr/local/src/vim && \  
cd /usr/local/src/vim && \  
./configure \  
\--prefix=/usr/local/ \  
\--enable-fail-if-missing \  
\--enable-fontset \  
\--enable-pythoninterp \  
\--enable-cscope \  
\--enable-multibyte \  
\--with-x=no \  
\--disable-gui \  
\--disable-xim \  
\--with-features=huge \  
\--disable-selinux \  
\--disable-gpm \  
\--disable-darwin && \  
make && make install  
  
# tmux install  
RUN \  
cd /usr/local/src && \  
curl -O
https://cloud.github.com/downloads/libevent/libevent/libevent-2.0.21-stable.tar.gz
&& \  
tar xf libevent-2.0.21-stable.tar.gz && \  
cd libevent-2.0.21-stable && \  
./configure && make && make install && \  
echo "/usr/local/lib" > /etc/ld.so.conf.d/libevent.conf && \  
ldconfig && \  
ln -s /usr/local/lib/libevent-2.0.so.5 /usr/lib64/libevent-2.0.so.5  
  
RUN \  
cd /usr/local/src && \  
wget http://downloads.sourceforge.net/tmux/tmux-1.9a.tar.gz && \  
tar -xvf tmux-1.9a.tar.gz && \  
cd tmux-1.9a && \  
./configure && make && make install && \  
echo 'export TERM=xterm-256color' >> /root/.zshrc && \  
echo 'export TERM=xterm-256color' >> /root/.bashrc  
  

