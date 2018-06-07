FROM gentoo/stage3-amd64  
  
MAINTAINER Milos Prchlik <happz@happz.cz>  
  
RUN wget -O /tmp/portage-latest.tar.bz2
http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2 \  
&& mkdir -p /usr \  
&& bzcat /tmp/portage-latest.tar.bz2 | tar -xf - -C /usr \  
&& mkdir -p /usr/portage/distfiles /usr/portage/metadata /usr/portage/packages
\  
&& echo "dev-vcs/git -perl -python -webdav" >> /etc/portage/package.use/git \  
&& emerge -v dev-vcs/git dev-util/ninja \  
&& rm -rf /usr/portage /tmp/portage-latest.tar.bz2  
  
RUN mkdir -p /llvm-build  
ADD Makefile /llvm-build/Makefile  
  
RUN wget \--no-check-certificate -O /tmp/cmake-3.5.2.tar.gz
http://www.cmake.org/files/v3.5/cmake-3.5.2.tar.gz \  
&& tar xf /tmp/cmake-3.5.2.tar.gz -C /tmp \  
&& cd /tmp/cmake-3.5.2 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd \  
&& rm -rf /tmp/cmake-3.5.2 /tmp/cmake-3.5.2.tar.gz  

