FROM centos:centos6  
  
MAINTAINER Gary Hai "gary@XL59.com"  
# update to latest version of centos6  
RUN yum -y update  
  
# install sshd  
RUN yum -y install openssh-server  
# generate default configuration.  
RUN service sshd start  
RUN service sshd stop  
  
# very simple password for root  
RUN echo "root:root" | chpasswd  
  
# install development envirenment  
RUN yum -y install gcc autoconf automake gcc-c++ libtool tar git subversion  
# install dependencies  
RUN yum -y install ncurses-devel libuuid-devel libxml2-devel sqlite-devel  
  
# install jason lib  
RUN mkdir -p /usr/local/src;\  
cd /usr/local/src;\  
git clone https://github.com/akheron/jansson.git;\  
cd jansson;\  
autoreconf -i;\  
./configure;\  
make;\  
make install  
  
# checkout trunk of asterisk and build it.  
RUN cd /usr/local/src;\  
svn checkout http://svn.asterisk.org/svn/asterisk/trunk asterisk;\  
cd asterisk;\  
./configure;\  
make && make install  
  
# clone erlang with HEAD checkout and build it  
RUN cd /usr/local/src;\  
git clone https://github.com/erlang/otp.git;\  
cd otp;\  
./otp_build autoconf;\  
./configure;\  
make;\  
make install  
  
#export ssh server port  
EXPOSE 22  
CMD /usr/sbin/sshd -D  

