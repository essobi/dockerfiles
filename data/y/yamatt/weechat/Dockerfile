FROM centos:7  
MAINTAINER fondu.io <maintainer@fondu.io>  
  
ENV RELEASE v1.6  
ENV INSTALL_PATH /opt/weechat  
  
RUN yum install -y \  
gcc \  
git \  
cmake \  
pkg-config \  
libncurses-devel \  
curl-devel \  
zlib \  
libgcrypt-devel \  
gettext-devel \  
gnutls-devel \  
aspell \  
aspell-devel \  
ca-certificates \  
perl-devel \  
ruby-2.3 \  
ruby-devel \  
rubygems \  
ncurses-devel \  
python-devel \  
python-setuptools \  
perl-ExtUtils-Embed  
  
ENV LC_ALL=en_US.utf8 LANG=en_US.utf8 TERM=screen-256color  
  
RUN git clone https://github.com/weechat/weechat.git  
WORKDIR weechat  
  
# checkout latest version  
RUN git checkout ${RELEASE}  
  
# compile  
RUN mkdir build  
WORKDIR build  
RUN cmake .. \  
-DCMAKE_INSTALL_PREFIX=${INSTALL_PATH} \  
-DWEECHAT_HOME=~ \  
&& make && make install  
  
# create low-level user  
RUN adduser weechat --home /home/weechat --uid 2000  
  
COPY aspell.conf /home/weechat/.aspell.conf  
  
RUN chown weechat:weechat /home/weechat/.aspell.conf  
  
USER weechat  
  
WORKDIR /home/weechat  
  
RUN mkdir aspell  
  
# Setup Weechat running dir  
VOLUME ["/home/weechat"]  
  
ENTRYPOINT ["/opt/weechat/bin/weechat"]  

