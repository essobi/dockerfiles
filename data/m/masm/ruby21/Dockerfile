FROM masm/archlinux  
MAINTAINER Marco Monteiro <marco@neniu.org>  
  
RUN pacman -Syq --needed --noconfirm --noprogressbar \  
autoconf \  
automake \  
bison \  
coreutils \  
file \  
flex \  
gcc \  
gcc-libs \  
git \  
imagemagick \  
libtool \  
m4 \  
make \  
patch \  
pkg-config \  
ruby2.1 \  
ruby2.1-bundler && \  
yes | pacman -Sqcc && \  
rm -rf /usr/share/man/*  
RUN ln -s /opt/ruby2.1/lib/ruby/gems/2.1.0/bin/bundle /usr/bin/bundle  
ENV
PATH=/opt/ruby2.1/bin:/opt/ruby2.1/lib/ruby/gems/2.1.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  

