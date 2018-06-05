FROM centos:7  
MAINTAINER Justin Wilson "sudo.justin.wilson@gmail.com"  
LABEL version=0.9  
LABEL asterisk_version=certified-11-LTS  
ENV REVISION 0.4  
# update system and install dependencies for Asterisk  
RUN yum install -y \  
gcc \  
curl \  
wget \  
gcc-c++ \  
libstdc++-devel \  
make \  
ncurses-devel \  
libxml2-devel \  
openssl-devel \  
libuuid-devel \  
vim \  
man-db \  
sqlite \  
sqlite-devel  
  
# create users and directories  
# download and extract Asterisk  
ENV ASTERISK_DOWNLOAD_URL
http://downloads.asterisk.org/pub/telephony/certified-asterisk/asterisk-
certified-11.6-current.tar.gz  
ENV ASTERISK_BUILDDIR /usr/local/src/  
ADD $ASTERISK_DOWNLOAD_URL $ASTERISK_BUILDDIR  
WORKDIR $ASTERISK_BUILDDIR  
RUN tar xvfz *asterisk*gz  
  
### NEW REVISED SECTION ###  
# install dependencies:  
RUN yum install -y svn epel-release \  
&& yum update -y  
  
RUN yum install -y libcurl-devel openssh openssh-server sudo visudo newt-devel
iproute  
  
# was having trouble creating a variables with BASH expansion. I ended up
creating a temp file that we can source....  
RUN echo 'ASTERISK_SOURCEDIR=$(ls "$ASTERISK_BUILDDIR"asterisk*[^gz] -d)' >>
~/.astersiskvars  
  
# This is to install dependencies with a tool shipped with the Asterisk source  
RUN source ~/.astersiskvars \  
&& pushd $ASTERISK_SOURCEDIR/contrib/scripts \  
&& ./install_prereq install \  
&& ./install_prereq install-unpackaged \  
&& pushd $ASTERISK_SOURCEDIR  
  
# change to build directory and configure:  
RUN source ~/.astersiskvars \  
&& cd $ASTERISK_SOURCEDIR \  
&& ./configure --libdir=/usr/lib64  
  
# You can add what modules you want to be compiled in, as an argument to
menuselect/menuselect --enable <MODULE>:  
RUN source ~/.astersiskvars \  
&& cd $ASTERISK_SOURCEDIR \  
&& make menuselect.makeopts \  
&& menuselect/menuselect --enable chan_sip --enable CORE-SOUNDS-EN_AU-WAV
--enable CORE-SOUNDS-EN_AU-ULAW --enable CORE-SOUNDS-EN_AU-ALAW --enable CORE-
SOUNDS-EN_AU-GSM - enable CORE-SOUNDS-EN_AU-G729 --enable CORE-SOUNDS-
EN_AU-G722 menuselect.makeopts \  
&& make \  
&& make install  
  
# if you want to add existing /etc/asterisk/*.conf files, tar them and put
them in the build context named "asterisk-etc-configs.tgz", or change the
following value:  
# Install personal /etc/asterisk files:  
ADD asterisk-etc-configs.tgz /etc/asterisk/  
  
# assign asterisk as the default user (unless the ASTERISKUSER env var is set
to something else):  
RUN echo "export ASTERISKUSER=${ASTERISKUSER:-'asterisk'}" >> ~/.astersiskvars  
  
RUN source ~/.astersiskvars \  
&& useradd -UmG wheel $ASTERISKUSER \  
&& echo ${ASTERISKUSER_PASSWORD:-'password'} | passwd --stdin $ASTERISKUSER \  
&& chown -R "$ASTERISKUSER":"$ASTERISKUSER"
{/var/lib,/var/spool,/var/log,/var/run}/asterisk \  
&& chown -R "$ASTERISKUSER":"$ASTERISKUSER" /etc/asterisk  
  
# clean up  
RUN rm -f ~/.astersiskvars  
  
WORKDIR /etc/asterisk  
  
CMD su - asterisk \  
&& /usr/sbin/asterisk  

